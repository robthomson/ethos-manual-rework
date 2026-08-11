"""Generates docs/en/contributing/translation-status.md before every build.

For each locale folder under docs/ (anything besides "en"), compares every
English page's last-changed commit against the `translated_from:` commit
recorded in that locale's frontmatter, and reports each page as current,
stale, or missing.

Runs automatically via mkdocs.yml's `hooks:` config -- no separate CI step,
no separate local command. The generated file is gitignored and rebuilt
fresh on every `mkdocs build`/`mkdocs serve`, anywhere.

Needs full git history to work (`git log -1 -- <path>` on a shallow clone
only sees commits within the shallow window) -- CI checkouts use
`fetch-depth: 0` for this reason.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import yaml

STATUS_FILENAME = "translation-status.md"


def _git_last_commit(repo_root: Path, path: Path) -> tuple[str | None, str | None]:
    """Return (sha, ISO-8601 date) of the last commit that touched `path`."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H%x1f%cI", "--", str(path)],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_root,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None, None
    if not out:
        return None, None
    sha, date = out.split("\x1f")
    return sha, date


def _read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def on_pre_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    en_dir = docs_dir / "en"
    repo_root = Path(config["config_file_path"]).parent
    output_path = en_dir / "contributing" / STATUS_FILENAME

    # A locale folder is any docs_dir subdirectory (besides "en") that
    # actually contains Markdown -- as opposed to shared, non-locale
    # folders living alongside it (docs/assets, docs/stylesheets, ...),
    # which we don't want mistaken for locales.
    locales = sorted(
        p.name
        for p in docs_dir.iterdir()
        if p.is_dir() and p.name != "en" and any(p.rglob("*.md"))
    )

    en_pages = sorted(
        p.relative_to(en_dir).as_posix()
        for p in en_dir.rglob("*.md")
        if p.name != STATUS_FILENAME
    )

    counts = {locale: {"current": 0, "stale": 0, "missing": 0} for locale in locales}
    rows = []

    for rel in en_pages:
        en_sha, en_date = _git_last_commit(repo_root, en_dir / rel)
        cells = []
        for locale in locales:
            locale_path = docs_dir / locale / rel
            if not locale_path.exists():
                cells.append("❌ missing")
                counts[locale]["missing"] += 1
                continue
            translated_from = _read_frontmatter(locale_path).get("translated_from")
            if translated_from is None:
                cells.append("⚠️ stale (no marker)")
                counts[locale]["stale"] += 1
            elif en_sha and translated_from == en_sha:
                cells.append("✅ current")
                counts[locale]["current"] += 1
            else:
                cells.append("⚠️ stale")
                counts[locale]["stale"] += 1
        rows.append((rel, en_date, cells))

    lines = [
        "# Translation Status",
        "",
        "Generated automatically before every build — not tracked in git, "
        "always current as of the last build. Compares each locale's "
        "`translated_from:` frontmatter against the English page's actual "
        "last-changed commit. See [Translation "
        "plan](index.md#translation-plan).",
        "",
    ]

    if not locales:
        lines.append("No locales beyond English exist yet.")
    else:
        for locale in locales:
            c = counts[locale]
            total = c["current"] + c["stale"] + c["missing"]
            lines.append(
                f"**{locale}**: {c['current']}/{total} pages current, "
                f"{c['stale']} stale, {c['missing']} missing.  "
            )
        lines.append("")

        header = "| Page | " + " | ".join(locales) + " | Last English change |"
        sep = "|---|" + "---|" * len(locales) + "---|"
        lines.append(header)
        lines.append(sep)
        for rel, en_date, cells in rows:
            date_str = en_date.split("T")[0] if en_date else "—"
            lines.append(f"| `{rel}` | " + " | ".join(cells) + f" | {date_str} |")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
