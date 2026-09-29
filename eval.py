"""RAG sistemini eval_questions.json'daki sorularla ölçer, sonuçları Markdown tablo olarak yazar.

Kullanım:
    python eval.py                                   # ayarlardaki model -> results.md
    python eval.py --model qwen2.5-7b --out results_qwen2.5-7b.md
    python eval.py --modes both                      # çeviri kapalı ve açık karşılaştırması
    python eval.py --ids 8,9,10 --min-score 0        # eşik kapalıyken yalnızca tuzak sorular
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

import config

MODES = [("kapalı", False), ("açık", True)]
CJK = re.compile(r"[぀-ヿ㐀-䶿一-鿿가-힯]")


def normalize(text):
    return " ".join(re.sub(r"[^\w\s-]", " ", text.lower()).split())


def said_no_answer(answer):
    """(birebir, gevşek): cevap tam olarak ret cümlesi mi / ret cümlesini içeriyor mu."""
    strict = answer.strip() == config.NO_ANSWER
    loose = normalize("dokümanlarda bilgi bulamadım") in normalize(answer)
    return strict, loose


def has_command(answer, commands):
    text = " ".join(answer.lower().split())
    return any(" ".join(c.lower().split()) in text for c in commands)


def evaluate(rag, question, translate):
    r = rag.ask(question["question"], translate=translate)
    strict, loose = said_no_answer(r["answer"])
    sources = [h["source"] for h in r["hits"]]
    row = {
        "id": question["id"],
        "type": question["type"],
        "question": question["question"],
        "query": r["query"],
        "answer": r["answer"],
        "hits": r["hits"],
        "top_score": r["hits"][0]["score"],
        "below_threshold": r["below_threshold"],
        "no_answer_strict": strict,
        "no_answer_loose": loose,
        "cjk": bool(CJK.search(r["answer"])),
        "thinking": r["thinking"],
        "time_total": round(r["time_total"], 1),
        "time_first_token": round(r["time_first_token"], 1),
    }
    if question["type"] == "answerable":
        row["source_hit"] = any(s in question["expected_sources"] for s in sources)
        row["command_hit"] = (has_command(r["answer"], question["expected_commands"])
                              if question["expected_commands"] else None)
    return row


def pct(values):
    values = [v for v in values if v is not None]
    if not values:
        return "-"
    return f"{sum(values)}/{len(values)} (%{100 * sum(values) / len(values):.0f})"


def avg(values):
    return f"{sum(values) / len(values):.1f} sn" if values else "-"


def summary(rows):
    ans = [r for r in rows if r["type"] == "answerable"]
    trap = [r for r in rows if r["type"] == "trap"]
    return {
        "Doğru kaynak getirildi (cevaplı sorular)": pct([r["source_hit"] for r in ans]),
        "Beklenen komut cevapta var": pct([r["command_hit"] for r in ans]),
        "Tuzak: ret cümlesi birebir": pct([r["no_answer_strict"] for r in trap]),
        "Tuzak: ret cümlesi geçiyor (gevşek)": pct([r["no_answer_loose"] for r in trap]),
        "Cevaplı soruda yanlışlıkla ret": pct([r["no_answer_loose"] for r in ans]),
        "Cevapta Çince/CJK karakter": pct([r["cjk"] for r in rows]),
        "Ortalama cevap süresi (cevaplı sorular)": avg([r["time_total"] for r in ans]),
        "Ortalama ilk kelime süresi (cevaplı sorular)": avg([r["time_first_token"] for r in ans]),
    }


def mark(value):
    return "-" if value is None else ("✅" if value else "❌")


def keep_awake():
    """Windows'un uzun ölçüm sırasında bekleme moduna geçmesini engeller
    (bekleme modunda model çağrısı donup kalabiliyor). Kapak kapatılırsa etkisizdir."""
    if sys.platform == "win32":
        import ctypes
        es_continuous, es_system_required, es_display_required = 0x80000000, 0x1, 0x2
        ctypes.windll.kernel32.SetThreadExecutionState(
            es_continuous | es_system_required | es_display_required)


def write_report(path, model, results, total_minutes):
    modes = list(results)
    first = results[modes[0]]
    lines = [
        f"# Değerlendirme sonuçları: `{model}`",
        "",
        f"- Embedding: `{config.EMBED_MODEL}`, TOP_K = {config.TOP_K}, "
        f"MIN_SCORE = {config.MIN_SCORE}, sıcaklık = {config.TEMPERATURE}",
        f"- Soru sayısı: {len(first)} "
        f"({sum(r['type'] == 'answerable' for r in first)} cevaplı, "
        f"{sum(r['type'] == 'trap' for r in first)} tuzak)",
        f"- Toplam çalışma süresi: {total_minutes:.1f} dk",
        "",
        "## Özet",
        "",
        "| Ölçüm | " + " | ".join(f"Çeviri {m}" for m in modes) + " |",
        "|---|" + "---|" * len(modes),
    ]
    summaries = [summary(results[m]) for m in modes]
    for key in summaries[0]:
        lines.append(f"| {key} | " + " | ".join(s[key] for s in summaries) + " |")

    label = " / ".join(m[0].upper() for m in modes)
    lines += [
        "",
        "## Soru bazında",
        "",
        f"Sütunlarda {label}: çeviri " + " / ".join(modes) + ". "
        "Kaynak = beklenen dosya ilk TOP_K parça içinde mi; Komut = beklenen komut cevapta mı; "
        "Ret = ret cümlesi geçiyor mu (tuzakta ✅, cevaplı soruda ❌ iyidir); "
        "Skor = en iyi parçanın benzerliği.",
        "",
        f"| # | Tür | Soru | Kaynak ({label}) | Komut ({label}) | Ret ({label}) "
        f"| Skor ({label}) | Süre sn ({label}) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for rows in zip(*(results[m] for m in modes)):
        r0 = rows[0]
        tur = "cevaplı" if r0["type"] == "answerable" else "tuzak"
        cell = lambda f: " / ".join(f(r) for r in rows)
        lines.append(
            f"| {r0['id']} | {tur} | {r0['question']} "
            f"| {cell(lambda r: mark(r.get('source_hit')))} "
            f"| {cell(lambda r: mark(r.get('command_hit')))} "
            f"| {cell(lambda r: mark(r['no_answer_loose']))} "
            f"| {cell(lambda r: format(r['top_score'], '.2f'))} "
            f"| {cell(lambda r: str(r['time_total']))} |"
        )
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=config.CHAT_MODEL)
    parser.add_argument("--out", default="results.md")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--ids", default=None, help="sadece bu sorular, örn. 8,9,10")
    parser.add_argument("--min-score", type=float, default=None,
                        help="config.MIN_SCORE'u geçersiz kıl (0 = eşik kapalı)")
    parser.add_argument("--modes", choices=["both", "off", "on"],
                        default="on" if config.TRANSLATE_QUERY else "off",
                        help="çeviri adımı: both = kapalı ve açık, off = kapalı, on = açık")
    args = parser.parse_args()
    modes = {"both": MODES, "off": MODES[:1], "on": MODES[1:]}[args.modes]
    sys.stdout.reconfigure(encoding="utf-8")
    keep_awake()

    config.CHAT_MODEL = args.model  # RAG, modeli ayarlardan okur
    if args.min_score is not None:
        config.MIN_SCORE = args.min_score
    from rag import RAG

    questions = json.loads(Path("eval_questions.json").read_text(encoding="utf-8"))
    if args.ids:
        wanted = {int(i) for i in args.ids.split(",")}
        questions = [q for q in questions if q["id"] in wanted]
    if args.limit:
        questions = questions[:args.limit]

    rag = RAG()
    start = time.perf_counter()
    results = {}
    try:
        for mode, translate in modes:
            results[mode] = []
            for q in questions:
                row = evaluate(rag, q, translate)
                results[mode].append(row)
                status = (f"kaynak={mark(row['source_hit'])} komut={mark(row['command_hit'])}"
                          if q["type"] == "answerable" else f"ret={mark(row['no_answer_loose'])}")
                print(f"[çeviri {mode}] #{q['id']:>2} {status} skor={row['top_score']:.2f} "
                      f"{row['time_total']:.0f} sn", flush=True)
    finally:
        rag.close()

    total_minutes = (time.perf_counter() - start) / 60
    raw_path = Path(args.out).with_suffix(".json")
    raw_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(args.out, args.model, results, total_minutes)
    print(f"\nSonuçlar: {args.out} (ham cevaplar: {raw_path})")


if __name__ == "__main__":
    main()
