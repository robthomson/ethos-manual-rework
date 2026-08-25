r"""Renders one combined PDF manual per locale opted into the LaTeX pipeline
(see hooks/_locales.py's PDF_LATEX_LOCALES/pdf_build_method() -- French,
initially) by concatenating that locale's markdown source in nav order and
running it through pandoc + xelatex: a typeset, book-style PDF (KOMA-Script
`scrreprt`, numbered chapters/sections, its own TOC, running headers/footers
from LaTeX itself) rather than scripts/build_pdfs.py's
screenshot-a-rendered-browser-page approach.

Modelled on C:\GitHub\ethos-manual's french/forge/pdf.py -- the predecessor
repo's own French-only LaTeX pipeline (concatenate SUMMARY.md-ordered
markdown into one book.md, `pandoc ... --pdf-engine xelatex`). This is the
same idea generalized to read nav order from mkdocs.yml (via scripts/_nav.py,
shared with build_pdfs.py) instead of a gitbook SUMMARY.md, and to
pre-process the mkdocs-material admonition syntax (`!!! note "..."`) this
repo's content actually uses, which the old repo's plain-markdown content
never needed to.

Unlike build_pdfs.py, this reads markdown *source* straight out of the repo
checkout (docs/<locale>/**/*.md) rather than an already-built site -- no
mkdocs build, no local HTTP server, no headless browser -- so it can run as
its own, independent, earlier CI step. It writes into the same --out-dir with
the same ethos-manual-<version>-<locale>.pdf naming as build_pdfs.py, so
deploy.yml's release-upload step (a `pdf-dist/*.pdf` glob) picks up either
pipeline's output without needing to know which one built it.

Same coverage bar as build_pdfs.py: only *fully covered* locales (every
English page present, see hooks/_locales.py's fully_covered_locales()) that
are also in PDF_LATEX_LOCALES get built. A locale can sit in
PDF_LATEX_LOCALES ahead of reaching full coverage -- it just won't produce a
PDF yet, same as any locale would under the Playwright pipeline. Pass
--include-partial to build one anyway (missing pages are skipped with a
warning, not fatal) -- for exercising the pandoc/xelatex toolchain itself
against a locale's real content before it reaches full coverage.
deploy.yml's real build step never passes this.

Requires the `pandoc` and `xelatex` binaries on PATH (see
.github/workflows/deploy.yml for the apt packages that provide them) --
that's not a Python dependency, so nothing in requirements.txt covers it.

Usage:
    python scripts/build_pdf_latex.py --out-dir pdf-dist --version 26.1
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "hooks"))
from _locales import fully_covered_locales, list_locales, pdf_build_method  # noqa: E402
from _nav import (  # noqa: E402
    load_mkdocs_config,
    localize_sections,
    locale_names,
    nav_sections,
    nav_translations_for,
)

LUA_FILTER = Path(__file__).resolve().parent / "pdf_latex" / "admonitions.lua"

# mkdocs-material admonition types actually used under docs/ (verified by
# grep across docs/fr; scripts/pdf_latex/admonitions.lua has one colored box
# per entry here). Add to both together if a locale's content grows a new
# type pandoc should style rather than leave as an unstyled fenced Div.
ADMONITION_TYPES = {"note", "tip", "warning", "danger", "example"}

FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
ADMONITION_START_RE = re.compile(r'^!!! (\w+)(?:\s+"([^"]*)")?\s*$')
HEADING_RE = re.compile(r"^(#{1,6})(\s)")
HEADING_ATTR_RE = re.compile(r"^(#{1,6}\s.*?)\s*\{:\s*(.*?)\s*\}\s*$")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
IMAGE_RE = re.compile(r'(!\[[^\]]*\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")


def pdf_filename(version: str, locale: str) -> str:
    return f"ethos-manual-{version}-{locale}.pdf"


def strip_front_matter(text: str) -> str:
    """Drop a page's own `---\\n...\\n---\\n` block (e.g. `translated_from:
    <sha>`) -- only the merged book's own single metadata block, built by
    book_metadata() below, should survive into book.md."""
    return FRONT_MATTER_RE.sub("", text, count=1)


def _walk_lines_tracking_fences(text: str):
    """Yields (line, in_fence) for every line of `text`, `in_fence` true for
    lines *inside* a ``` or ~~~ fenced block (including its own fence
    lines) -- shared by shift_headings() and convert_admonitions() so
    neither one rewrites content inside a code fence."""
    in_fence = False
    fence_marker = None
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)[0]
            was_in_fence = in_fence
            if not in_fence:
                in_fence, fence_marker = True, marker
            elif marker == fence_marker:
                in_fence, fence_marker = False, None
            yield line, was_in_fence or in_fence
            continue
        yield line, in_fence


def shift_headings(text: str, delta: int) -> str:
    """Add `delta` '#'s to every ATX heading (# .. ######), skipping fenced
    code blocks -- used to demote every page but a nav section's landing
    page by one level, so the section becomes a \\chapter and its pages
    become \\sections within it instead of a flat stack of equally-weighted
    chapters (see nav_sections()'s docstring for the landing-page
    convention this relies on)."""
    if delta == 0:
        return text
    out = []
    for line, in_fence in _walk_lines_tracking_fences(text):
        if not in_fence and HEADING_RE.match(line):
            line = ("#" * delta) + line
        out.append(line)
    return "\n".join(out) + "\n"


def convert_heading_attrs(text: str) -> str:
    """mkdocs/python-markdown's `attr_list` heading-ID syntax
    (`## Heading {: #some-id }` -- used across docs/fr wherever a page's
    English original has other pages linking to it by anchor, see
    docs/en/contributing/index.md's `attr_list` guidance) isn't pandoc
    markdown syntax; left alone, pandoc's reader treats the whole
    `{: #some-id }` as literal heading text, so it leaks into the printed
    heading itself and the TOC. Pandoc's own heading-attribute syntax is
    the same idea without the leading colon (`## Heading {#some-id}`), so
    this just reshapes one into the other. Skips fenced code blocks, since
    docs/en/contributing/index.md itself shows this exact syntax as a
    `markdown` code sample, which must stay literal.
    """
    out = []
    for line, in_fence in _walk_lines_tracking_fences(text):
        if not in_fence:
            match = HEADING_ATTR_RE.match(line)
            if match:
                line = f"{match.group(1)} {{{match.group(2)}}}"
        out.append(line)
    return "\n".join(out) + "\n"


def rewrite_image_paths(text: str, source_file: Path) -> str:
    """Resolve every relative image path against `source_file`'s own
    directory, replacing it with an absolute filesystem path. Makes the
    merged book.md's image references correct regardless of which
    directory depth each page's source file lives at, or what pandoc's own
    working directory happens to be -- no need to track/replicate mkdocs'
    own relative-path conventions here."""

    def replace(match: re.Match) -> str:
        prefix, target, suffix = match.groups()
        if URL_RE.match(target):
            return match.group(0)  # remote image -- leave alone
        resolved = (source_file.parent / target).resolve()
        return f"{prefix}{resolved.as_posix()}{suffix}"

    return IMAGE_RE.sub(replace, text)


def defuse_missing_images(text: str) -> tuple[str, list[str]]:
    """Replaces any `![alt](path)` whose target (already rewritten to an
    absolute path by rewrite_image_paths()) doesn't exist on disk with a
    plain inline `*(missing image: <filename>)*` marker, and returns the
    list of missing paths found.

    Unlike the Playwright pipeline -- where a missing image just quietly
    becomes a broken-image icon in the browser -- xelatex treats a missing
    `\\includegraphics` target as a fatal compile error that would abort
    this locale's *entire* merged document (see build_book_body()'s
    docstring). Substituting a visible marker keeps that one page's problem
    from taking down the whole manual, while still surfacing it -- both
    right there in the rendered PDF, and via a loud build-log warning (see
    build_book_body()) -- rather than silently disappearing the way it did
    under the old pipeline. Kept as an inline marker rather than a block
    (e.g. one of scripts/pdf_latex/admonitions.lua's boxes) so it's valid
    regardless of whether the original image sat on its own line or
    mid-paragraph.
    """
    missing: list[str] = []

    def replace(match: re.Match) -> str:
        _prefix, target, _suffix = match.groups()
        if URL_RE.match(target) or Path(target).exists():
            return match.group(0)
        missing.append(target)
        return f"*(missing image: {Path(target).name})*"

    return IMAGE_RE.sub(replace, text), missing


def convert_admonitions(text: str) -> str:
    """mkdocs-material's `!!! type "title"` blocks (body indented 4 spaces)
    -> pandoc fenced Divs (`::: {.type}` / `:::`) with an optional bold
    title paragraph. Pandoc's own markdown reader has no idea what `!!!`
    means, so this has to happen before pandoc ever sees the text;
    scripts/pdf_latex/admonitions.lua turns the resulting Divs into colored
    boxes at pandoc-render time.

    Unrecognized admonition types (not in ADMONITION_TYPES) are left
    untouched -- they'll render as a literal `!!! foo` paragraph, same as
    an unhandled type would look wrong either way, but at least visibly so
    rather than silently mis-boxed.
    """
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    fence_flags = dict(enumerate(f for _, f in _walk_lines_tracking_fences(text)))
    while i < len(lines):
        line = lines[i]
        match = None if fence_flags[i] else ADMONITION_START_RE.match(line)
        kind = match.group(1) if match else None
        if not match or kind not in ADMONITION_TYPES:
            out.append(line)
            i += 1
            continue
        title = match.group(2)
        i += 1
        body: list[str] = []
        while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
            body.append(lines[i][4:] if lines[i].startswith("    ") else lines[i])
            i += 1
        while body and not body[-1].strip():
            body.pop()
        out.append(f"::: {{.{kind}}}")
        if title:
            out.append(f"**{title}**")
            out.append("")
        out.extend(body)
        out.append(":::")
        out.append("")
    return "\n".join(out) + "\n"


def preprocess_page(source_file: Path) -> tuple[str, list[str]]:
    text = source_file.read_text(encoding="utf-8")
    text = strip_front_matter(text)
    text = convert_heading_attrs(text)
    text = rewrite_image_paths(text, source_file)
    text, missing = defuse_missing_images(text)
    text = convert_admonitions(text)
    return text, missing


def build_book_body(locale: str, sections: list[dict], docs_dir: Path) -> tuple[str, int]:
    """Concatenates every page in nav order into the book's body text, and
    returns how many missing-image markers defuse_missing_images() had to
    substitute along the way (0 in the common case) -- callers surface that
    count so a run that quietly patched over broken content doesn't look
    identical to a clean one.

    A page file itself not existing is only reachable via main()'s
    --include-partial (the normal fully_covered_locales() gate guarantees
    every page exists otherwise) -- skipped with a warning rather than
    raising, same defusing-not-crashing posture as a missing image.
    """
    locale_dir = docs_dir / locale
    parts: list[str] = []
    missing_count = 0
    for section in sections:
        for index, (_title, rel_path) in enumerate(section["pages"]):
            source_file = locale_dir / rel_path
            if not source_file.exists():
                print(
                    f"warning: {locale}/{rel_path} doesn't exist -- skipping "
                    "(--include-partial build)",
                    file=sys.stderr,
                )
                missing_count += 1
                continue
            text, missing = preprocess_page(source_file)
            if index > 0:  # not this section's landing page -- see shift_headings()
                text = shift_headings(text, delta=1)
            for image_path in missing:
                print(
                    f"warning: {locale}/{rel_path} references missing image "
                    f"{image_path} -- substituting a placeholder note",
                    file=sys.stderr,
                )
            missing_count += len(missing)
            parts.append(text.strip("\n"))
    return "\n\n".join(parts) + "\n", missing_count


# Colors are defined via \definecolor(...){HTML}{...} in book_metadata()'s
# header-includes rather than named xcolor colors (e.g. dvipsnames'
# "MidnightBlue") -- named-color sets depend on *which* options xcolor gets
# loaded with, which pandoc's own template also touches (for colorlinks),
# and a second \usepackage{xcolor} with mismatched options is a hard LaTeX
# "Option clash" error. Defining our own named colors sidesteps that
# entirely: they only ever need bare, no-option `\usepackage{xcolor}`.
ADMONITION_COLORS = {
    "note": "1F6FEB",
    "tip": "1A7F37",
    "warning": "9A6700",
    "danger": "CF222E",
    "example": "57606A",
}

# Fallback fonts for Unicode blocks "Noto Sans" (the mainfont) doesn't
# cover, keyed by the \newfontfamily command name book_metadata()'s
# header-includes binds each one to. See that function's docstring for how
# these were chosen (empirically, by actually running xelatex) and why
# each one is wrapped in \IfFontExistsTF rather than assumed present.
FALLBACK_FONTS = {
    "admonSymbolFont": "DejaVu Sans",  # Arrows, MathematicalOperators (e.g. →, −)
    "admonHebrewFont": "Noto Sans Hebrew",
    "admonCJKFont": "Noto Sans CJK SC",
}


def book_metadata(locale: str, display_name: str, version: str, generated: str) -> str:
    """The merged book's own single pandoc YAML metadata block -- title,
    KOMA-Script/font/TOC settings, and header-includes wiring in tcolorbox
    for scripts/pdf_latex/admonitions.lua's boxes and forcing figures to
    stay put (`[H]`) rather than float away from the text referencing them.
    Adapted from C:\\GitHub\\ethos-manual's french/styles.md, dropping what
    doesn't apply here (no CSL/bibliography -- nothing in this manual cites
    sources; no `links-as-notes` -- this content is link-dense with internal
    cross-references, and turning every one into a footnote showing a bare,
    inert `../foo.md` target would be actively worse here than the
    underlined-link default).

    "Noto Sans" alone doesn't cover every glyph docs/fr's real content
    actually uses -- menu-navigation notation ("Système → Info") and a
    signed voltage figure use → and − throughout, and
    system-setup/general.md's list of the radio firmware's own menu
    languages spells a couple of them natively (中文, עברית). xelatex
    doesn't error on an unsupported glyph, it just silently drops it from
    the page -- a worse failure mode than an error, and only found by
    actually running this script's output through xelatex and reading the
    "Missing character" warnings.

    Pandoc's `mainfontfallback` metadata field looked like the built-in fix
    (per-font per-project fallback lists), but empirically does nothing
    with this pandoc version's default LaTeX template (verified via
    `pandoc --to latex` on a real book.md -- no fallback code appears in
    the output at all). fontspec itself has no automatic-fallback feature
    for xelatex either (that's a lualatex-only luaotfload feature). What
    actually works, tested directly against this exact set of characters:
    the `ucharclasses` header-includes below, switching font by Unicode
    block for the handful of ranges that need it and leaving everything
    else on the mainfont. DejaVu Sans (not a Noto face) covers the Arrows
    and MathematicalOperators blocks that "Noto Sans Symbols"/"Symbols2"
    turned out, on testing, *not* to actually include despite the name.

    Each fallback font is wrapped in `\\IfFontExistsTF` (falling back to
    plain `mainfont` if not found) rather than an unconditional
    `\\newfontfamily`, which errors out fatally -- aborting the whole
    document, the exact failure mode this whole function exists to avoid --
    if the named font isn't installed. "Noto Sans CJK SC" specifically
    couldn't be verified locally (this repo's own dev sandbox has no CJK
    font installed at all); it's guarded for that reason, even though
    deploy.yml's apt install list does include fonts-noto-cjk.
    """
    color_defs = "\n  ".join(
        f"\\definecolor{{admon{kind.capitalize()}}}{{HTML}}{{{hex_}}}"
        for kind, hex_ in ADMONITION_COLORS.items()
    )
    fallback_font_defs = "\n  ".join(
        f"\\IfFontExistsTF{{{font}}}{{\\newfontfamily\\{cmd}{{{font}}}}}"
        f"{{\\newfontfamily\\{cmd}{{Noto Sans}}}}"
        for cmd, font in FALLBACK_FONTS.items()
    )
    return f"""---
