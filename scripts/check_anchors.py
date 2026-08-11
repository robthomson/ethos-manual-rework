#!/usr/bin/env python3
"""
Check (and optionally fix) cross-page/same-page anchor links broken by
translation.

When a heading's translated text differs from English, MkDocs' default
auto-slug changes with it -- silently breaking any `#that-heading-slug`
link from another page that still points at the old (English) slug,
since translated content copies link *fragments* verbatim per the
translation system prompt (see docs/en/contributing/index.md). This
script finds every such break across every locale by diffing the built
site's real anchor IDs against every internal link's target fragment,
and (with --fix) pins the affected heading to a stable ID -- using its
current English auto-slug -- with `attr_list`, in English and in every
locale that has that page translated, so the ID never depends on
translated text again.

This is a repo-maintenance tool, not part of the site build. Run it
after any batch of new/updated translations (a fresh
scripts/translate.py run, or a manual edit) -- it's the only reliable
way to catch this class of bug; a broken anchor is not a build error
(mkdocs build --strict does not fail on it) and won't otherwise surface
except as a dead link a reader clicks.

Usage:
    python scripts/check_anchors.py            # report only, exit 1 if any found
    python scripts/check_anchors.py --fix       # report AND pin every finding
    python scripts/check_anchors.py --no-build  # skip the `mkdocs build` step
                                                  # (use an already-fresh site/)
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
SITE_DIR = REPO_ROOT / "site"
EN_DIR = DOCS_DIR / "en"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
ATTR_LIST_RE = re.compile(r"\s*\{:\s*#([\w-]+)\s*\}\s*$")
HTML_HEADING_RE = re.compile(r'<h([1-6])[^>]*\sid="([^"]+)"')
LINK_RE = re.compile(r'href="([^"]+)"')
HTML_ID_RE = re.compile(r'id="([^"]+)"')

NON_LOCALE_DIRS = {"assets", "stylesheets"}


def locales() -> list[str]:
    return sorted(
        p.name for p in DOCS_DIR.iterdir()
        if p.is_dir() and p.name != "en" and p.name not in NON_LOCALE_DIRS
    )


def en_md_to_html_rel(md_rel: str) -> str:
    p = Path(md_rel)
    html_dir = p.parent if p.name == "index.md" else p.with_suffix("")
    return (html_dir / "index.html").as_posix().removeprefix("./")


def extract_html_heading_ids(html: str) -> list[tuple[int, str]]:
    return [(int(lvl), hid) for lvl, hid in HTML_HEADING_RE.findall(html)]


def pin_heading_in_file(md_path: Path, ordinal: int, expected_level: int, pin_id: str) -> bool:
    """Add `{: #pin_id }` to the ordinal-th heading in md_path. Returns True on
    success or if it's already correctly pinned; False (with a printed
    reason) if it can't be applied safely."""
    text = md_path.read_text(encoding="utf-8")
    lines = text.split("\n")
    in_fence = False
    idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        idx += 1
        if idx != ordinal:
            continue
        level = len(m.group(1))
        if level != expected_level:
            print(f"    LEVEL MISMATCH in {md_path.relative_to(REPO_ROOT)}: "
                  f"expected h{expected_level}, found h{level} at ordinal {ordinal}")
            return False
        rest = m.group(2)
        pin_m = ATTR_LIST_RE.search(rest)
        if pin_m:
            if pin_m.group(1) == pin_id:
                return True  # already correctly pinned
            print(f"    WARNING: {md_path.relative_to(REPO_ROOT)} heading already "
                  f"pinned to #{pin_m.group(1)}, wanted #{pin_id} -- leaving as-is")
            return False
        lines[i] = f"{'#' * level} {rest} {{: #{pin_id} }}"
        md_path.write_text("\n".join(lines), encoding="utf-8")
        return True
    print(f"    ERROR: ordinal {ordinal} not found in {md_path.relative_to(REPO_ROOT)}")
    return False


