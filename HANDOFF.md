# Story Shelf — Handoff

**Purpose:** bring a brand-new session fully current on this repo without re-deriving its structure from scratch. This is a *separate* project from "The Ura" itself — it's the private reading site, not the story files. For narrative/worldbuilding state, see `SESSION_HANDOFF.md` in "The Ura" project instead.

**Live:** https://andireyes06-maker.github.io/story-shelf/
**Repo:** `github.com/andireyes06-maker/story-shelf` (public — required for free-tier GitHub Pages; reachable by anyone with the link, not listed anywhere)
**Source of truth it depends on:** `/Users/rien/Documents/rien-schoolwork/The Ura/` — chapters and reference docs both originate there, not here.

---

## What This Is

A small private "library" site, built because the author didn't want to keep reading draft chapters as a Claude Artifact and wanted something of their own on GitHub Pages instead. Two things live on it:

1. **Story chapters** — currently just The Ura, Chapters One through Nineteen, kept in sync with `Story/Arc_01_Yamashiro/CHXXX_DRAFT.md` in the main project.
2. **A Codex** — 11 reference documents (World Bible, Characters, Magic & System, Continuity & Mysteries, Craft Rulebook, Saga Architecture, Arc 1 Plan/Cast, Chapter Outline, Prompting Rules), synced from the actual project files rather than hand-copied.

It's one file, `index.html` — no build step, no framework, no `node_modules`. Deploys by pushing to `main`; GitHub Pages serves it directly.

---

## Architecture, in Enough Detail to Extend It

**Everything is one HTML file** with inline `<style>` and one inline `<script>` at the bottom. It's a tiny client-side "app" with three views, switched by a `state.view` string (`'home' | 'reader' | 'codex'`) and rendered by swapping `#app`'s `innerHTML`:

- `renderHome()` — the shelf. Currently one story card + one Codex card. Add a second story by adding a second `STORIES` entry and a second card in this function.
- `renderReader()` — chapter prose. Reads from `STORIES.ura.chapters[]`.
- `renderCodex()` — reference docs. Reads from the `CODEX_DOCS` array, fetches the matching `codex/*.md` file on demand, renders it with `marked.js` (loaded from cdnjs, pinned to `4.3.0`), and caches the rendered HTML in memory per session.

**Chapter data format** — each chapter is `{ id, movement, title, blocks: [...] }`, where each block is one of:
- `{t:"p", x:"..."}` — a paragraph. `*text*` inside becomes `<em>` (see the `em()` helper). Dialogue uses curly quotes (`“` / `”`) as a house style, not straight `"` — matching the convention already used throughout, and necessary anyway since blocks are double-quoted JS strings.
- `{t:"br"}` — a scene break (renders as `◆ ◆ ◆`).
- `{t:"sys"}, x:[...]}` — a System-text panel (Chapter 1's `[MARKING CONFIRMED.]` etc.) — an array of bracket lines, rendered in a distinct monospace box. Only used where the source prose actually formats it as a fenced ` ``` ` block of bracket lines; a single italicized bracket phrase inline in prose (e.g. Chapter 3's `*[CONTACT: UNRESOLVED.]*`) should stay a normal `p` block instead — that distinction is intentional, matching how the source chapters format the two differently.

**To add a new chapter:** open the relevant `CHXXX_DRAFT.md` in the main project, strip its title/revision-history preamble, convert straight dialogue quotes to curly, and append a new chapter object to `STORIES.ura.chapters` following the pattern above. Then run the syntax check before pushing (see "Before You Push," below) — it's caught real mistakes twice already.

**Theming — this matters for adding a second story:** CSS custom properties are defined twice. `:root` holds neutral "chrome" tokens (the shelf, the header — Libre Franklin, muted green accent) shared by everything. `.ura-theme` *redefines the same token names* (Shippori Mincho, ash/ember palette) scoped to that class. `renderReader()` and the story card both add `class="ura-theme"` to pick up Ura's look; the shelf/header never does. **A second story should get its own scoped class** (e.g. `.newstory-theme`) with its own token values, following the exact same pattern — don't reuse `.ura-theme` for a different story's content, and don't theme the shared chrome (header, shelf background).

**The Codex is intentionally wider than the chapter reader** (`main.reader.codex-wide` → 1180px vs. the default 680px) because it has a sidebar and benefits from the room; the chapter reader stays narrow by default for prose readability, with an optional per-viewer **Wide** toggle (`main.reader.reader-wide` → 900px, text still capped at 720px so lines don't over-stretch). Both preferences persist via `localStorage`, along with reading position per story and the Codex's last-opened doc.

**No build step, no dependencies to install** — the only external loads are three Google Fonts and `marked.js` from cdnjs, both via plain `<link>`/`<script src>` tags. Editing is just editing `index.html` (or the `codex/*.md` files) directly.

---

## Keeping the Codex in Sync

`codex/*.md` are **copies**, not the source of truth — they're regenerated from the actual "The Ura" project files by `scripts/sync_codex.py`. Whenever the World Bible, Craft Rulebook, or any Arc 1 planning doc changes:

```bash
cd story-shelf
python3 scripts/sync_codex.py
git add codex/ && git commit -m "Re-sync Codex" && git push
```

The script also wraps the World Bible's ASCII-art tables (`+----+----+` style) in fenced code blocks so `marked.js` renders them as clean monospace instead of mangling them as prose — that's the main reason to run the script rather than just `cp`-ing files over.

**Deliberately excluded from the Codex:** `Bible/handoff.md` and `AI_CONTEXT.md` — both are pre-reorg originals, explicitly superseded by the current Bible/Story files per the main project's own `SESSION_HANDOFF.md`. Don't add them without checking that's actually changed.

---

## Before You Push

There's no CI here, so do this by hand — it's caught real syntax errors twice:

```bash
cd story-shelf
python3 -c "
import re
text = open('index.html').read()
m = re.search(r'<script>\n\(function.*?\n</script>', text, re.S)
open('/tmp/check.js','w').write(m.group(0).replace('<script>','').replace('</script>',''))
"
node --check /tmp/check.js && echo OK
```

Then commit, push, and give GitHub Pages ~15–20 seconds before checking the live URL — first deploys and cache invalidation aren't instant.

---

## Known Gaps / Next Things

- Chapters 1–19 are on the site. Check `Story/Arc_01_Yamashiro/` for newer drafts before assuming the shelf is current.
- No mechanism yet for a second story on the shelf — the `STORIES` object and `renderHome()`'s card markup are both written for exactly one story right now. Generalizing to a `STORIES` map with N entries and a `.forEach` in `renderHome()` is straightforward whenever it's actually needed; not done preemptively.
- `codex/*.md` can silently go stale if `scripts/sync_codex.py` isn't re-run after a Bible/Craft edit — there's no automation (e.g. a git hook or CI job) enforcing the sync. Worth adding if this becomes a recurring point of friction.
