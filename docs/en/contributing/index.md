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

1. Branch off `main`.
2. Edit the relevant `.md` file(s) under `docs/en/`.
3. Preview locally with `mkdocs serve` (see the root
   [README](https://github.com/robthomson/ethos-manual-rework)) or rely on
   the PR preview once one is wired up.
4. Open a pull request.

Screenshots referenced from a page live next to it in `docs/en/assets/` and
are just Markdown image links — no special syntax. See
[Screenshot Pipeline](screenshot-pipeline.md) for how they're generated.

## Translation plan

Translation tooling is deliberately **not** built yet. Non-technical
translators will need to learn enough git to branch, edit, and open a PR —
a real barrier, but preferred over standing up and maintaining a separate
translation app before there's a stable English source to translate from.
Content is kept in plain Markdown specifically so that path stays open:

- In the near term, a translator (human or AI) works from the English
  `docs/en/` tree directly, producing a sibling `docs/<locale>/` tree with
  the same file structure.
- [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n) is
  the likely plugin once a second locale exists — it understands exactly
  this folder-per-locale layout (`docs/en/…`, `docs/fr/…`) and adds a
  language switcher automatically.
- Screenshots are **not** shared across locales — the Ethos UI itself is
  localized, so each locale's `assets/` folder needs its own screenshots
  captured with that language's radio settings file (see [Screenshot
  Pipeline](screenshot-pipeline.md)).
- Whether translation staleness (English pages that changed after they were
  translated) needs its own tooling, versus being tracked by git history
  alone, is an open question to revisit once there's a second language to
  actually maintain.
