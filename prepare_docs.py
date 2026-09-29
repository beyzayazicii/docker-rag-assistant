"""docker/docs reposundan seçilen dosyaları temizleyip docs/ klasörüne yazar.

Önce repoyu klonla:
    git clone --depth 1 --filter=blob:none --sparse https://github.com/docker/docs.git _docker-docs-src
    cd _docker-docs-src && git sparse-checkout set content data/cli
Sonra:
    pip install pyyaml
    python prepare_docs.py
"""
import re
from pathlib import Path

import yaml

SRC = Path("_docker-docs-src")
OUT = Path("docs")

# (kaynak dosya, docs/ içindeki yeni ad)
CONCEPTS = "content/get-started/docker-concepts"
MARKDOWN_FILES = [
    ("content/get-started/docker-overview.md", "overview.md"),
    (f"{CONCEPTS}/the-basics/what-is-a-container.md", "what-is-a-container.md"),
    (f"{CONCEPTS}/the-basics/what-is-an-image.md", "what-is-an-image.md"),
    (f"{CONCEPTS}/the-basics/what-is-a-registry.md", "what-is-a-registry.md"),
    (f"{CONCEPTS}/building-images/writing-a-dockerfile.md", "writing-a-dockerfile.md"),
    ("content/manuals/build/concepts/dockerfile.md", "dockerfile-concepts.md"),
    (f"{CONCEPTS}/building-images/build-tag-and-publish-an-image.md", "build-tag-and-publish-an-image.md"),
    (f"{CONCEPTS}/building-images/understanding-image-layers.md", "understanding-image-layers.md"),
    (f"{CONCEPTS}/building-images/multi-stage-builds.md", "multi-stage-builds.md"),
    (f"{CONCEPTS}/running-containers/publishing-ports.md", "publishing-ports.md"),
    (f"{CONCEPTS}/running-containers/overriding-container-defaults.md", "overriding-container-defaults.md"),
    (f"{CONCEPTS}/running-containers/persisting-container-data.md", "persisting-container-data.md"),
    ("content/manuals/engine/storage/volumes.md", "storage-volumes.md"),
    ("content/manuals/engine/storage/bind-mounts.md", "storage-bind-mounts.md"),
    ("content/manuals/engine/network/_index.md", "networking-overview.md"),
    ("content/manuals/engine/network/drivers/bridge.md", "network-bridge-driver.md"),
    (f"{CONCEPTS}/the-basics/what-is-docker-compose.md", "what-is-docker-compose.md"),
    ("content/manuals/compose/gettingstarted.md", "compose-getting-started.md"),
]

# data/cli altındaki YAML dosyaları (docker build için güncel BuildKit/buildx sayfası kullanılır)
CLI_FILES = [
    "engine/docker_container_run", "engine/docker_container_ls", "engine/docker_container_exec",
    "engine/docker_container_logs", "engine/docker_container_stop", "engine/docker_container_rm",
    "buildx/docker_buildx_build", "engine/docker_image_ls", "engine/docker_image_pull",
    "engine/docker_volume_create", "engine/docker_network_create",
]
CLI_OUT = "docker-cli-common.md"
MAX_EXAMPLES_CHARS = 5000  # docker run örnekleri tek başına ~50 KB
RUN_MAX_EXAMPLES_CHARS = 12000  # en sık kullanılan komut, daha fazla örnek tut
# Örnekler kırpılırken başlığında bunlar geçenler önce seçilir
COMMON_FLAGS = {"--name", "-p", "-v", "--mount", "-e", "-d", "-i", "-t", "--rm",
                "--restart", "--network", "-a", "--all", "-f", "--follow", "--tail",
                "--force", "--tag", "--file", "--build-arg", "--target", "--driver"}

HTML_TAGS = r"(?:div|span|p|br|img|a|iframe|details|summary|section|figure|figcaption|table|thead|tbody|tr|td|th|sup|sub|small|video|source)"


