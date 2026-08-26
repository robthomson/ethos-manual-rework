"""Renders one combined PDF manual per fully-covered locale (plus English).

Deliberately doesn't run as an mkdocs plugin/hook. mkdocs-static-i18n builds
each locale through its own nested, complete build pass within a single
`mkdocs build` (see hooks/split_search_index.py's docstring for the details
this caused there) -- a PDF-export plugin hooking the normal page/build
events would see that same partial, single-locale state on every call, and
neither of the two established mkdocs PDF plugins (mkdocs-with-pdf,
mkdocs-exporter) has real support for it (mkdocs-with-pdf has a years-old
open issue and an abandoned PR attempting exactly this).

Instead, this is a standalone script that crawls an *already-built* site
over HTTP with headless Chromium (Playwright) -- same mechanism as visiting
the real site in a browser and printing to PDF, just automated and merged
into one file per locale. That sidesteps the nested-build problem entirely:
by the time this runs, mkdocs-static-i18n and the search/i18n plugins are
long done, and there's nothing left to get confused by. Material's own
`@media print` styles already hide the header/sidebar/nav chrome cleanly, so
no custom print stylesheet is needed.

Writes plain files (ethos-manual-<version>-<locale>.pdf) to a local
directory -- deploy.yml uploads them as GitHub Release assets rather than
committing them into the gh-pages branch. At ~15-20MB apiece across a
growing number of locales, regenerating and re-committing them on every
push would permanently bloat that branch's git history a little more on
every single deploy, forever; a release's assets just get replaced in
place. The site's header links to that release list directly (see
overrides/partials/header.html) rather than a specific file, so which
locale/version to grab is a choice made on GitHub's release page, not
something this script's output layout needs to support.

Usage (see .github/workflows/deploy.yml for how CI wires this in):
    python -m playwright install --with-deps chromium
    python scripts/build_pdfs.py --base-url http://localhost:8000 --out-dir pdf-dist --version 1.6
"""

from __future__ import annotations

import argparse
import asyncio
import io
import math
import re
import sys
from datetime import date
from html import escape
from pathlib import Path

import material
import yaml
from playwright.async_api import Browser, async_playwright
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from reportlab.pdfgen import canvas as reportlab_canvas

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "hooks"))
from _locales import fully_covered_locales  # noqa: E402

CONCURRENCY = 6

# mkdocs-material's own bundled UI-string translations -- reused below so
# the PDF's table-of-contents heading says "Table of contents" in whatever
# language matches that locale's actual sidebar TOC, without re-guessing a
# translation here.
MATERIAL_LANG_DIR = Path(material.__file__).resolve().parent / "templates" / "partials" / "languages"

# --- Shared layout constants for the cover/TOC/footer, chosen to match the
# *real* content pages so they don't look like a bolted-on extra document:
#
# - Font: mkdocs-material's default theme.font (unset here -> "Roboto",
#   loaded from Google Fonts, see material/templates/base.html's `fonts`
#   block) with its own fallback stack appended.
# - Margin: measured directly off a rendered content page (a plain
#   render_pdf() of the home page, text bbox via pypdf) -- 82-87pt
#   left/right. That's noticeably more than Material's own declared
#   `@page{margin:25mm}` (~71pt) because Playwright's render_pdf() doesn't
#   pass preferCSSPageSize, so that rule is never actually applied; the
#   visible inset is entirely `.md-content`'s own internal padding. Matching
#   the *measured* number (not the unused CSS rule) is what makes the TOC's
#   margins actually look consistent with real pages.
#
# All A4/page-geometry math below is in PDF points (1pt = 1/72in, and CSS
# "pt" is defined as the same 1/72in -- using pt for every TOC/footer
# dimension means the CSS layout and this file's own page-position math for
# hyperlink/footer placement agree exactly, no px<->pt conversion needed.
FONT_STACK = '"Roboto", -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif'
GOOGLE_FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css?'
    'family=Roboto:300,300i,400,400i,700,700i&display=fallback">'
)
PAGE_WIDTH_PT = 595.28  # A4
PAGE_HEIGHT_PT = 841.89
MARGIN_PT = 83.0
ROW_HEIGHT_PT = 16.0
HEADING_BLOCK_PT = 46.0
FOOTER_Y_PT = 40.0  # baseline height from the bottom edge, within the margin band


