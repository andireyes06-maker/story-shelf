#!/usr/bin/env python3
"""Sync drafted Arc 2 chapters from The Ura into the Story Shelf reader."""

import json
import re
from pathlib import Path


SOURCE_ROOT = Path.home() / "Documents/rien-schoolwork/The Ura/Story/Arc_02_Haejin"
SHELF_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = SHELF_ROOT / "index.html"
START = "        // ARC 2 CHAPTERS START"
END = "        // ARC 2 CHAPTERS END"

CHAPTERS = [
    (20, 1, "The Cleanest Cut", "CH001_DRAFT.md"),
    (21, 2, "Future Yield", "CH002_DRAFT.md"),
]


def smart_quotes(text):
    return re.sub(r'"([^"\n]+)"', lambda m: "“" + m.group(1) + "”", text)


def prose_blocks(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("\n---\n")
    if len(parts) < 3:
        raise ValueError(f"Expected draft delimiters in {path}")
    body = "\n---\n".join(parts[1:-1]).strip()
    blocks = []
    in_code = False
    system_lines = []
    paragraph = []

    def flush_paragraph():
        if paragraph:
            value = smart_quotes(" ".join(line.strip() for line in paragraph))
            blocks.append({"t": "p", "x": value})
            paragraph.clear()

    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            if in_code:
                blocks.append({"t": "sys", "x": system_lines[:]})
                system_lines.clear()
            in_code = not in_code
        elif in_code:
            if stripped:
                system_lines.append(stripped)
        elif stripped == "---":
            flush_paragraph()
            blocks.append({"t": "br"})
        elif not stripped:
            flush_paragraph()
        else:
            paragraph.append(line)
    flush_paragraph()
    return blocks


def chapter_object(site_id, arc_number, title, filename):
    number_words = {1: "One", 2: "Two"}
    chapter = {
        "id": site_id,
        "movement": "Arc Two · Movement I · The Price That Moved",
        "title": f"Chapter {number_words[arc_number]}: {title}",
        "blocks": prose_blocks(SOURCE_ROOT / filename),
    }
    raw = json.dumps(chapter, ensure_ascii=False, indent=10)
    lines = raw.splitlines()
    return "\n".join("        " + line for line in lines)


def main():
    html = INDEX_PATH.read_text(encoding="utf-8")
    if START not in html or END not in html:
        raise ValueError("Arc 2 sync markers are missing from index.html")
    payload = ",\n".join(chapter_object(*chapter) for chapter in CHAPTERS)
    replacement = START + "\n" + payload + "\n" + END
    html = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        replacement,
        html,
        flags=re.S,
    )
    INDEX_PATH.write_text(html, encoding="utf-8")
    print(f"Synced {len(CHAPTERS)} Arc 2 chapters into index.html")


if __name__ == "__main__":
    main()