def clean_line(line):
    """Kod bloğu dışındaki bir satırı temizler."""
    line = re.sub(r"\{\{[<%]\s*tab\s+name=\"([^\"]+)\"[^}]*[>%]\}\}", r"**\1**", line)
    line = re.sub(r"\{\{[<%].*?[>%]\}\}", "", line)            # kalan shortcode'lar
    line = re.sub(r"<!--.*?-->", "", line)                       # HTML yorumları
    line = re.sub(rf"</?{HTML_TAGS}\b[^>]*>", "", line, flags=re.I)
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)             # resimler
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)         # [metin](link) -> metin
    line = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", line)        # [metin][ref] -> metin
    line = re.sub(r"\s*\{\s*#[^}]*\}\s*$", "", line)             # başlık id'leri {#id}
    if re.match(r"^\s*\[[^\]]+\]:\s*\S+", line):                 # [ref]: url satırları
        return ""
    return line.rstrip()


def clean_markdown(text):
    in_code = False
    lines = []
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            # Hugo kod bloğu seçeneklerini at: ```console {title="..."} -> ```console
            lines.append(re.sub(r"\s*\{.*\}\s*$", "", line.rstrip()))
            continue
        lines.append(line.rstrip() if in_code else clean_line(line))
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def convert_markdown(src, dest):
    raw = (SRC / src).read_text(encoding="utf-8").replace("\r\n", "\n")
    meta, body = split_front_matter(raw)
    title = meta.get("title") or dest
    header = f"# {title}\n\nSource: https://github.com/docker/docs/blob/main/{src}\n\n"
    (OUT / dest).write_text(header + clean_markdown(body), encoding="utf-8")


def select_examples(examples, limit=MAX_EXAMPLES_CHARS):
    """Uzun örnek listesini kısaltır; sık kullanılan bayrakların örneklerini tercih eder."""
    if len(examples) <= limit:
        return examples
    sections = re.split(r"(?m)^(?=#### )", examples)
    intro = sections[0] if not sections[0].startswith("#### ") else ""
    sections = [s for s in sections if s.startswith("#### ")]
    common = [s for s in sections
              if COMMON_FLAGS & set(re.findall(r"(?<![\w-])--?[\w-]+", s.splitlines()[0]))]
    others = [s for s in sections if s not in common]
    chosen, total = [], len(intro)
    for s in common + others:
        if total + len(s) <= limit:
            chosen.append(s)
            total += len(s)
    chosen.sort(key=sections.index)  # orijinal sırayı koru
    return intro + "".join(chosen)


def convert_cli():
    parts = ["# Common Docker CLI commands\n",
             "Source: https://github.com/docker/docs/tree/main/data/cli\n"]
    for name in CLI_FILES:
        data = yaml.safe_load((SRC / "data/cli" / f"{name}.yaml").read_text(encoding="utf-8"))
        cmd = data["command"]
        parts.append(f"## {cmd}\n")
        parts.append(f"{data.get('short', '')}\n")
        if data.get("aliases"):
            parts.append(f"Aliases: {data['aliases']}\n")
        parts.append(f"Usage:\n\n```console\n{data['usage']}\n```\n")
        if data.get("long"):
            parts.append(f"### Description of {cmd}\n\n{data['long']}\n")
        options = [o for o in data.get("options", [])
                   if not o.get("hidden") and not o.get("deprecated")]
        if options:
            lines = []
            for o in options:
                flag = f"`--{o['option']}`" + (f", `-{o['shorthand']}`" if o.get("shorthand") else "")
                desc = " ".join(str(o.get("description", "")).split())
                lines.append(f"- {flag}: {desc}")
            parts.append(f"### Options of {cmd}\n\n" + "\n".join(lines) + "\n")
        examples = data.get("examples")
        if examples:
            # Örnek başlıklarını "### Examples of ..." altına sığacak şekilde bir seviye aşağı al
            examples = re.sub(r"^### ", "#### ", examples, flags=re.M)
            limit = RUN_MAX_EXAMPLES_CHARS if cmd == "docker container run" else MAX_EXAMPLES_CHARS
            examples = select_examples(examples, limit)
            parts.append(f"### Examples of {cmd}\n\n{examples}\n")
    text = clean_markdown("\n".join(parts))
    (OUT / CLI_OUT).write_text(text, encoding="utf-8")


def main():
    OUT.mkdir(exist_ok=True)
    for src, dest in MARKDOWN_FILES:
        convert_markdown(src, dest)
    convert_cli()
    for f in sorted(OUT.glob("*.md")):
        print(f"{f.stat().st_size:7d}  {f.name}")


if __name__ == "__main__":
    main()
