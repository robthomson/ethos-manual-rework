# Adding a New Language

A step-by-step playbook for bootstrapping a locale from zero to a fully
translated, fully navigable manual — written for whoever (human or agent)
does the next one. Every step below was actually run, in this order, for
`de`, `fr`, `es`, `it`, `pt-BR`, and `zh`; the gotchas called out are real
failures hit while doing it, not hypotheticals.

## Checklist

Work through in order; each item links to the section with the actual
commands and the gotchas hit doing it for real. Don't skip straight to
step 4 — steps 1 and 3 are cheap and avoid rework later.

- [ ] **[1](#1-confirm-the-locale-code-before-touching-anything)** — Confirm Ethos ships a UI in this language, and pick a locale code `mkdocs-material` actually has a template for (not necessarily the code FrSky's own tooling uses internally — `pb` vs `pt-BR` bit us here).
- [ ] **[2](#2-add-the-locale-to-mkdocsyml)** — Add the locale to `mkdocs.yml` (no `nav_translations` yet).
- [ ] **[3](#3-seed-a-glossary-in-scriptstranslatepy)** — Seed a ~30-term glossary in `scripts/translate.py`'s `GLOSSARIES`.
- [ ] **[4](#4-translate)** — Run `scripts/translate.py --only <code>` (dry-run first); confirm `0 failed`.
- [ ] **[5](#5-check-for-existing-screenshots-before-considering-the-simulator)** — Check the old `ethos-manual` repo for an already-captured screenshot set before assuming the simulator pipeline is needed; bulk-copy and spot-check visually if one matches.
- [ ] **[6](#6-check-and-fix-anchor-links)** — Run `python scripts/check_anchors.py --fix`.
- [ ] **[7](#7-verify-for-real)** — `mkdocs build --strict` and check `$?` is `0` (not just that the output looks clean); `check_anchors.py` reports 0.
- [ ] **[8](#8-add-nav_translations-once-after-page-coverage-is-complete)** — Once page coverage is complete, add `nav_translations` (leaf labels from each page's own H1, section tabs from the glossary).
- [ ] **[9](#9-ship-it)** — Commit, push, watch the Action, verify live (allow for CDN propagation lag on brand-new paths).

## 1. Confirm the locale code before touching anything {: #1-confirm-the-locale-code-before-touching-anything }

Two separate things need to agree, and getting either wrong is annoying to
unwind later (URLs bake the code in permanently):

- **Does Ethos actually ship a UI in this language?** A manual in a
  language the firmware doesn't support is confusing, not useful. FrSky's
  own [Ethos Suite](https://www.frsky-rc.com/) desktop app ships an
  `i18n/*.json` file per supported language — installed locally it's at
  `Program Files/Ethos Suite/i18n/`. That list (`cs`, `de`, `en`, `es`,
  `fr`, `he`, `it`, `nl`, `no`, `pb`, `sk`, `zh-CN` at last check) is a
  reliable proxy for what Ethos itself supports.
- **Does `mkdocs-material` ship a language-switcher template for that
  code?** This is a *different* list, and the two don't always agree —
  Ethos Suite's own folder is literally named `pb`, but Material has no
  `partials/languages/pb.html`, only `pt-BR.html`. Using `pb` builds fine
  right up until `mkdocs build`'s post-build sitemap step, where it
  crashes with `jinja2.exceptions.TemplateNotFound` — **and that crash
  does not contain the word "error" or "warning"**, so grepping build
  output for those (a totally reasonable thing to do) will report a clean
  build that actually exited non-zero. Always check `$?` after
  `mkdocs build --strict`, not just its printed output. To see the exact
  codes Material supports:

  ```python
  import material
  from pathlib import Path
  p = Path(material.__file__).parent / "templates" / "partials" / "languages"
  print(sorted(x.stem for x in p.glob("*.html")))
  ```

## 2. Add the locale to `mkdocs.yml` {: #2-add-the-locale-to-mkdocsyml }

```yaml
languages:
  - locale: <code>
    name: <native display name>
    build: true
```

No `nav_translations` yet — that's step 6, after there's real content to
match labels against.

## 3. Seed a glossary in `scripts/translate.py` {: #3-seed-a-glossary-in-scriptstranslatepy }

Add a `GLOSSARIES["<code>"]` entry (see the existing `fr`/`de`/`es`/`it`
entries for the term list to cover — flight-surface names, mix/output/
timer/trim vocabulary, switches, sensors, etc.). This is what keeps
terminology consistent from the very first translated page instead of
drifting page to page. ~30 terms is enough; it's a floor to build on, not
a complete dictionary.

If the console errors with `UnicodeEncodeError` partway through a run —
this hit `zh` specifically — it's because Windows' console defaults to
`cp1252`, which can't encode non-Latin scripts. Already fixed at the top
of the script (`sys.stdout.reconfigure(encoding="utf-8", ...)`); if it
resurfaces, that's where to look.

## 4. Translate {: #4-translate }

```bash
python scripts/translate.py --only <code> --dry-run   # confirm scope/cost first
python scripts/translate.py --only <code> --yes
```

Independent locales can run **in parallel** (separate background
processes) — they only read shared files (`docs/en/`, `mkdocs.yml`) and
write to entirely separate `docs/<code>/` trees, so there's no race
condition. Four locales translating concurrently finished in roughly the
same wall-clock time as one.

Check the log for `Done: N translated, 0 failed` before moving on.

## 5. Check for existing screenshots before considering the simulator {: #5-check-for-existing-screenshots-before-considering-the-simulator }

**Don't assume new screenshots require running the simulator pipeline —
check first.** The predecessor repo
([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), typically
cloned as a sibling directory) may already have a captured, per-language
screenshot set from FrSky's own team sitting unused. It did for German,
French (via the `french_LT/` folder — not the smaller, incomplete
`french/` one), Italian, and Spanish; it had nothing for Portuguese or
Chinese. Check filename overlap against what this repo currently
references:

```python
from pathlib import Path
old_repo_lang_assets = Path("../ethos-manual/<language-folder>/assets")  # sibling checkout
current = {p.name for p in Path("docs/en/assets").iterdir() if p.suffix.lower() == ".png"}
old = {p.name for p in old_repo_lang_assets.glob("*.png")}
print(f"{len(old & current)} / {len(current)} would match")
```

A high match rate (≥90%, in practice) means it's a straight copy into
`docs/<code>/assets/` — `fallback_to_default` in `mkdocs.yml` means
that's *all* that's needed; no markdown changes. **Visually spot-check
at least one copied image** before trusting the match (open it, confirm
it's genuinely the target language's UI, not a stale/mismatched capture)
— filenames matching doesn't strictly guarantee content matches, even
though it always has so far.

If there's no match (Portuguese, Chinese, or any future language the old
repo never covered), the locale correctly falls back to English
screenshots automatically. That's the expected, working state — closing
the gap for real means porting/running the actual macro pipeline against
the simulator (see [Screenshot Pipeline](screenshot-pipeline.md)), which
is out of scope for a text-translation pass and needs a local simulator
install.

## 6. Check and fix anchor links {: #6-check-and-fix-anchor-links }

Translating a heading changes its auto-generated slug, which silently
breaks any `#that-heading-slug` link from another page — and **this is
not a build error**: `mkdocs build --strict` does not fail on it, so
nothing will tell you it happened except a dead link a reader clicks.

```bash
python scripts/check_anchors.py         # report only
python scripts/check_anchors.py --fix   # pin every finding, in en + every locale that has the page
```

This is a real, recurring class of bug, not a one-time cleanup — every
locale added so far surfaced a handful of new instances (the ones that
happened to coincide with a `<locale>`-specific translated slug diverging
from English, which a *different* locale's translation didn't). Run it
after every batch of new/updated translations. It rebuilds the site
itself by default (`mkdocs build --strict` first) so results are never
stale.

## 7. Verify for real {: #7-verify-for-real }

```bash
mkdocs build --strict; echo "exit code: $?"   # must be 0, not just free of "error"/"warn" text
python scripts/check_anchors.py                # must report 0
```

## 8. Add `nav_translations` — once, after page coverage is complete {: #8-add-nav_translations-once-after-page-coverage-is-complete }

Tab and sidebar labels in `nav:` don't pick up a locale's translated page
title automatically unless the nav entry has no explicit label at all.
Add `nav_translations` under the locale's `mkdocs.yml` entry once (not
before) the locale has full — or near-full — page coverage; translating
the chrome ahead of the content it points to reads oddly. Leaf labels
should be copied verbatim from each translated page's own H1 (so the
sidebar text matches the page heading exactly); section-tab labels
(Home, Getting Started, ...) should match the glossary from step 3.
Extract every H1 programmatically rather than retyping labels by hand —
it's faster and removes any chance of a transcription mismatch:

```python
import re
h1 = re.search(r"^#\s+(.+)$", Path(f"docs/{code}/{rel_path}").read_text(encoding="utf-8"), re.MULTILINE).group(1).strip()
```

Skip `Translation Status` — it's a generated, English-only maintainer
page with no translated equivalent in any locale.

## 9. Ship it {: #9-ship-it }

Commit, push to `main`, and watch the `Deploy Docs` Action run. GitHub
Pages' CDN can 404 a brand-new locale path for the first 15–30+ seconds
after a genuinely successful deploy — that's edge-cache propagation lag,
not a failure. Confirm via the GitHub API that the file exists on
`gh-pages` before worrying:

```bash
gh api "repos/<owner>/<repo>/contents/<version>/<code>/<path>?ref=gh-pages" --jq '.sha, .size'
```

then retry the live URL with a short backoff.
