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

Usage (see .github/workflows/deploy.yml for how CI wires this in):
    python -m playwright install --with-deps chromium
    python scripts/build_pdfs.py --base-url http://localhost:8000 --out-dir site --version 1.6
"""

from __future__ import annotations

import argparse
import asyncio
import io
import sys
from datetime import date
from pathlib import Path

import yaml
from playwright.async_api import Browser, async_playwright
from pypdf import PdfReader, PdfWriter

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "hooks"))
from _locales import fully_covered_locales  # noqa: E402

PDF_FILENAME = "ethos-manual.pdf"
CONCURRENCY = 6

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


def load_mkdocs_config(mkdocs_yml: Path) -> dict:
    return yaml.safe_load(mkdocs_yml.read_text(encoding="utf-8"))


def nav_pages(config: dict) -> list[str]:
    """Ordered list of docs_dir-relative .md paths, walked from `nav:`."""
    pages: list[str] = []

    def walk(entry):
        if isinstance(entry, str):
            pages.append(entry)
        elif isinstance(entry, dict):
            for value in entry.values():
                walk(value)
        elif isinstance(entry, list):
            for item in entry:
                walk(item)

    walk(config["nav"])
    return pages


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


async def build_locale_pdf(
    browser: Browser,
    base_url: str,
    locale: str,
    display_name: str,
    pages: list[str],
    out_path: Path,
    version: str,
    generated: str,
) -> None:
    prefix = "" if locale == "en" else f"{locale}/"
    logo_url = f"{base_url}/assets/ethos-logo.png"
    cover_html = COVER_HTML.format(
        logo_url=logo_url, subtitle=display_name, version=version, generated=generated
    )

    cover_page = await browser.new_page()
    try:
        await cover_page.set_content(cover_html, wait_until="networkidle")
        cover_bytes = await cover_page.pdf(format="A4", print_background=True)
    finally:
        await cover_page.close()

    semaphore = asyncio.Semaphore(CONCURRENCY)
    results: list[bytes | None] = [None] * len(pages)

    async def fetch(index: int, md_path: str) -> None:
        async with semaphore:
            url = f"{base_url}/{prefix}{page_url(md_path)}"
            results[index] = await render_pdf(browser, url)

    await asyncio.gather(*(fetch(i, p) for i, p in enumerate(pages)))

    writer = PdfWriter()
    writer.append(PdfReader(io.BytesIO(cover_bytes)))
    for pdf_bytes in results:
        assert pdf_bytes is not None
        writer.append(PdfReader(io.BytesIO(pdf_bytes)))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        writer.write(f)
    print(f"wrote {out_path} ({len(pages) + 1} pages)")


async def main_async(args: argparse.Namespace) -> None:
    config = load_mkdocs_config(args.mkdocs_yml)
    pages = nav_pages(config)
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
                out_path = (
                    out_dir / PDF_FILENAME
                    if locale == "en"
                    else out_dir / locale / PDF_FILENAME
                )
                await build_locale_pdf(
                    browser,
                    base_url,
                    locale,
                    names.get(locale, locale),
                    pages,
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
        "--out-dir", required=True, type=Path, help="directory to write <locale>/ethos-manual.pdf into"
    )
    parser.add_argument(
        "--mkdocs-yml", default=REPO_ROOT / "mkdocs.yml", type=Path
    )
    parser.add_argument("--version", default="dev", help="shown on the cover page")
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
