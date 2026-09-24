#!/usr/bin/env python3
"""
Sync the Codex's reference documents from the actual "The Ura" project files.

What it does: copies each source .md file into codex/, wrapping any ASCII-art
table (the "+----+----+" style tables used in the World Bible etc.) in a
fenced code block first, so the Codex's markdown renderer (marked.js) shows
them as clean monospace blocks instead of mangling them as prose.

Run this after editing any of the source files below, then commit + push
codex/*.md. It's idempotent — safe to re-run any time.

Usage:
    python3 scripts/sync_codex.py
"""
import re
import os

# Adjust if either project moves relative to the other.
SRC_ROOT = os.path.expanduser("~/Documents/rien-schoolwork/The Ura")
DST_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "codex")

FILES = [
    ("Bible/01_WORLD_BIBLE.md", "world-bible.md"),
    ("Bible/02_CHARACTERS.md", "characters.md"),
    ("Bible/03_MAGIC_AND_SYSTEM.md", "magic-and-system.md"),
    ("Bible/04_CONTINUITY_AND_MYSTERIES.md", "continuity-and-mysteries.md"),
    ("Craft/WRITING_RULEBOOK.md", "craft-rulebook.md"),
    ("Story/01_SAGA_ARCHITECTURE.md", "saga-architecture.md"),
    ("Story/Arc_01_Yamashiro/ARC_01_PLAN.md", "arc-01-plan.md"),
    ("Story/Arc_01_Yamashiro/ARC_01_CAST.md", "arc-01-cast.md"),
    ("Story/Arc_01_Yamashiro/CHAPTER_OUTLINE.md", "chapter-outline.md"),
    ("Story/Arc_02_Haejin/ARC_02_PLAN.md", "arc-02-plan.md"),
    ("Story/Arc_02_Haejin/ARC_02_CAST.md", "arc-02-cast.md"),
    ("Story/Arc_02_Haejin/CHAPTER_OUTLINE.md", "arc-02-chapter-outline.md"),
    ("CODEX_PROMPTING_RULES.md", "prompting-rules.md"),
    ("00_PROJECT_INDEX.md", "project-index.md"),
    # Deliberately excluded: Bible/handoff.md and AI_CONTEXT.md — both are
    # pre-reorg originals, explicitly superseded by the files above per
    # SESSION_HANDOFF.md. Add them here if that ever changes.
]


def is_table_line(line):
    s = line.rstrip("\n")
    if re.match(r"^\+[-+]+\+\s*$", s):
        return True
    if s.startswith("|") and s.count("|") >= 2:
        return True
    return False


def wrap_ascii_tables(text):
    lines = text.split("\n")
    out = []
    in_fence = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if not in_fence and is_table_line(line):
            block = []
            while i < n and (
                is_table_line(lines[i])
                or (block and lines[i].strip() == "" and i + 1 < n and is_table_line(lines[i + 1]))
            ):
                block.append(lines[i])
                i += 1
            while block and block[-1].strip() == "":
                block.pop()
                i -= 1
            out.append("```")
            out.extend(block)
            out.append("```")
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def main():
    for src_rel, dst_name in FILES:
        src_path = os.path.join(SRC_ROOT, src_rel)
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
        processed = wrap_ascii_tables(text)
        dst_path = os.path.join(DST_ROOT, dst_name)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(processed)
        print(f"{src_rel} -> codex/{dst_name} ({len(processed)} bytes)")


if __name__ == "__main__":
    main()
