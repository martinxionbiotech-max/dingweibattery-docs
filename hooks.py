# mkdocs hooks: post-build Markdown mirrors (Plan A — no paid Cloudflare Markdown for Agents)
# Copies the original .md sources into site/md/ so AI crawlers can fetch pure markdown,
# generates site/llms-full.txt (whole corpus), and writes site/_headers content-type rules.
import shutil
import time
from pathlib import Path

def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    generated_on = time.strftime("%Y-%m-%d")
    md_root = site_dir / "md"
    if md_root.exists():
        shutil.rmtree(md_root)
    md_root.mkdir(parents=True, exist_ok=True)

    corpus = []

    for src in sorted(docs_dir.rglob("*.md")):
        if src.name == "llms.txt":
            continue
        rel = src.relative_to(docs_dir)  # e.g. specs/jis-145g51/index.md
        out = md_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)
        text = src.read_text(encoding="utf-8")
        # URL: docs site serves /<path without index.md>/
        url_path = rel.as_posix()
        if url_path.endswith("/index.md"):
            url_path = url_path[: -len("index.md")]
        elif url_path.endswith(".md"):
            url_path = url_path[: -len(".md")]
        corpus.append(
            f"---\n\n# {rel.as_posix()}\n\n> Source: https://docs.dingweibattery.com/{url_path}\n> Generated: {generated_on}\n\n{text}"
        )

    full = (
        "# Dingwei Battery Technical Documentation — Full Markdown Corpus\n\n"
        f"> Source: https://docs.dingweibattery.com\n> Generated: {generated_on}\n"
    ) + "\n".join(corpus)
    (site_dir / "llms-full.txt").write_text(full, encoding="utf-8")

    headers = """\
/md/*
  Content-Type: text/markdown; charset=utf-8
  Cache-Control: public, max-age=0, must-revalidate

/llms-full.txt
  Content-Type: text/markdown; charset=utf-8
  Cache-Control: public, max-age=0, must-revalidate
"""
    existing = site_dir / "_headers"
    if existing.exists() and "/md/*" not in existing.read_text(encoding="utf-8"):
        existing.write_text(existing.read_text(encoding="utf-8") + "\n" + headers, encoding="utf-8")
    elif not existing.exists():
        existing.write_text(headers, encoding="utf-8")

    print(f"[md-hook] {len(corpus)} markdown mirrors -> site/md/ ; llms-full.txt written")
