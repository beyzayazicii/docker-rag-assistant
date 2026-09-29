"""Docker dokümanları üzerinde yerel RAG soru-cevap (terminal arayüzü).

Kullanım: python rag.py
"""
import array
import sqlite3
import sys
import time

import config
from llm import Embedder, load_model

SYSTEM_PROMPT = f"""Sen Docker dokümantasyonu üzerine çalışan bir yardımcı asistansın.

Kurallar:
1. Yalnızca aşağıdaki "Bağlam" bölümündeki bilgilere dayanarak cevap ver. Kendi bilgini ekleme.
2. Cevabı her zaman Türkçe yaz. Başka bir dile (örneğin Çince veya İngilizce) geçme.
3. Docker komutlarını, dosya adlarını, seçenekleri ve teknik terimleri (container, image, volume, Dockerfile, network, Compose, bind mount, registry vb.) çevirme; olduğu gibi bırak.
4. Komutları her zaman ``` ile açılan bir kod bloğu içinde ver.
5. Kısa ve net cevap ver; soruda istenmeyen ek bilgi ekleme.
6. Bağlam soruyu cevaplamak için yeterli bilgi içermiyorsa, başka hiçbir şey yazmadan tam olarak şu cümleyi yaz:
{config.NO_ANSWER}"""

TRANSLATE_PROMPT = ("Translate the user's question about Docker from Turkish into English. "
                    "Keep Docker commands and technical terms unchanged. "
                    "Output only the English translation, nothing else.")

THINKING_LIMIT_MESSAGE = ("Model bu soru üzerinde düşünürken uzunluk sınırına ulaştı ve cevap "
                          "üretemedi. Soruyu daha kısa veya tek bir konuya odaklı sormayı deneyin.")


