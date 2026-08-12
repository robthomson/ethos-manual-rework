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
import re
import sys
from datetime import date
from html import escape
from pathlib import Path

import material
import yaml
from playwright.async_api import Browser, async_playwright
from pypdf import PdfReader, PdfWriter

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "hooks"))
from _locales import fully_covered_locales  # noqa: E402

CONCURRENCY = 6

# mkdocs-material's own bundled UI-string translations -- reused below so
# the PDF's table-of-contents heading says "Table of contents" in whatever
# language matches that locale's actual sidebar TOC, without re-guessing a
# translation here.
MATERIAL_LANG_DIR = Path(material.__file__).resolve().parent / "templates" / "partials" / "languages"


def pdf_filename(version: str, locale: str) -> str:
    return f"ethos-manual-{version}-{locale}.pdf"


COVER_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
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
"""

TOC_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 2.5rem 3rem;
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a1a1a;
  }}
  h1 {{ font-size: 1.75rem; font-weight: 300; margin: 0 0 2rem; }}
  .row {{ display: flex; align-items: baseline; gap: 0.5rem; padding: 0.2rem 0; }}
  .row.section {{ font-weight: 600; margin-top: 0.9rem; }}
  .row.page {{ margin-left: 1.5rem; font-weight: 400; font-size: 0.95rem; }}
  .title {{ white-space: nowrap; }}
  .leader {{ flex: 1 1 auto; border-bottom: 1px dotted #999; margin-bottom: 0.3rem; }}
  .page-number {{ white-space: nowrap; color: #555; }}
</style>
</head>
<body>
  <h1>{heading}</h1>
  {rows}
</body>
</html>
"""

TOC_ROW = (
    '<div class="row {css_class}">'
    '<span class="title">{title}</span><span class="leader"></span>'
    '<span class="page-number">{page}</span></div>'
)


def load_mkdocs_config(mkdocs_yml: Path) -> dict:
    return yaml.safe_load(mkdocs_yml.read_text(encoding="utf-8"))


def nav_sections(config: dict) -> list[dict]:
    """Top-level `nav:` entries, preserving titles and grouping -- used to
    build the PDF's table of contents (nav_pages() below only needed the
    flat path list, and threw titles away).

    Each entry is {"title": str, "pages": [(title, md_path), ...]}. A
    section that's a single leaf (e.g. "Home: index.md") has exactly one
    page, whose title matches the section title. A section that's a group
    (e.g. "Getting Started:") may start with a bare, title-less landing
    page -- `pages[0]` reuses the section's own title for that one --
    followed by its labelled sub-pages.
    """
    sections = []
    for entry in config["nav"]:
        if not isinstance(entry, dict):
            continue
        for title, value in entry.items():
            pages: list[tuple[str, str]] = []
            if isinstance(value, str):
                pages.append((title, value))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        pages.append((title, item))
                    elif isinstance(item, dict):
                        for sub_title, sub_value in item.items():
                            pages.append((sub_title, sub_value))
            sections.append({"title": title, "pages": pages})
    return sections


def nav_pages(config: dict) -> list[str]:
    """Ordered list of docs_dir-relative .md paths, flattened from nav_sections()."""
    return [path for section in nav_sections(config) for _, path in section["pages"]]


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


def render_toc_html(sections: list[dict], page_numbers: dict[str, int], heading: str) -> str:
    rows = []
    for section in sections:
        first_title, first_path = section["pages"][0]
        rows.append(
            TOC_ROW.format(
                css_class="section", title=escape(first_title), page=page_numbers[first_path]
            )
        )
        for title, path in section["pages"][1:]:
            rows.append(
                TOC_ROW.format(css_class="page", title=escape(title), page=page_numbers[path])
            )
    return TOC_HTML.format(heading=escape(heading), rows="\n  ".join(rows))


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

    def page_starts(offset: int) -> dict[str, int]:
        """md_path -> its first page number in the final, merged PDF."""
        starts: dict[str, int] = {}
        cursor = offset
        for path, count in zip(pages, page_counts):
            starts[path] = cursor
            cursor += count
        return starts

    # The TOC's own page count depends on its rendered content, which
    # depends on the page numbers it prints, which depend on the TOC's own
    # page count -- solved by rendering it, checking how many pages it
    # actually came out as, and re-rendering with the real offset if that
    # guess was wrong. Converges in practice within a couple of passes,
    # since numbers shifting by a page or two essentially never changes how
    # many lines wrap.
    heading = toc_label(locale)
    toc_page_count = 1
    for _ in range(3):
        offset = cover_page_count + toc_page_count + 1
        starts = page_starts(offset)
        toc_html = render_toc_html(sections, starts, heading)
        toc_bytes = await render_static_pdf(browser, toc_html)
        new_count = len(PdfReader(io.BytesIO(toc_bytes)).pages)
        if new_count == toc_page_count:
            break
        toc_page_count = new_count

    writer = PdfWriter()
    writer.append(PdfReader(io.BytesIO(cover_bytes)))
    writer.append(PdfReader(io.BytesIO(toc_bytes)))
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

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        writer.write(f)
    total_pages = cover_page_count + toc_page_count + sum(page_counts)
    print(f"wrote {out_path} ({total_pages} pages)")


async def main_async(args: argparse.Namespace) -> None:
    config = load_mkdocs_config(args.mkdocs_yml)
    sections = nav_sections(config)
    names = locale_names(config)
    names.setdefault("en", "English")

    docs_dir = REPO_ROOT / config["docs_dir"]
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
