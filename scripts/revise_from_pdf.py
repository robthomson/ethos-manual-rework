#!/usr/bin/env python3
"""
Revise an existing AI translation against a real human-translated PDF
manual, using Claude's native PDF vision (not text extraction).

Why not text extraction: FrSky's exported manual PDFs (at least DE/IT/ES)
have a broken font ToUnicode mapping -- every accented character
extracts as U+FFFD via pypdf *and* pdfplumber. Claude's native PDF
handling reads the rendered page visually and is unaffected (verified:
"koennen" -> "können" transcribed correctly). The tradeoff is the whole
PDF doesn't fit any model's context window (a 477-page manual is ~1.01M
tokens, over even Opus 5's 1M ceiling) -- so this works page-range by
page-range instead of whole-document.

Two phases:
  1. `--map` -- one cheap, text-only call per language: feed Claude the
     PDF's bookmark outline (page numbers are reliable even though titles
     are partially garbled by the same encoding bug) plus our page list,
     get back an approximate [start, end] page range per page. Thinking
     disabled -- this is mechanical, not a reasoning task, and adaptive
     thinking was burning the entire output budget on a task this small.
  2. `--revise` -- per page: extract that page range to a temp PDF,
     upload via the Files API, and ask Claude to locate the relevant
     content within the range and revise our current AI translation
     against it (same system prompt shape as revise_from_reference.py).

This is a LOCAL, standalone tool -- not part of the site build or CI.
Never commits or pushes; only writes docs/<locale>/<path>.

Usage:
    python scripts/revise_from_pdf.py --locale de --pdf "../ethos-manual/german/docs/[DE] Ethos User Manual 1.6.3.pdf" --map
    python scripts/revise_from_pdf.py --locale de --dry-run
    python scripts/revise_from_pdf.py --locale de --yes
    python scripts/revise_from_pdf.py --locale de --pages model-setup/mixes.md --yes
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

try:
    import pypdf
except ImportError:
    print("ERROR: pypdf not installed. Run: pip install pypdf")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
EN_DIR = DOCS_DIR / "en"
SCRATCH_DIR = REPO_ROOT / ".pdf_revision_cache"  # gitignored; range maps + temp extracts
DEFAULT_MODEL = "claude-opus-5"

LOCALE_NAMES = {"de": "German", "it": "Italian", "es": "Spanish"}

NO_TRANSLATE_TERMS = (
    "ENT", "RTN", "PAGE", "MDL", "TELE", "DISP", "SYS",
    "FrSky", "Ethos", "Rotorflight", "Rotorflight LUA", "Ethos Suite",
    "X20S", "X20", "X20 PRO", "X20 PRO AW", "X18S", "X18", "X-Lite",
    "Horus", "Taranis",
    "ACCESS", "ACCST", "S.Port", "F.Port", "F.BUS", "SBUS", "CRSF",
    "ELRS", "ExpressLRS", "Multi-protocol", "MSP",
    "SD card", "USB", "Wi-Fi", "Bluetooth", "MicroSD",
    "Lua",
)

SYSTEM_PROMPT_TEMPLATE = """You are revising an existing machine-translated {locale_name} page for the Ethos radio manual using a REAL, human-written {locale_name} reference manual (an excerpt from FrSky's own official {locale_name} PDF manual) as a quality/terminology guide.

You are given a PDF excerpt (a page range from the full manual) that MAY OR MAY NOT contain the relevant section -- the range was estimated from a bookmark outline, not guaranteed exact. First locate the content matching the current English source's topic within the excerpt. If the excerpt genuinely does not cover this topic, say so and revise only for natural fluency without inventing content from the reference.

1. Read the CURRENT ENGLISH SOURCE first -- it defines what must be covered and is authoritative for accuracy/completeness.
2. Read the CURRENT {locale_name} AI TRANSLATION -- this is what you're revising.
3. Find the matching section in the PDF excerpt (if present) -- adopt its terminology, phrasing, idiom, and natural {locale_name} style wherever it covers the same content as the current English source.
4. Produce a revised {locale_name} translation that:
   - Fully and accurately covers everything in the current English source.
   - Uses the PDF reference's actual wording/terminology wherever topics overlap, instead of the AI translation's original wording, when the human phrasing is natural and still accurate.
   - Falls back to revising the AI translation's own wording (improving naturalness where you can) for anything the reference doesn't cover, or if the excerpt doesn't contain the relevant section at all.

Hard rules -- do not violate these:

1. Output ONLY the revised Markdown body. No commentary, no preamble, no code fence wrapping the whole output.
2. Preserve the Markdown structure exactly: identical headings (same levels, same order, same count as the CURRENT ENGLISH SOURCE), identical list/table structure, identical paragraph breaks.
3. NEVER translate or alter, copy verbatim character-for-character:
   - Anchor IDs in attr_list syntax, e.g. `{{: #choosing-a-source }}` at the end of a heading.
   - URLs and relative file paths inside links and images.
   - Anchor fragments in links, e.g. `#choosing-a-source`.
   - Content inside fenced code blocks (``` ... ```).
   - These technical terms, brand names, and protocol names -- keep them exactly as written: {no_translate_terms}.
4. DO translate/revise: headings, paragraph text, list item text, table cell text, image alt text, admonition title text.
"""


def load_page_list() -> list[tuple[str, str]]:
    """[(rel_path, english_title), ...] -- excludes contributor-only docs,
    which have no equivalent in any official FrSky manual PDF."""
    pages = []
    for p in sorted(EN_DIR.rglob("*.md")):
        rel = p.relative_to(EN_DIR).as_posix()
        if p.name == "translation-status.md" or "contributing" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        pages.append((rel, m.group(1).strip() if m else rel))
    return pages


def extract_outline(pdf_path: Path) -> str:
    reader = pypdf.PdfReader(str(pdf_path))
    entries: list[tuple[int, str]] = []

    def walk(items):
        for it in items:
            if isinstance(it, list):
                walk(it)
                continue
            try:
                pn = reader.get_destination_page_number(it)
            except Exception:
                continue
            if pn is not None and it.title and it.title.strip():
                entries.append((pn + 1, it.title.strip()))  # 1-indexed

    walk(reader.outline)
    entries.sort()
    return "\n".join(f"{pn}: {title}" for pn, title in entries)


def build_range_map(client: anthropic.Anthropic, model: str, locale: str, pdf_path: Path) -> dict[str, list[int]]:
    outline = extract_outline(pdf_path)
    pages = load_page_list()
    page_list_text = "\n".join(f"{rel}\t{title}" for rel, title in pages)
    locale_name = LOCALE_NAMES[locale]

    prompt = f"""This is the bookmark outline (page numbers + titles, in {locale_name}, some titles possibly garbled by a PDF encoding issue but page numbers are reliable) from a large {locale_name} Ethos radio manual PDF:

{outline}

I have target topics from an English manual with the same overall structure. For each one below (format: relative_path<TAB>English title), estimate the page range in the {locale_name} PDF (1-indexed) that most likely covers that topic, based on the outline and typical manual ordering. Use a generous window (prefer to over-include neighboring pages rather than miss content) but keep each range under 30 pages. If you have no reasonable basis to guess a topic's location, omit it from the output rather than guessing wildly.

Topics:
{page_list_text}

Respond with ONLY a JSON object mapping relative_path to [start_page, end_page] (1-indexed, inclusive). Be terse -- no commentary, no markdown fence, no extra whitespace."""

    with client.messages.stream(
        model=model,
        max_tokens=16000,
        thinking={"type": "disabled"},
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        resp = stream.get_final_message()
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-z]*\n?|```$", "", text).strip()
    return json.loads(text)


def extract_page_range(pdf_path: Path, start: int, end: int, total_pages: int, out_path: Path) -> None:
    reader = pypdf.PdfReader(str(pdf_path))
    writer = pypdf.PdfWriter()
    start_idx = max(0, start - 1)
    end_idx = min(total_pages, end)
    for i in range(start_idx, end_idx):
        writer.add_page(reader.pages[i])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "wb") as f:
        writer.write(f)


def _clean_output(text: str) -> str:
    text = text.strip()
    lines = text.split("\n")
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text + "\n"


def strip_leading_frontmatter(text: str) -> str:
    """Remove a leading ---...--- block, if the model echoed one despite
    being told to output only the Markdown body."""
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        return text
    end = stripped.find("\n---", 3)
    if end == -1:
        return text
    return stripped[end + 4:].lstrip("\n")


def revise_page(client: anthropic.Anthropic, model: str, locale: str,
                 en_text: str, current_translation: str, file_id: str) -> str:
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        locale_name=LOCALE_NAMES[locale],
        no_translate_terms=", ".join(NO_TRANSLATE_TERMS),
    )
    user_content = [
        {"type": "document", "source": {"type": "file", "file_id": file_id}},
        {"type": "text", "text": (
            "=== CURRENT ENGLISH SOURCE ===\n"
            f"{en_text}\n\n"
            "=== CURRENT AI TRANSLATION (to revise) ===\n"
            f"{current_translation}\n"
        )},
    ]
    resp = client.beta.messages.create(
        model=model,
        max_tokens=16000,
        betas=["files-api-2025-04-14"],
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    text = "".join(block.text for block in resp.content if block.type == "text")
    return _clean_output(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Revise AI translations against a real PDF manual (vision-based)")
    ap.add_argument("--locale", required=True, choices=sorted(LOCALE_NAMES))
    ap.add_argument("--pdf", help="Path to the source PDF (required for --map)")
    ap.add_argument("--map", action="store_true", help="(Re)build the page-range map and exit")
    ap.add_argument("--pages", nargs="*", metavar="PATH")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args(argv)

    SCRATCH_DIR.mkdir(exist_ok=True)
    range_map_path = SCRATCH_DIR / f"{args.locale}_ranges.json"

    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    if args.map:
        if not args.pdf:
            raise SystemExit("--map requires --pdf <path>")
        pdf_path = Path(args.pdf)
        if not pdf_path.exists():
            raise SystemExit(f"PDF not found: {pdf_path}")
        print(f"Building page-range map for {args.locale} from {pdf_path.name}...")
        range_map = build_range_map(client, args.model, args.locale, pdf_path)
        range_map_path.write_text(json.dumps(range_map, indent=2), encoding="utf-8")
        print(f"Mapped {len(range_map)} pages -> {range_map_path}")
        return 0

    if not range_map_path.exists():
        raise SystemExit(f"No range map for {args.locale} yet -- run with --map --pdf <path> first")
    range_map: dict[str, list[int]] = json.loads(range_map_path.read_text(encoding="utf-8"))

    if not args.pdf:
        raise SystemExit("--pdf <path> is required (page extraction needs the source file)")
    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")
    reader = pypdf.PdfReader(str(pdf_path))
    total_pages = len(reader.pages)

    pages = args.pages if args.pages else sorted(range_map)
    unknown = [p for p in pages if p not in range_map]
    if unknown:
        print(f"WARNING: no mapped range for (skipping): {', '.join(unknown)}")
        pages = [p for p in pages if p in range_map]

    print(f"Revising {len(pages)} {args.locale} page(s) against {pdf_path.name} (model: {args.model})\n")
    for p in pages:
        s, e = range_map[p]
        print(f"  {p}  <-  pages {s}-{e}")

    if args.dry_run:
        print("\nDry run -- no API calls made, no files written.")
        return 0

    if not args.yes:
        answer = input(f"\nRevise {len(pages)} page(s) with {args.model}? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted.")
            return 0

    revised = 0
    failed: list[str] = []
    for i, rel_path in enumerate(pages, 1):
        print(f"[{i}/{len(pages)}] {args.locale}/{rel_path}...", end=" ", flush=True)
        en_path = EN_DIR / rel_path
        fr_path = DOCS_DIR / args.locale / rel_path
        if not en_path.exists() or not fr_path.exists():
            print("SKIP (missing en or current translation)")
            continue

        start, end = range_map[rel_path]
        extract_path = SCRATCH_DIR / args.locale / f"{rel_path.replace('/', '_')}.pdf"
        try:
            extract_page_range(pdf_path, start, end, total_pages, extract_path)
            uploaded = client.beta.files.upload(file=(extract_path.name, open(extract_path, "rb"), "application/pdf"))
            en_text = en_path.read_text(encoding="utf-8")
            current_translation = fr_path.read_text(encoding="utf-8")
            revised_text = revise_page(client, args.model, args.locale, en_text, current_translation, uploaded.id)
        except anthropic.APIError as exc:
            print(f"FAILED: {exc}")
            failed.append(rel_path)
            time.sleep(2)
            continue
        except Exception as exc:
            print(f"FAILED: {exc}")
            failed.append(rel_path)
            continue

        existing = current_translation
        if existing.startswith("---"):
            end_fm = existing.find("\n---", 3)
            frontmatter = existing[: end_fm + 4] if end_fm != -1 else ""
        else:
            frontmatter = ""
        # Claude's output sometimes echoes a frontmatter-like block despite
        # being told to output only the Markdown body (it saw one in the
        # "current translation" it was revising) -- strip any leading
        # ---...--- block from its output before prepending our own, or
        # the file ends up with the same translated_from block twice.
        revised_text = strip_leading_frontmatter(revised_text)
        fr_path.write_text(f"{frontmatter}\n\n{revised_text}" if frontmatter else revised_text, encoding="utf-8")
        print("done")
        revised += 1

    print(f"\nDone: {revised} revised, {len(failed)} failed.")
    if failed:
        print("Failed pages (re-run to retry):")
        for f in failed:
            print(f"  {f}")
    print("\nNothing was committed. Review the diff (`git diff docs/`), then commit/PR as usual.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