def pdf_filename(version: str, locale: str) -> str:
    return f"ethos-manual-{version}-{locale}.pdf"


COVER_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
{google_font_link}
<style>
  body {{
    margin: 0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    font-family: {font_stack};
    background: #1a1a1a;
    color: #fff;
    text-align: center;
  }}
  img {{ width: 220px; }}
  h1 {{ font-size: 2.5rem; font-weight: 300; margin: 0; }}
  p {{ font-size: 1.1rem; color: #b0b0b0; margin: 0; }}
</style>
</head>
<body>
  <img src="{logo_url}" alt="">
  <h1>Ethos Manual</h1>
  <p>{subtitle}</p>
  <p>Version {version} &middot; Generated {generated}</p>
</body>
</html>
""".replace("{google_font_link}", GOOGLE_FONT_LINK).replace("{font_stack}", FONT_STACK)

# One physical page per render -- see paginate_toc()/render_toc_page_html().
# Every dimension is in pt so this file's own row/page-position math (used
# for footer stamping and the per-row hyperlink rects) lines up exactly with
# what's on screen, with no unit conversion to get wrong.
TOC_PAGE_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
{google_font_link}
<style>
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    width: {page_width}pt;
    height: {page_height}pt;
    padding: {margin}pt;
    font-family: {font_stack};
    color: #1a1a1a;
  }}
  h1 {{
    font-size: 18pt;
    font-weight: 300;
    height: {heading_block}pt;
    margin: 0;
    display: flex;
    align-items: flex-end;
  }}
  .row {{
    height: {row_height}pt;
    display: flex;
    align-items: center;
    overflow: hidden;
  }}
  .row.section {{ font-weight: 600; font-size: 10.5pt; }}
  .row.page {{ margin-left: 14pt; font-weight: 400; font-size: 9.5pt; }}
  .title {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .leader {{ flex: 1 1 auto; min-width: 8pt; border-bottom: 1px dotted #999; margin: 0 4pt 3pt; }}
  .page-number {{ white-space: nowrap; color: #555; font-size: 9pt; }}
</style>
</head>
<body>
  {heading_html}
  {rows}
</body>
</html>
""".replace("{google_font_link}", GOOGLE_FONT_LINK).replace("{font_stack}", FONT_STACK).replace(
    "{page_width}", str(PAGE_WIDTH_PT)
).replace("{page_height}", str(PAGE_HEIGHT_PT)).replace("{margin}", str(MARGIN_PT)).replace(
    "{heading_block}", str(HEADING_BLOCK_PT)
).replace("{row_height}", str(ROW_HEIGHT_PT))

TOC_ROW = (
    '<div class="row {css_class}">'
    '<span class="title">{title}</span><span class="leader"></span>'
    '<span class="page-number">{page}</span></div>'
)


def load_mkdocs_config(mkdocs_yml: Path) -> dict:
    return yaml.safe_load(mkdocs_yml.read_text(encoding="utf-8"))


# Matches one literate-nav bullet line: leading whitespace (indent, always a
# multiple of 4 spaces in this repo's SUMMARY.md), a "*"/"-" marker, then a
# markdown link. Non-matching lines (blank lines, the file's own leading
# HTML-comment docstring) are simply skipped, not errors -- SUMMARY.md is
# free-form markdown around the bullet list, not a strict grammar.
_BULLET_RE = re.compile(r"^(?P<indent>\s*)[*-]\s+\[(?P<title>[^\]]+)\]\((?P<path>[^)]+)\)\s*$")


def nav_sections(config: dict, docs_root: Path) -> list[dict]:
    """Top-level nav entries (from docs_root/en/SUMMARY.md), preserving
    titles and grouping -- used to build the PDF's table of contents
    (nav_pages() below only needed the flat path list, and threw titles
    away).

    Each entry is {"title": str, "pages": [(title, md_path), ...]}. A
    top-level bullet with no indented children under it is a single-page
    section (e.g. "Home") -- pages has exactly one entry. A top-level
    bullet *with* indented children (e.g. "Getting Started") is a group:
    pages[0] is the section's own (title, landing_page) -- matching how
    every section in this site is actually laid out, its own link doubling
    as both the section title and its landing page -- followed by each
    child bullet's own (title, path).

    `config` isn't actually read here any more (structure now comes purely
    from SUMMARY.md) -- kept as the first parameter anyway so every
    function in this module still takes `config` first, matching
    nav_translations_for()/locale_names() below, which do need it.
    """
    summary = docs_root / "en" / "SUMMARY.md"
    lines = summary.read_text(encoding="utf-8").splitlines()

    sections: list[dict] = []
    for line in lines:
        m = _BULLET_RE.match(line)
        if not m:
            continue
        title, path = m["title"], m["path"]
        # Indent 0 starts a new section; anything indented is a child of
        # whichever section was most recently started.
        if len(m["indent"]) == 0:
            sections.append({"title": title, "pages": [(title, path)]})
        elif sections:
            sections[-1]["pages"].append((title, path))
    return sections


def nav_pages(config: dict, docs_root: Path) -> list[str]:
    """Ordered list of docs_dir-relative .md paths, flattened from nav_sections()."""
    return [path for section in nav_sections(config, docs_root) for _, path in section["pages"]]


def nav_translations_for(config: dict, locale: str) -> dict[str, str]:
    """English title -> translated title, from that locale's i18n plugin config."""
    for plugin in config["plugins"]:
        if isinstance(plugin, dict) and "i18n" in plugin:
            for language in plugin["i18n"]["languages"]:
                if language["locale"] == locale:
                    return language.get("nav_translations", {})
    return {}


def localize_sections(sections: list[dict], translations: dict[str, str]) -> list[dict]:
    """Swap each section/page title for its nav_translations entry, where one exists."""
    return [
        {
            "title": translations.get(section["title"], section["title"]),
            "pages": [(translations.get(t, t), p) for t, p in section["pages"]],
        }
        for section in sections
    ]


def toc_label(locale: str) -> str:
    """"Table of contents" in this locale (see MATERIAL_LANG_DIR above)."""
    path = MATERIAL_LANG_DIR / f"{locale}.html"
    if not path.exists():
        path = MATERIAL_LANG_DIR / "en.html"
    match = re.search(r'"toc":\s*"([^"]*)"', path.read_text(encoding="utf-8"))
    return match.group(1) if match else "Table of contents"


def paginate_toc(sections: list[dict]) -> list[list[dict]]:
    """Flatten sections into {"title", "path", "css_class"} rows and split
    them across fixed-height TOC pages, entirely by row *count* -- no
    rendering needed to know this, since every row and the heading block
    have a fixed CSS height (see TOC_PAGE_HTML). Deciding this up front
    (rather than rendering and measuring) is what makes both the page
    numbers content pages get shifted by, and the hyperlink rect for every
    row, computable as plain arithmetic below instead of guess-and-check.
    """
    rows: list[dict] = []
    for section in sections:
        first_title, first_path = section["pages"][0]
        rows.append({"title": first_title, "path": first_path, "css_class": "section"})
        for title, path in section["pages"][1:]:
            rows.append({"title": title, "path": path, "css_class": "page"})

    usable_height = PAGE_HEIGHT_PT - 2 * MARGIN_PT
    capacity_first = math.floor((usable_height - HEADING_BLOCK_PT) / ROW_HEIGHT_PT)
    capacity_rest = math.floor(usable_height / ROW_HEIGHT_PT)

    toc_pages: list[list[dict]] = []
    i = 0
    while i < len(rows):
        capacity = capacity_first if not toc_pages else capacity_rest
        toc_pages.append(rows[i : i + capacity])
        i += capacity
    return toc_pages or [[]]


def render_toc_page_html(
    rows: list[dict], page_numbers: dict[str, int], heading: str, is_first_page: bool
) -> str:
    row_html = "\n  ".join(
        TOC_ROW.format(
            css_class=row["css_class"], title=escape(row["title"]), page=page_numbers[row["path"]]
        )
        for row in rows
    )
    heading_html = f"<h1>{escape(heading)}</h1>" if is_first_page else ""
    return TOC_PAGE_HTML.format(heading_html=heading_html, rows=row_html)


def toc_row_rect(
    local_index: int, is_first_page: bool, page_width: float, page_height: float
) -> tuple[float, float, float, float]:
    """The clickable (x0, y0, x1, y1) rect, in PDF space (origin bottom-left),
    for the row at `local_index` within its own TOC page -- the same fixed
    top-offset arithmetic TOC_PAGE_HTML's CSS heights produce, just computed
    here instead of measured, against that specific page's *actual* rendered
    size (so a fraction-of-a-point difference between our A4 constants and
    whatever Chromium actually emitted for format="A4" can't misalign it).
    """
    top = MARGIN_PT + (HEADING_BLOCK_PT if is_first_page else 0) + local_index * ROW_HEIGHT_PT
    bottom = top + ROW_HEIGHT_PT
    return (MARGIN_PT, page_height - bottom, page_width - MARGIN_PT, page_height - top)


def make_footer_overlay(width_pt: float, height_pt: float, page_number: int, label: str):
    """A one-page PDF containing just the running footer, to be merged onto
    a real page. Uses a built-in PDF standard font (Helvetica) rather than
    Roboto -- reportlab can't use the Google-Fonts-loaded Roboto a browser
    render pulled in, and embedding a Roboto .ttf just for an 8pt footer
    isn't worth the extra asset; Helvetica reads close enough at this size.
    """
    buf = io.BytesIO()
    c = reportlab_canvas.Canvas(buf, pagesize=(width_pt, height_pt))
    c.setFont("Helvetica", 8)
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.drawString(MARGIN_PT, FOOTER_Y_PT, label)
    c.drawRightString(width_pt - MARGIN_PT, FOOTER_Y_PT, str(page_number))
    c.showPage()
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def locale_names(config: dict) -> dict[str, str]:
    """locale -> display name (e.g. "fr" -> "Français"), from the i18n plugin config."""
    names = {}
    for plugin in config["plugins"]:
        if isinstance(plugin, dict) and "i18n" in plugin:
            for language in plugin["i18n"]["languages"]:
                names[language["locale"]] = language["name"]
    return names


def page_url(md_path: str) -> str:
    """docs_dir-relative .md path -> mkdocs "pretty" URL path (no leading/trailing slash)."""
    if md_path == "index.md":
        return ""
    if md_path.endswith("/index.md"):
        return md_path[: -len("index.md")]
    return md_path[:-3] + "/"


async def render_pdf(browser: Browser, url: str) -> bytes:
    page = await browser.new_page()
    try:
        await page.goto(url, wait_until="networkidle")
        await page.emulate_media(media="print")
        return await page.pdf(format="A4", print_background=True)
    finally:
        await page.close()


async def render_static_pdf(browser: Browser, html: str) -> bytes:
    """Same as render_pdf(), but for a standalone HTML string with no URL to
    navigate to (the cover and table-of-contents pages)."""
    page = await browser.new_page()
    try:
        await page.set_content(html, wait_until="networkidle")
        return await page.pdf(format="A4", print_background=True)
    finally:
        await page.close()


async def build_locale_pdf(
    browser: Browser,
    base_url: str,
    locale: str,
    display_name: str,
    sections: list[dict],
    out_path: Path,
    version: str,
    generated: str,
) -> None:
    prefix = "" if locale == "en" else f"{locale}/"
    # -reversed is the light-on-transparent variant; the plain logo is dark
    # text and was unreadable against this cover's dark background.
    logo_url = f"{base_url}/assets/ethos-logo-reversed.png"
    cover_html = COVER_HTML.format(
        logo_url=logo_url, subtitle=display_name, version=version, generated=generated
    )
    cover_bytes = await render_static_pdf(browser, cover_html)
    cover_page_count = len(PdfReader(io.BytesIO(cover_bytes)).pages)

    pages = [path for section in sections for _, path in section["pages"]]
    semaphore = asyncio.Semaphore(CONCURRENCY)
    results: list[bytes | None] = [None] * len(pages)

    async def fetch(index: int, md_path: str) -> None:
        async with semaphore:
            url = f"{base_url}/{prefix}{page_url(md_path)}"
            results[index] = await render_pdf(browser, url)

    await asyncio.gather(*(fetch(i, p) for i, p in enumerate(pages)))
    page_counts = [len(PdfReader(io.BytesIO(b)).pages) for b in results]  # type: ignore[arg-type]

    # Row count -- and so TOC page count -- is fixed-height arithmetic (see
    # paginate_toc()), independent of what page numbers actually get
    # printed. So, unlike before, no render-and-check loop is needed to
    # learn it: compute it once, then the content pages' real page numbers,
    # then render the TOC (now that it knows what numbers to print) exactly
    # once.
    toc_pages = paginate_toc(sections)
    toc_page_count = len(toc_pages)
    offset = cover_page_count + toc_page_count + 1
    starts: dict[str, int] = {}
    cursor = offset
    for path, count in zip(pages, page_counts):
        starts[path] = cursor
        cursor += count

    heading = toc_label(locale)
    toc_page_bytes = [
        await render_static_pdf(
            browser, render_toc_page_html(rows, starts, heading, is_first_page=(i == 0))
        )
        for i, rows in enumerate(toc_pages)
    ]

    writer = PdfWriter()
    writer.append(PdfReader(io.BytesIO(cover_bytes)))
    for pdf_bytes in toc_page_bytes:
        writer.append(PdfReader(io.BytesIO(pdf_bytes)))
    for pdf_bytes in results:
        assert pdf_bytes is not None
        writer.append(PdfReader(io.BytesIO(pdf_bytes)))

    # PDF bookmarks/outline mirroring the site's own sidebar nav -- most
    # viewers show these in a side panel, complementing the printed
    # table-of-contents page above for on-screen navigation.
    for section in sections:
        section_start = starts[section["pages"][0][1]] - 1  # pypdf pages are 0-indexed
        parent = writer.add_outline_item(section["title"], section_start)
        for title, path in section["pages"][1:]:
            writer.add_outline_item(title, starts[path] - 1, parent=parent)

    # Real, clickable in-PDF links on every TOC row -- jumps straight to
    # that row's target page, on top of (and in addition to) the outline
    # panel above. Rects come from toc_row_rect()'s fixed-height arithmetic,
    # not measurement, matched against each TOC page's *actual* rendered
    # mediabox (see that function's docstring for why).
    for toc_index, rows in enumerate(toc_pages):
        writer_index = cover_page_count + toc_index
        mediabox = writer.pages[writer_index].mediabox
        page_width, page_height = float(mediabox.width), float(mediabox.height)
        for local_index, row in enumerate(rows):
            rect = toc_row_rect(local_index, toc_index == 0, page_width, page_height)
            target_index = starts[row["path"]] - 1
            writer.add_annotation(
                page_number=writer_index,
                annotation=Link(rect=rect, target_page_index=target_index, border=[0, 0, 0]),
            )

    # Running footer (page number + manual label) stamped onto every real
    # page except the cover -- see make_footer_overlay()'s docstring. Global
    # page numbers fall straight out of the writer's own page order, which
    # is why bookmarks/TOC/footer never need to be kept in sync separately.
    footer_label = f"Ethos Manual · v{version}"
    for index in range(1, len(writer.pages)):
        mediabox = writer.pages[index].mediabox
        overlay = make_footer_overlay(
            float(mediabox.width), float(mediabox.height), index + 1, footer_label
        )
        writer.pages[index].merge_page(overlay)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        writer.write(f)
    total_pages = cover_page_count + toc_page_count + sum(page_counts)
    print(f"wrote {out_path} ({total_pages} pages)")


async def main_async(args: argparse.Namespace) -> None:
    config = load_mkdocs_config(args.mkdocs_yml)
    docs_dir = REPO_ROOT / config["docs_dir"]
    sections = nav_sections(config, docs_dir)
    names = locale_names(config)
    names.setdefault("en", "English")

    locales = ["en", *fully_covered_locales(docs_dir)]
    generated = date.today().isoformat()

    base_url = args.base_url.rstrip("/")
    out_dir = args.out_dir

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            for locale in locales:
                out_path = out_dir / pdf_filename(args.version, locale)
                locale_sections = (
                    sections
                    if locale == "en"
                    else localize_sections(sections, nav_translations_for(config, locale))
                )
                await build_locale_pdf(
                    browser,
                    base_url,
                    locale,
                    names.get(locale, locale),
                    locale_sections,
                    out_path,
                    args.version,
                    generated,
                )
        finally:
            await browser.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-url", required=True, help="e.g. http://localhost:8000 (a locally-served build of site/)"
    )
    parser.add_argument(
        "--out-dir",
        required=True,
        type=Path,
        help="directory to write ethos-manual-<version>-<locale>.pdf into",
    )
    parser.add_argument(
        "--mkdocs-yml", default=REPO_ROOT / "mkdocs.yml", type=Path
    )
    parser.add_argument(
        "--version", default="dev", help="shown on the cover page and in each output filename"
    )
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
