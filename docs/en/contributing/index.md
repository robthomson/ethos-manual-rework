# Contributing

## Why this manual exists

The previous manual ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
split into two disconnected halves per language. The English tree was only
ever a **screenshot-generation rig** — shell scripts driving the real Ethos
simulator through a Lua macro API to capture UI screenshots — with no
Markdown (or any other plain-text) source for the manual's actual prose; the
English text only ever existed as a stack of PDF/ODT exports. The French
tree, by contrast, was a fully written GitBook export with real content, but
built and maintained independently, with its own separate set of
hand-pasted screenshots. Other languages had neither. There was no single
source of truth to translate *from*, and no way to tell when a translated
page had drifted out of date with the (nonexistent) English source.

This repo starts over with one format for every page, in every language:
plain Markdown, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(the same stack used for [wingflight-docs](https://doc.wingflight.org)),
deployed to GitHub Pages on every push to `main`.

## Workflow

There's no CMS or web editor in front of the content — writers and
translators work directly in git, the same as any other change to this
repo:

1. Branch off `main` (in this repo directly — see the fork note below).
2. Edit the relevant `.md` file(s) under `docs/en/`.
3. Preview locally with `mkdocs serve` (see the root
   [README](https://github.com/robthomson/ethos-manual-rework)), or just open
   the pull request and use the automatic PR preview below.
4. Open a pull request.

Screenshots referenced from a page live next to it in `docs/en/assets/` and
are just Markdown image links — no special syntax. See
[Screenshot Pipeline](screenshot-pipeline.md) for how they're generated.

### PR previews

Every pull request against `main` gets its own live preview, built and
deployed automatically by `.github/workflows/pr-preview.yml`: at
`manual.rt-rc.com/pr-preview/<PR number>/`, linked in a bot comment on the
PR and updated on every push. It's removed automatically when the PR closes.
The main site itself (`manual.rt-rc.com`) is unaffected — previews live
alongside it in a `pr-preview/` folder on the `gh-pages` branch that survives
every production deploy.

This only runs for branches pushed directly to this repo, not forks — a PR
from a fork won't get a live preview (GitHub withholds write access to
`GITHUB_TOKEN` for fork-triggered `pull_request` workflows, deliberately, so
a fork can't use CI to push arbitrary content to `gh-pages`). Fork
contributors can still preview locally with `mkdocs serve`.

## Versioning

Multiple firmware versions' manuals (e.g. 1.6 alongside a future Ethos26)
live in the same repo as separate branches, each deployed to its own
`manual.rt-rc.com/<version>/` path with a version-select dropdown — see
[Versioning](versioning.md) for the full scheme and how to cut a new one.

## Translation plan {: #translation-plan }

Translators (human or AI) work directly in git, same as any other
change — no CMS, no separate translation app. A first French pilot
(a handful of pages) proved the mechanics out end to end; here's how it
actually works.

### Adding/updating a translation

1. Branch, create/edit `docs/<locale>/<same path as the English page>`,
   translating the prose. Keep code-literal text (key names like `ENT`,
   `RTN`, UI element names shown on screen) as-is.
2. Stamp the page with which English commit it was translated from:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Find that sha with `git log -1 --format=%H -- docs/en/<path>`.
3. **If the English page has a heading that other pages link to by
   anchor** (check by searching for `#that-heading-slug` across
   `docs/en/`), don't let the translated heading's own auto-generated
   slug change the target — pin the same, locale-stable ID explicitly
   with `attr_list` (already enabled):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Skipping this doesn't break the build, but it does silently break the
   anchor scroll-to for any other, still-untranslated page linking into
   that heading via fallback.
4. Open a PR — [preview it](#pr-previews) like any other change, including
   the language switcher.

### Screenshots

Nothing to duplicate up front. [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
falls back to the English file for *any* asset a locale doesn't have its
own copy of — a translated page's `../assets/foo.png` just works,
unmodified, showing the English screenshot, until a real localized one
(captured once the [screenshot pipeline](screenshot-pipeline.md) is
ported and run against that language's radio settings) is dropped in at
the same filename under `docs/<locale>/assets/`, which silently
overrides the fallback from then on.

### Staleness tracking

[Translation Status](translation-status.md) is generated automatically
before every build (`hooks/i18n_status.py`, wired up via `mkdocs.yml`'s
`hooks:` — runs locally, in PR previews, and in production alike, always
current, never committed to git) and compares every locale's
`translated_from` marker against each English page's actual last-changed
commit: **current**, **stale** (English moved on), or **missing**. That
page is the worklist — no GitHub Issues, no digging through Actions logs.

### Automated translation (optional)

`scripts/translate.py` is a standalone local script (not part of the site
build or CI) that drives the same missing/stale worklist through the
Claude API to produce a first-draft translation for each page, stamped
with the correct `translated_from:` frontmatter automatically:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

It reads every locale from `mkdocs.yml`'s `i18n` plugin config by default
(`--only` restricts to specific ones), skips anything already current
unless `--force` is passed, and never commits or pushes — it only writes
files under `docs/<locale>/`, same as if you'd hand-edited them. Review the
diff, do the [anchor-pinning](#addingupdating-a-translation) check for any
newly-translated heading, then open a PR as usual.

The system prompt pre-seeds Claude with the manual's domain (FrSky Ethos
radio firmware, RC hobbyist audience) and a list of terms that must never
be translated (physical key names, protocol names, brand names), the same
technique used by the sister
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite)
repo's own `bin/i18n/auto-translate.py`. A glossary of terms established
during the French pilot is baked in for `fr`; extend
`GLOSSARIES` in the script the same way once another locale has a few
pages translated and reviewed.

### Nav labels (`nav_translations`)

Tab and sidebar labels in `nav:` (e.g. "Model Setup") don't pick up a
locale's translated page title automatically unless the nav entry has no
explicit label at all (e.g. `- how-to/index.md` — MkDocs then uses that
page's own H1). Everywhere `nav:` gives an explicit `Label: path.md`
string, or names a section (`Model Setup:` as a dict key with children),
that label stays in English until the locale's `nav_translations` map in
`mkdocs.yml` covers it — added for a locale once its page coverage is
substantial enough that translating the chrome ahead of most of the
content wouldn't read oddly. `fr`'s map was filled in once French reached
full page coverage; each leaf label was copied verbatim from that page's
own translated H1, so the sidebar text matches the page heading exactly.
