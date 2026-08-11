# Contributing

Quick reference — the full write-up lives in the published manual itself:

- [Contributing](docs/en/contributing/index.md) — why this repo exists, the
  git-based editing workflow, and the translation plan.
- [Screenshot Pipeline](docs/en/contributing/screenshot-pipeline.md) — how
  the manual's screenshots are captured from the Ethos simulator.

## Local preview

```
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000/.

## Workflow

1. Branch off `main`.
2. Edit the relevant `.md` file(s) under `docs/en/`.
3. Preview locally with `mkdocs serve`.
4. Open a pull request.