title: "Ethos Manual"
subtitle: "{display_name}"
lang: {locale}
date: "{generated}"
papersize: a4
documentclass: scrreprt
documentoptions: twoside
fontsize: 10pt
mainfont: "Noto Sans"
colorlinks: true
linkcolor: blue
citecolor: blue
urlcolor: blue
toc: true
toc-depth: 2
numbersections: true
header-includes:
- |
  \\usepackage{{xcolor}}
  {color_defs}
  \\usepackage[most]{{tcolorbox}}
  \\usepackage{{graphicx}}
  \\setkeys{{Gin}}{{width=\\linewidth,keepaspectratio}}
  \\usepackage{{float}}
  \\let\\origfigure\\figure
  \\let\\endorigfigure\\endfigure
  \\renewenvironment{{figure}}[1][2]{{\\expandafter\\origfigure\\expandafter[H]}}{{\\endorigfigure}}
  \\usepackage{{ucharclasses}}
  {fallback_font_defs}
  \\setTransitionsFor{{Arrows}}{{\\admonSymbolFont}}{{\\normalfont}}
  \\setTransitionsFor{{MathematicalOperators}}{{\\admonSymbolFont}}{{\\normalfont}}
  \\setTransitionsFor{{Hebrew}}{{\\admonHebrewFont}}{{\\normalfont}}
  \\setTransitionsFor{{CJKUnifiedIdeographs}}{{\\admonCJKFont}}{{\\normalfont}}
