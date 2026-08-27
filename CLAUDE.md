# Notes for Claude Code

Cross-repo pointers and reminders for whoever (human or agent) works in
this repo next. Keep entries short; link out rather than duplicating
detail that lives elsewhere.

## Real manual content sync (repeatable ODT → Markdown process)

`docs/<locale>/` in this repo is populated from `.odt` masters (or, for a
locale/branch where that doesn't exist, left as-is) by a process that
lives in **other** repos, not this one:

- `ethos-tools/manual-sync/RUNBOOK.md` — the step-by-step process:
  building `PAGE_MAP` for English first, verifying a locale's real
  structure before trusting it, deriving other locales' mappings
  positionally instead of hand-writing them, the PDF-only-locale dead end
  (confirmed encoding-corruption finding on the `1.6` branch's German/
  Italian/Spanish PDFs), and the full verification checklist.
- `ethos-tools/manual-sync/README.md` — per-script reference
  (`sync.py`, `sync_mapped.py`, `page_map.py`/`page_map_<branch>.py`).
- `ethos-manual/forge/odt_to_markdown.py` — the actual `.odt` → Markdown
  converter.

If asked to sync real content for a new locale, bring another branch of
*this* repo onto real content, or otherwise do more of this kind of
work, start there rather than reinventing the mapping/derivation logic
from scratch — it's already built, tested, and documented.

Also worth knowing before touching `docs/<locale>/` by hand: `main` and
`1.6` are separate mkdocs-versioned branches (see
`docs/en/contributing/versioning.md`) with their **own** independent
`mkdocs.yml`, `extra.real_content_locales`, and set of which locales
have real vs. no content — don't assume a decision made on one branch
(e.g. which locales are configured, which have real content) carries
over to the other without checking.