class RAG:
    def __init__(self):
        self.chunks = self._load_chunks()
        self.embedder = Embedder()
        self.chat_model = load_model(config.CHAT_MODEL)
        # Reasoning modeller (ör. qwen3.5) cevaptan önce </think> ile biten bir düşünme metni üretir
        self.reasoning = "reasoning" in (self.chat_model.info.capabilities or "")

        self.chat = self.chat_model.get_chat_client()
        self.chat.settings.temperature = config.TEMPERATURE
        self.chat.settings.max_tokens = config.MAX_TOKENS + (config.THINKING_TOKENS if self.reasoning else 0)

        self.translator = self.chat_model.get_chat_client()
        self.translator.settings.temperature = 0.0
        self.translator.settings.max_tokens = 100

    @staticmethod
    def _load_chunks():
        db = sqlite3.connect(config.DB_PATH)
        (model,) = db.execute("SELECT value FROM meta WHERE key = 'embed_model'").fetchone()
        if model != config.EMBED_MODEL:
            sys.exit(f"{config.DB_PATH} '{model}' ile oluşturulmuş, ayarlarda '{config.EMBED_MODEL}' var. "
                     "ingest.py'yi tekrar çalıştırın.")
        rows = db.execute("SELECT source, heading, text, embedding FROM chunks").fetchall()
        db.close()
        return [{"source": s, "heading": h, "text": t, "embedding": array.array("f", e)}
                for s, h, t, e in rows]

    def translate(self, question):
        messages = [{"role": "system", "content": TRANSLATE_PROMPT},
                    {"role": "user", "content": question}]
        text = self.translator.complete_chat(messages).choices[0].message.content
        return text.split("</think>", 1)[-1].strip()

    def retrieve(self, query, top_k=config.TOP_K):
        """Sorguya en benzer top_k parçayı [(skor, parça), ...] olarak döner."""
        qv = self.embedder.embed([config.QUERY_INSTRUCTION + query])[0]
        # Vektörler birim uzunlukta olduğundan kosinüs benzerliği = iç çarpım
        scored = [(sum(a * b for a, b in zip(qv, c["embedding"])), c) for c in self.chunks]
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:top_k]

    @staticmethod
    def build_messages(question, hits):
        context = "\n\n".join(
            f"[{i}] Kaynak: {c['source']} | {c['heading']}\n{c['text']}"
            for i, (_, c) in enumerate(hits, 1)
        )
        return [
            {"role": "system", "content": f"{SYSTEM_PROMPT}\n\nBağlam:\n{context}"},
            {"role": "user", "content": question},
        ]

    def _stream_answer(self, messages, thinking_out):
        """Modelin cevabını parça parça üretir. Reasoning modellerde düşünme metni
        gösterilmez, thinking_out listesine eklenir."""
        buffer = ""
        thinking = self.reasoning
        for chunk in self.chat.complete_streaming_chat(messages):
            content = chunk.choices[0].delta.content if chunk.choices else None
            if not content:
                continue
            if thinking:
                buffer += content
                if "</think>" not in buffer:
                    continue
                thinking = False
                head, content = buffer.split("</think>", 1)
                thinking_out.append(head.replace("<think>", "").strip())
                content = content.lstrip()
                if not content:
                    continue
            yield content
        if thinking:
            # Token sınırı düşünme bitmeden doldu; düşünme metni cevap olarak gösterilmez
            thinking_out.append(buffer.replace("<think>", "").strip())
            yield THINKING_LIMIT_MESSAGE

    def ask(self, question, translate=config.TRANSLATE_QUERY, on_token=None):
        """Soruyu cevaplar. on_token verilirse cevap parça parça ona gönderilir.
        Cevap, kaynaklar ve süreleri içeren bir sözlük döner."""
        t0 = time.perf_counter()
        query = self.translate(question) if translate else question
        t1 = time.perf_counter()
        hits = self.retrieve(query)
        t2 = time.perf_counter()

        below_threshold = hits[0][0] < config.MIN_SCORE
        thinking = []
        if below_threshold:
            # İlgili parça yok: model hiç çağrılmaz
            tokens = iter([config.NO_ANSWER])
        else:
            tokens = self._stream_answer(self.build_messages(question, hits), thinking)

        parts, first_token = [], None
        for token in tokens:
            first_token = first_token or time.perf_counter()
            parts.append(token)
            if on_token:
                on_token(token)
        t3 = time.perf_counter()

        return {
            "question": question,
            "query": query,
            "answer": "".join(parts).strip(),
            "thinking": "".join(thinking),
            "below_threshold": below_threshold,
            "hits": [{"score": round(s, 3), "source": c["source"], "heading": c["heading"]}
                     for s, c in hits],
            "time_translate": t1 - t0,
            "time_retrieve": t2 - t1,
            "time_first_token": (first_token or t3) - t0,
            "time_total": t3 - t0,
        }

    def close(self):
        self.embedder.model.unload()
        self.chat_model.unload()


def unique_hits(result):
    """Aynı dosya ve başlıktan gelen parçaları tekrar etmeden listeler."""
    seen, hits = set(), []
    for hit in result["hits"]:
        key = (hit["source"], hit["heading"])
        if key not in seen:
            seen.add(key)
            hits.append(hit)
    return hits


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("Modeller yükleniyor...")
    rag = RAG()
    print(f"Hazır. Sohbet modeli: {config.CHAT_MODEL} | {len(rag.chunks)} parça")
    print("Docker hakkında Türkçe soru sorun. Çıkmak için 'q' yazın.\n")
    try:
        while True:
            question = input("Soru: ").strip()
            if question.lower() in ("q", "quit", "exit", "çık"):
                break
            if not question:
                continue
            if rag.reasoning:
                print("\n(Model düşünüyor...)", flush=True)
            print("\nCevap: ", end="", flush=True)
            try:
                result = rag.ask(question, on_token=lambda t: print(t, end="", flush=True))
            except Exception as e:
                print(f"\n\n[Hata] Cevap üretilemedi: {e}\n")
                continue
            print("\n")
            if config.NO_ANSWER not in result["answer"]:
                print("Kaynaklar:")
                for hit in unique_hits(result):
                    print(f"  - {hit['source']} → {hit['heading']}  (benzerlik {hit['score']:.2f})")
            if result["query"] != question:
                print(f"(Arama sorgusu: {result['query']})")
            print(f"(Süre: {result['time_total']:.1f} sn)\n")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        rag.close()


if __name__ == "__main__":
    main()
