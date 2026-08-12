# Versioning

Ethos moved from point-release firmware numbers (1.6.x) to year-based
branding starting with Ethos26 (26.1.x) — the manual's `main` branch now
tracks 26.1, with the full 1.6.x manual frozen on its own `1.6` branch.
This page describes the mechanism that makes that possible, and the
process for cutting the next version when it's time.

## How it works

Versioning is handled by [mike](https://github.com/jimporter/mike), the
tool Material for MkDocs itself recommends. `.github/workflows/deploy.yml`
runs `mike deploy` instead of publishing straight to the `gh-pages` root:
each version is built and committed to its own subfolder there (`/1.6/`,
`/26.1/`, …), and `manual.rt-rc.com/` redirects to whichever version
currently holds the `latest` alias. Material shows a version-select
dropdown automatically, reading `versions.json` (which `mike` maintains)
— this is unrelated to, and composes cleanly with, the locale switcher:
version is the outer path segment, locale (once more than `en` exists) is
the inner one, e.g. `manual.rt-rc.com/26.1/fr/...`.

This reuses the same "subfolder on `gh-pages`" mechanism as [PR
previews](index.md#pr-previews) — `mike`'s version folders and the
`pr-preview/` folder coexist on the same branch without conflicting, since
each only ever touches its own paths.

## Source layout: `main` + frozen branches

- **`main` always tracks the current/latest firmware version's content.**
  Day-to-day editing happens here exactly as it does today — nothing
  changes about the normal contribution workflow.
- Once a new firmware version's manual needs to start diverging from
  what's on `main`, **cut a branch named for the old version first**,
  e.g. `1.6`, to freeze it permanently. `main` then becomes the new
  version's content.
- A frozen branch is not dead — it can still receive corrections via its
  own PRs. It just no longer tracks new-version development.

## Cutting a new version

This is the process that took `main` from 1.6.x to 26.1 (branch `1.6`
frozen, `main` retargeted), and the same steps apply to the next cut
whenever it's needed — substitute the actual old/new version labels below.

1. From `main`, create and push the frozen branch for the version being
   left behind:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   `1.6`'s copy of `.github/workflows/deploy.yml` now permanently deploys
   `mike deploy --push --update-aliases 1.6 latest` on every push to that
   branch — correct as-is, no edit needed, since a branch is a full
   snapshot including its own CI config.

2. On `main`, edit `.github/workflows/deploy.yml`: change the version
   string in the `Deploy version 1.6 with mike` step (and its name) from
   `1.6` to the new version's label (e.g. `26.1`). This is the **only**
   required edit to start deploying the new version — the next push to
   `main` will publish it to `/26.1/` and move the `latest` alias there,
   while `/1.6/` stays exactly as it was.

3. Update the new version's content on `main` for whatever actually
   changed — new/renamed menu sections, new screenshots, updated
   terminology. `mkdocs.yml`'s `nav` can differ freely between branches;
   there's no shared config to keep in sync.

4. Add the new branch's name to `.github/workflows/pr-preview.yml`'s
   `branches:` trigger list if PRs against it should get live previews
   too (frozen branches generally don't need this, since they only take
   occasional correction PRs).

## Screenshots across versions

Screenshots are captured from a specific Ethos build (see [Screenshot
Pipeline](screenshot-pipeline.md)) and belong to whichever branch's UI
they show — a version cut naturally forks the screenshot set along with
everything else, so `1.6/assets/` and (once regenerated for the new UI)
`main`'s `docs/en/assets/` diverge independently after the branch point.
