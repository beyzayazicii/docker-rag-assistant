"""docs/ altındaki Markdown dosyalarını parçalayıp embedding'leriyle SQLite'a yazar.

Kullanım: python ingest.py
"""
import array
import re
import sqlite3
import time
from pathlib import Path

import config
from llm import Embedder

MAX_CHARS = 1500   # bundan uzun bölümler paragraf sınırından tekrar bölünür
MIN_CHARS = 80     # bundan kısa (neredeyse boş) bölümler atılır
BATCH_SIZE = 16
# Sadece başka sayfalara link veren bölümler: bilgi içermez, aramada gürültü yapar
SKIP_HEADINGS = {"Next steps", "Additional resources", "Where to go next"}


def split_sections(text):
    """Markdown'ı başlıklara göre böler. [(başlık yolu, gövde), ...] döner."""
    sections = []
    path = []          # [(seviye, başlık), ...] örn. [(1, "Volumes"), (2, "Create a volume")]
    body = []
    in_code = False

    def flush():
        content = "\n".join(body).strip()
        if content:
            sections.append((" > ".join(h for _, h in path), content))
        body.clear()

    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
        m = None if in_code else re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            flush()
            level = len(m.group(1))
            path[:] = [p for p in path if p[0] < level] + [(level, m.group(2).strip())]
        else:
            body.append(line)
    flush()
    return sections


def split_long(body):
    """Uzun gövdeyi paragraf sınırlarından MAX_CHARS'ı aşmayan parçalara böler.
    Kod blokları bölünmez."""
    if len(body) <= MAX_CHARS:
        return [body]
    # Kod bloklarını bozmadan paragraflara ayır
    blocks, current, in_code = [], [], False
    for line in body.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
        if not line.strip() and not in_code:
            if current:
                blocks.append("\n".join(current))
                current = []
        else:
            current.append(line)
    if current:
        blocks.append("\n".join(current))

    # Boş satırsız uzun listeler/tablolar tek blok kalır; onları satır satır böl
    small_blocks = []
    for block in blocks:
        if len(block) > MAX_CHARS and not block.lstrip().startswith(("```", "~~~")):
            part = []
            for line in block.splitlines():
                if part and sum(len(x) + 1 for x in part) + len(line) > MAX_CHARS:
                    small_blocks.append("\n".join(part))
                    part = []
                part.append(line)
            small_blocks.append("\n".join(part))
        else:
            small_blocks.append(block)
    blocks = small_blocks

    pieces, piece = [], ""
    for block in blocks:
        if piece and len(piece) + len(block) + 2 > MAX_CHARS:
            pieces.append(piece)
            piece = block
        else:
            piece = f"{piece}\n\n{block}" if piece else block
    if piece:
        pieces.append(piece)
    return pieces


def build_chunks():
    chunks = []
    for path in sorted(Path(config.DOCS_DIR).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        # "Source: https://..." satırını parçalara katma
        text = re.sub(r"(?m)^Source: \S+\n", "", text)
        for heading, body in split_sections(text):
            if len(body) < MIN_CHARS or heading.split(" > ")[-1] in SKIP_HEADINGS:
                continue
            for piece in split_long(body):
                chunks.append({"source": path.name, "heading": heading, "text": piece})
    return chunks


def main():
    chunks = build_chunks()
    print(f"{len(chunks)} parça oluşturuldu ({config.DOCS_DIR}/ altındaki "
          f"{len(set(c['source'] for c in chunks))} dosyadan).")

    embedder = Embedder()
    start = time.perf_counter()
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        # Embedding'e dosya adı + başlık bilgisini de kat: arama isabeti artar
        texts = [f"{c['source']} | {c['heading']}\n\n{c['text']}" for c in batch]
        for chunk, vec in zip(batch, embedder.embed(texts)):
            chunk["embedding"] = vec
        print(f"\rEmbedding: {min(i + BATCH_SIZE, len(chunks))}/{len(chunks)}", end="", flush=True)
    print(f"\nEmbedding süresi: {time.perf_counter() - start:.1f} sn")

    db = sqlite3.connect(config.DB_PATH)
    db.executescript("""
        DROP TABLE IF EXISTS chunks;
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            source TEXT NOT NULL,
            heading TEXT NOT NULL,
            text TEXT NOT NULL,
            embedding BLOB NOT NULL       -- float32 dizisi, birim uzunlukta
        );
        DROP TABLE IF EXISTS meta;
        CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
    """)
    db.executemany(
        "INSERT INTO chunks (source, heading, text, embedding) VALUES (?, ?, ?, ?)",
        [(c["source"], c["heading"], c["text"], array.array("f", c["embedding"]).tobytes())
         for c in chunks],
    )
    db.execute("INSERT INTO meta VALUES ('embed_model', ?)", (config.EMBED_MODEL,))
    db.commit()
    db.close()
    embedder.model.unload()
    print(f"{len(chunks)} parça {config.DB_PATH} dosyasına kaydedildi.")


if __name__ == "__main__":
    main()
