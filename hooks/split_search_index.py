"""Splits the combined multi-language search index into one file per locale.

mkdocs-static-i18n builds every locale into a single site, and its
`reconfigure_search_index` step folds every locale's pages into ONE
search/search_index.json -- so out of the box, searching from an English
page also surfaces French/German/... results, with no config knob to turn
it off (https://github.com/ultrabug/mkdocs-static-i18n/issues/271).

mkdocs-static-i18n builds each locale's pages via its own nested, complete
build pass (see the "Building '<locale>' documentation to directory: ..."
log lines), and each of those passes fires the normal `on_post_build` event
-- so a plain `on_post_build` hook here would see search/search_index.json
in a different partial, single-locale state on every call. The final,
correctly deduplicated, all-locales-combined index is instead written by
`I18n.reconfigure_search_index()` calling the search plugin's
`on_post_build` *directly* (bypassing the normal event dispatch other hooks
tap into) once every locale pass has finished. `on_shutdown` fires once, at
the very end of the `mkdocs` process, strictly after all of that -- so that
is where this hook does its work, using the config captured from whichever
`on_post_build` call happened to run last (site_dir/docs_dir don't change
between passes).

Reads the final search/search_index.json, partitions its `docs` entries by
the locale prefix on each entry's `location` (the default locale, English,
has no prefix -- see `docs_structure: folder` in mkdocs.yml), and writes
search/search_index-<locale>.json per locale.

docs/javascripts/search-scope.js picks the matching split file at runtime
based on the locale segment in the current URL; the locale list it needs
for that is patched into the deployed copy of that file here, so the two
never drift apart.
"""

from __future__ import annotations

import json
from pathlib import Path

_last_config = None


def on_post_build(config, **kwargs):
    # Called once per locale's nested build pass, each time with the same
    # site_dir/docs_dir -- just stash it for on_shutdown, which is where the
    # actually-final combined index is read. See module docstring.
    global _last_config
    _last_config = config


def on_shutdown(**kwargs):
    if _last_config is None:
        return

    site_dir = Path(_last_config["site_dir"])
    index_path = site_dir / "search" / "search_index.json"
    if not index_path.exists():
        return

    docs_dir = Path(_last_config["docs_dir"])
    default_locale = "en"

    # Same "does it actually contain markdown" test hooks/i18n_status.py
    # uses to tell locale folders apart from shared, non-locale folders
    # living alongside them (docs/assets, docs/javascripts, docs/stylesheets).
    locales = sorted(
        p.name
        for p in docs_dir.iterdir()
        if p.is_dir() and any(p.rglob("*.md"))
    )
    other_locales = [locale for locale in locales if locale != default_locale]

    data = json.loads(index_path.read_text(encoding="utf-8"))
    per_locale: dict[str, list[dict]] = {locale: [] for locale in locales}

    for entry in data["docs"]:
        location = entry["location"]
        matched = default_locale
        for locale in other_locales:
            if location == locale or location.startswith(f"{locale}/"):
                matched = locale
                break
        per_locale[matched].append(entry)

    for locale, docs in per_locale.items():
        out_path = site_dir / "search" / f"search_index-{locale}.json"
        out_path.write_text(
            json.dumps({"config": data["config"], "docs": docs}),
            encoding="utf-8",
        )

    search_scope_js = site_dir / "javascripts" / "search-scope.js"
    if search_scope_js.exists():
        text = search_scope_js.read_text(encoding="utf-8")
        text = text.replace(
            "/*__I18N_LOCALES__*/ []",
            "/*__I18N_LOCALES__*/ " + json.dumps(other_locales),
        )
        search_scope_js.write_text(text, encoding="utf-8")
