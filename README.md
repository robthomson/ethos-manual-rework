# ethos-manual-rework

Source for a rebuilt, git-based user manual for the FrSky Ethos radio
firmware, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

This replaces [`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), whose
English tree only ever contained a screenshot-generation rig (no Markdown
prose) and whose translated trees were separate, hand-maintained GitBook
exports with no shared source of truth. See
[`docs/en/contributing/index.md`](docs/en/contributing/index.md) for the
reasoning and workflow going forward.

## Local preview

```
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000/.

## Structure

All content lives under `docs/<locale>/`, currently just `docs/en/`. Screenshots
live alongside the content in `docs/en/assets/` — they're captured per-language
(the radio UI itself is localized), so each locale will eventually have its
own `assets/` folder rather than a shared one. The site navigation is defined
in [`docs/en/SUMMARY.md`](docs/en/SUMMARY.md) (one line per page, nested
under its section); add new pages there as well as under `docs/en/` for
them to appear in the nav. Per-locale nav titles are separate, in
`mkdocs.yml`'s `nav_translations:` blocks — see
[`docs/en/contributing/adding-a-language.md`](docs/en/contributing/adding-a-language.md).

See [`docs/en/contributing/screenshot-pipeline.md`](docs/en/contributing/screenshot-pipeline.md)
for how the screenshots are (and will again be) generated from the Ethos
simulator.

## Deployment

Pushing to `main` builds the site and publishes it to the `gh-pages` branch
via `.github/workflows/deploy.yml`, served at
[manual.rt-rc.com](https://manual.rt-rc.com) — a placeholder domain used
until this project moves to the official FrSky repo, at which point it'll
be repointed.
