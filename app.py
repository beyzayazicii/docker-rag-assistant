"""Yerel web arayüzü (yalnızca Python standart kütüphanesi).

Kullanım: python app.py  ->  tarayıcıda http://localhost:8000
"""
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import config
from rag import RAG, unique_hits

HOST, PORT = "127.0.0.1", 8000   # sadece bu bilgisayardan erişilebilir
INDEX = Path(__file__).parent / "web" / "index.html"

rag = None
lock = threading.Lock()   # model aynı anda tek soruyu cevaplayabilir


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/info":
            body = json.dumps({
                "chat_model": config.CHAT_MODEL,
                "embed_model": config.EMBED_MODEL,
                "chunks": len(rag.chunks),
                "docs": len({c["source"] for c in rag.chunks}),
            }).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path not in ("/", "/index.html"):
            self.send_error(404)
            return
        body = INDEX.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/ask":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            question = json.loads(self.rfile.read(length).decode("utf-8")).get("question", "").strip()
        except (UnicodeDecodeError, json.JSONDecodeError, AttributeError):
            self.send_error(400, "Geçersiz istek (UTF-8 JSON bekleniyor)")
            return
        if not question:
            self.send_error(400, "Soru boş")
            return

        # Cevap satır satır JSON olarak (NDJSON) akış halinde gönderilir
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        def send(event):
            self.wfile.write((json.dumps(event, ensure_ascii=False) + "\n").encode("utf-8"))
            self.wfile.flush()

        try:
            if not lock.acquire(blocking=False):
                send({"type": "status", "text": "Sırada bekleniyor"})
                lock.acquire()
            try:
                send({"type": "status", "text": "Model düşünüyor" if rag.reasoning
                      else "Model dokümanları okuyor"})
                result = rag.ask(question, on_token=lambda t: send({"type": "token", "text": t}))
            finally:
                lock.release()
            sources = [] if config.NO_ANSWER in result["answer"] else [
                {"file": h["source"], "heading": h["heading"], "score": h["score"]}
                for h in unique_hits(result)
            ]
            send({"type": "done", "sources": sources, "seconds": round(result["time_total"], 1)})
        except (BrokenPipeError, ConnectionResetError):
            pass   # kullanıcı sayfayı kapattı
        except Exception as e:
            try:
                send({"type": "error", "text": f"Cevap üretilemedi: {e}"})
            except OSError:
                pass

    def log_message(self, fmt, *args):
        pass   # terminali her istekle doldurma


def main():
    global rag
    sys.stdout.reconfigure(encoding="utf-8")
    print("Modeller yükleniyor...")
    rag = RAG()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Hazır. Tarayıcıda aç: http://localhost:{PORT}  (kapatmak için Ctrl+C)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        rag.close()


if __name__ == "__main__":
    main()
