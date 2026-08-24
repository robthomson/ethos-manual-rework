"""Shared `mkdocs.yml` `nav:` parsing/localization helpers.

Extracted from scripts/build_pdfs.py so its Playwright-based PDF pipeline and
scripts/build_pdf_latex.py's pandoc-based one build the exact same page order,
section grouping, and per-locale nav-title translations -- neither pipeline
should have its own, potentially drifting, copy of this logic.
"""

from __future__ import annotations

from pathlib import Path

import yaml


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


def locale_names(config: dict) -> dict[str, str]:
    """locale -> display name (e.g. "fr" -> "Français"), from the i18n plugin config."""
    names = {}
    for plugin in config["plugins"]:
        if isinstance(plugin, dict) and "i18n" in plugin:
            for language in plugin["i18n"]["languages"]:
                names[language["locale"]] = language["name"]
    return names