---

"""


def build_locale_pdf(
    locale: str,
    display_name: str,
    sections: list[dict],
    docs_dir: Path,
    out_path: Path,
    version: str,
    generated: str,
    debug_dir: Path | None = None,
) -> int:
    """Returns the missing-image count from build_book_body() -- 0 in the
    common case -- so main() can print a build-wide summary.

    pandoc's own xelatex errors already surface directly in the caller's
    terminal/CI log (subprocess.run() below doesn't capture that
    subprocess's stdout/stderr, so they just inherit through); `debug_dir`,
    if given, additionally saves the exact merged markdown pandoc was fed as
    book-<locale>.md -- not written by default since it's only useful when
    something's actually gone wrong.
    """
    body, missing_count = build_book_body(locale, sections, docs_dir)
    book = book_metadata(locale, display_name, version, generated) + body
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if debug_dir is not None:
        debug_dir.mkdir(parents=True, exist_ok=True)
        (debug_dir / f"book-{locale}.md").write_text(book, encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="ethos-pdf-latex-") as tmp:
        book_path = Path(tmp) / "book.md"
        book_path.write_text(book, encoding="utf-8")
        subprocess.run(
            [
                "pandoc",
                str(book_path),
                "--standalone",
                "--from",
                "markdown+smart",
                "--to",
                "pdf",
                "--pdf-engine",
                "xelatex",
                "--lua-filter",
                str(LUA_FILTER),
                "--output",
                str(out_path),
            ],
            check=True,
        )
    suffix = f" ({missing_count} missing image(s) substituted)" if missing_count else ""
    print(f"wrote {out_path}{suffix}")
    return missing_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--docs-dir", default=REPO_ROOT / "docs", type=Path, help="mkdocs docs_dir (source markdown)"
    )
    parser.add_argument(
        "--out-dir",
        required=True,
        type=Path,
        help="directory to write ethos-manual-<version>-<locale>.pdf into",
    )
    parser.add_argument("--mkdocs-yml", default=REPO_ROOT / "mkdocs.yml", type=Path)
    parser.add_argument(
        "--version", default="dev", help="shown on the title page and in each output filename"
    )
    parser.add_argument(
        "--include-partial",
        action="store_true",
        help=(
            "also build LaTeX-pipeline locales that aren't fully covered yet -- missing pages "
            "are skipped with a warning rather than fatal (see build_book_body()). For testing "
            "the pandoc/xelatex toolchain itself; deploy.yml's real build never passes this."
        ),
    )
    parser.add_argument(
        "--debug-dir",
        type=Path,
        default=None,
        help="also save each locale's merged book-<locale>.md here (see build_locale_pdf())",
    )
    args = parser.parse_args()

    config = load_mkdocs_config(args.mkdocs_yml)
    sections = nav_sections(config, args.docs_dir)
    names = locale_names(config)
    generated = date.today().isoformat()

    candidate_locales = (
        list_locales(args.docs_dir) if args.include_partial else fully_covered_locales(args.docs_dir)
    )
    locales = [loc for loc in candidate_locales if pdf_build_method(loc) == "latex"]
    if not locales:
        print("no locale on the LaTeX pipeline is eligible to build -- nothing to build")
        return

    total_missing = 0
    for locale in locales:
        locale_sections = localize_sections(sections, nav_translations_for(config, locale))
        total_missing += build_locale_pdf(
            locale,
            names.get(locale, locale),
            locale_sections,
            args.docs_dir,
            args.out_dir / pdf_filename(args.version, locale),
            args.version,
            generated,
            debug_dir=args.debug_dir,
        )

    # Missing images don't fail the build (see defuse_missing_images()'s
    # docstring) but shouldn't be easy to miss either -- one last loud line
    # after a successful run, on top of each locale's own per-page warnings
    # above, in case CI log output only gets skimmed for the final status.
    if total_missing:
        print(
            f"warning: {total_missing} missing image(s) were substituted with placeholder "
            "notes across the locale(s) above -- see the warnings for which ones",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
