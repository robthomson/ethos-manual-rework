"""Points the deployed site's "Download PDF" link at a GitHub Release.

scripts/build_pdfs.py only renders the PDFs to a local directory -- it
doesn't know (or need to know) where they end up. This is the small,
separate step that does: run *after* deploy.yml has uploaded them as
release assets, against the already-deployed docs/javascripts/locale-scope.js
(copied verbatim into the built site by mkdocs, no templating of its own),
patching in the release download URL prefix so the browser-side lookup in
that file (see its docstring) has something to work with.

Usage (see .github/workflows/deploy.yml for how CI wires this in):
    python scripts/patch_pdf_links.py --tag 1.6 --locale-scope-js pages/1.6/javascripts/locale-scope.js
"""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER = '/*__PDF_BASE_URL__*/ ""'


def repo_slug(mkdocs_yml: Path) -> str:
    """"https://github.com/<owner>/<repo>[.git]" -> "<owner>/<repo>"."""
    config = yaml.safe_load(mkdocs_yml.read_text(encoding="utf-8"))
    repo_url = config["repo_url"].rstrip("/")
    if repo_url.endswith(".git"):
        repo_url = repo_url[: -len(".git")]
    return "/".join(repo_url.split("/")[-2:])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True, help="release tag the PDFs were uploaded to")
    parser.add_argument("--locale-scope-js", required=True, type=Path)
    parser.add_argument("--mkdocs-yml", default=REPO_ROOT / "mkdocs.yml", type=Path)
    args = parser.parse_args()

    base_url = f"https://github.com/{repo_slug(args.mkdocs_yml)}/releases/download/{args.tag}/"

    text = args.locale_scope_js.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        raise SystemExit(
            f"{args.locale_scope_js}: expected placeholder {PLACEHOLDER!r} not found "
            "(already patched, or docs/javascripts/locale-scope.js changed?)"
        )
    text = text.replace(PLACEHOLDER, f'/*__PDF_BASE_URL__*/ "{base_url}"')
    args.locale_scope_js.write_text(text, encoding="utf-8")
    print(f"patched {args.locale_scope_js}: PDF base URL -> {base_url}")


if __name__ == "__main__":
    main()