def find_broken_links(pages: dict[str, str]) -> list[tuple[str, str, str]]:
    """Return [(source_html_rel, target_html_rel, fragment), ...] for every
    locale-prefixed page (i.e. skip the default-locale/English tree, which
    is the source of truth and can't itself be "broken" by translation)."""
    locale_prefixes = tuple(f"{loc}/" for loc in locales())
    problems = []
    for rel, html in pages.items():
        if not rel.startswith(locale_prefixes):
            continue
        base_dir = (SITE_DIR / rel).parent
        for href in LINK_RE.findall(html):
            if not href or href.startswith(("http://", "https://", "mailto:", "javascript:", "tel:")):
                continue
            if "#" not in href:
                continue
            path_part, frag = href.split("#", 1)
            if not frag:
                continue
            target_dir = (base_dir / path_part).resolve() if path_part else base_dir
            try:
                target_dir.relative_to(SITE_DIR.resolve())
            except ValueError:
                continue
            target_html = target_dir / "index.html"
            if not target_html.exists():
                continue
            target_key = target_html.resolve().relative_to(SITE_DIR.resolve()).as_posix()
            if target_key not in pages:
                continue
            ids = set(HTML_ID_RE.findall(pages[target_key]))
            if frag not in ids:
                problems.append((rel, target_key, frag))
    return problems


def resolve_rel_md(target_html: str, loc: str) -> str | None:
    target_dir = target_html[len(f"{loc}/"):]
    target_dir = target_dir[: -len("index.html")].rstrip("/")
    candidates = [target_dir + ".md"] if target_dir else []
    candidates.append((target_dir + "/index.md") if target_dir else "index.md")
    return next((c for c in candidates if (EN_DIR / c).exists()), None)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true", help="Pin every finding with attr_list (en + every locale that has the page)")
    ap.add_argument("--no-build", action="store_true", help="Skip running `mkdocs build` first; use the existing site/ as-is")
    args = ap.parse_args()

    if not args.no_build:
        print("Building site (mkdocs build --strict)...")
        result = subprocess.run(["mkdocs", "build", "--strict"], cwd=REPO_ROOT, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            print("ERROR: mkdocs build failed -- fix that before checking anchors.")
            return 1

    pages = {}
    for html in SITE_DIR.rglob("*.html"):
        pages[html.relative_to(SITE_DIR).as_posix()] = html.read_text(encoding="utf-8")

    problems = find_broken_links(pages)
    unique = sorted(set((t, f) for _s, t, f in problems))
    print(f"\n{len(problems)} broken link occurrence(s), {len(unique)} unique (target, fragment) pair(s)\n")

    if not unique:
        print("Nothing to fix.")
        return 0

    locs = locales()
    for target_html, frag in unique:
        loc = next((l for l in locs if target_html.startswith(f"{l}/")), None)
        if loc is None:
            print(f"SKIP: {target_html} doesn't match any locale prefix {locs}")
            continue
        rel_md = resolve_rel_md(target_html, loc)
        if rel_md is None:
            print(f"SKIP: can't resolve {target_html} to a docs/en source file")
            continue

        en_html_path = SITE_DIR / en_md_to_html_rel(rel_md)
        if not en_html_path.exists():
            print(f"SKIP: no built EN html for {rel_md} (expected {en_html_path})")
            continue
        en_ids = extract_html_heading_ids(en_html_path.read_text(encoding="utf-8"))

        match = next(((i, lvl) for i, (lvl, hid) in enumerate(en_ids) if hid == frag), None)
        if match is None:
            print(f"SKIP: fragment #{frag} not found among EN heading ids in {rel_md}")
            continue
        ordinal, level = match

        print(f"{rel_md} : ordinal {ordinal} (h{level}) -> #{frag}")
        if not args.fix:
            continue
        ok_en = pin_heading_in_file(EN_DIR / rel_md, ordinal, level, frag)
        print(f"    en: {'ok' if ok_en else 'FAILED'}", end="")
        for other_loc in locs:
            other_md_path = DOCS_DIR / other_loc / rel_md
            if not other_md_path.exists():
                continue
            ok = pin_heading_in_file(other_md_path, ordinal, level, frag)
            print(f"  {other_loc}: {'ok' if ok else 'FAILED'}", end="")
        print()

    if not args.fix:
        print("\nRe-run with --fix to pin these, or fix manually per "
              "docs/en/contributing/index.md#addingupdating-a-translation.")
    else:
        print("\nDone. Re-run without --fix (or just this script again) to confirm 0 remain.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
