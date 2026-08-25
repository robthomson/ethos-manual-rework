"""Shared nav-structure parsing/localization helpers.

Extracted from scripts/build_pdfs.py so its Playwright-based PDF pipeline and
scripts/build_pdf_latex.py's pandoc-based one build the exact same page order,
section grouping, and per-locale nav-title translations -- neither pipeline
should have its own, potentially drifting, copy of this logic.

Nav *structure* (page order/grouping) comes from docs/en/SUMMARY.md (the
mkdocs-literate-nav plugin's own nav source -- see mkdocs.yml's plugins:
list) as of this file's rewrite; nav *translations* (per-locale titles)
still come from mkdocs.yml's plugins.i18n.languages[].nav_translations:,
unchanged. literate-nav must be the *last* plugin in mkdocs.yml (confirmed
live: placing it before i18n breaks nav resolution) -- unrelated to this
file, which reads SUMMARY.md directly rather than through the plugin.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml


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
        # Indent 0 (this repo's SUMMARY.md never nests deeper than one
        # level, matching the old YAML nav's own shape, which had no
        # recursion either) starts a new section; anything indented is a
        # child of whichever section was most recently started.
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


def locale_names(config: dict) -> dict[str, str]:
    """locale -> display name (e.g. "fr" -> "Français"), from the i18n plugin config."""
    names = {}
    for plugin in config["plugins"]:
        if isinstance(plugin, dict) and "i18n" in plugin:
            for language in plugin["i18n"]["languages"]:
                names[language["locale"]] = language["name"]
    return names
