#!/usr/bin/env python3
"""
Revise an existing AI translation against a real human-translated
reference text, for the pages where one exists.

Different from translate.py's "translate fresh from English" mode: this
takes our CURRENT AI translation plus the CURRENT English source plus a
genuine human-written reference (older FrSky-authored GitBook content,
or eventually PDF-extracted text) and asks Claude to revise the AI
translation toward the human's terminology, phrasing, and natural style
-- while still fully covering everything in the current English source,
since the human reference may be from an older firmware version and
may not mention newer sections/features.

This is a LOCAL, standalone tool -- not part of the site build or CI.
Never commits or pushes; only writes docs/<locale>/<path>, same as if
you'd hand-edited it. Review the diff before committing.

Usage:
    python scripts/revise_from_reference.py --locale fr --dry-run
    python scripts/revise_from_reference.py --locale fr --yes
    python scripts/revise_from_reference.py --locale fr --pages model-setup/mixes.md
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
EN_DIR = DOCS_DIR / "en"
DEFAULT_MODEL = "claude-opus-5"

# Old-repo location, sibling checkout of https://github.com/FrSkyRC/ethos-manual
OLD_REPO = REPO_ROOT.parent / "ethos-manual"

# locale -> {new_relpath: [old-repo-relative reference file(s), concatenated in order]}
# Only pages with a real human-written match are listed; everything else in
# docs/<locale>/ keeps its current AI translation untouched.
REFERENCE_MAP: dict[str, dict[str, list[str]]] = {
    "fr": {
        "index.md": ["french/README.md"],
        "getting-started/main-views.md": ["french/vues-principales.md"],
        "getting-started/user-interface-and-navigation.md": ["french/interface-utilisateur-et-navigation.md"],
        "getting-started/usb-connection-modes.md": ["french/les-differents-modes-de-connexion-usb.md"],
        "system-setup/index.md": ["french/configuration-du-systeme/README.md"],
        "system-setup/file-manager.md": ["french/configuration-du-systeme/gestionnaire-de-fichiers.md"],
        "system-setup/alerts.md": ["french/configuration-du-systeme/alertes.md"],
        "system-setup/date-and-time.md": ["french/configuration-du-systeme/date-et-heure.md"],
        "system-setup/general.md": ["french/configuration-du-systeme/generalites.md"],
        "system-setup/battery.md": ["french/configuration-du-systeme/batterie.md"],
        "system-setup/hardware.md": ["french/configuration-du-systeme/materiel.md"],
        "system-setup/controls.md": ["french/configuration-du-systeme/manches.md"],
        "system-setup/devices.md": ["french/configuration-du-systeme/capteurs.md"],
        "system-setup/information.md": ["french/configuration-du-systeme/information.md"],
        "model-setup/index.md": ["french/configuration-du-modele/README.md"],
        "model-setup/model-select.md": ["french/configuration-du-modele/choix-modele.md"],
        "model-setup/model-edit.md": ["french/configuration-du-modele/edition-modele.md"],
        "model-setup/flight-modes.md": ["french/configuration-du-modele/phases-de-vol.md"],
        "model-setup/mixes.md": ["french/configuration-du-modele/mixages.md"],
        "model-setup/outputs.md": ["french/configuration-du-modele/sorties.md"],
        "model-setup/timers.md": ["french/configuration-du-modele/chronos.md"],
        "model-setup/trims.md": ["french/configuration-du-modele/trims.md"],
        "displays/index.md": [
            "french/configurer-les-ecrans/README.md",
            "french/configurer-les-ecrans/configuration-ecran-principal.md",
        ],
        "displays/additional-displays.md": ["french/configurer-les-ecrans/ajout-ecrans-supplementaires.md"],
        "displays/custom-widgets.md": ["french/configurer-les-ecrans/ajout-widgets-personnalises.md"],
        "lua-scripts/index.md": ["french/lua-scripts/README.md"],
        "lua-scripts/lua-interpreter.md": ["french/lua-scripts/interprete-lua-ethos.md"],
        "lua-scripts/ethos-lua-documentation.md": ["french/lua-scripts/documentation-ethos-lua.md"],
        "lua-scripts/example-script-locations.md": ["french/lua-scripts/emplacement-fichiers-scripts-exemple-lua.md"],
        "lua-scripts/configuration-limits.md": ["french/lua-scripts/limite-configuration-scripts-lua.md"],
        "lua-scripts/basic-widget-layout.md": ["french/lua-scripts/mise-en-page-de-base-widget-lua.md"],
        "ethos-suite/index.md": ["french/ethos-suite/README.md", "french/ethos-suite/apercu.md"],
        "ethos-suite/migration.md": ["french/ethos-suite/procedure-migration-vers-ethos-suite.md"],
        "ethos-suite/operation.md": [
            "french/ethos-suite/operation/README.md",
            "french/ethos-suite/operation/section-accueil.md",
            "french/ethos-suite/operation/section-radio.md",
            "french/ethos-suite/operation/section-outils.md",
            "french/ethos-suite/operation/section-autres.md",
        ],
        "tutorials/initial-radio-setup.md": [
            "french/Tutoriels-de-programmation/Exemple-de-configuration-radio-initiale/README.md",
            "french/Tutoriels-de-programmation/Exemple-de-configuration-radio-initiale/Exemple-de-configuration-radio-initiale.md",
            "french/Tutoriels-de-programmation/Exemple-de-configuration-radio-initiale/Etape-1-Chargez-la-radio-et-les-batteries-de-vol.md",
            "french/Tutoriels-de-programmation/Exemple-de-configuration-radio-initiale/Etape-2-Calibrez-le-materiel.md",
            "french/Tutoriels-de-programmation/Exemple-de-configuration-radio-initiale/Etape-3-Effectuez-la-configuration-du-systeme-radio.md",
        ],
        "tutorials/basic-fixed-wing.md": [
            f"french/Tutoriels-de-programmation/Exemple-d-avion-a-voilure-fixe-de-base/{f}"
            for f in [
                "Exemple-d-avion-a-voilure-fixe-de-base.md",
                "Etape-1-Confirmez-les-parametres-du-systeme.md",
                "Etape-2-Identifier-les-servos-voies-requis.md",
                "Etape-3-Creez-un-nouveau-modele.md",
                "Etape-4-Examiner-et-configurer-les-mixages.md",
                "Etape-5-Appairer-le-recepteur.md",
                "Etape-6-Configurer-les-sorties.md",
                "Etape-7-Introduction-aux-modes-de-vol.md",
                "Etape-8-Configurer-une-chrono-de-vol-pour-la-batterie.md",
                "Etape-9-Ajouter-un-mixage-pour-les-retractations.md",
            ]
        ],
        "tutorials/basic-flying-wing.md": [
            f"french/Tutoriels-de-programmation/Exemple-d-aile-volante-basique-Elevon/{f}"
            for f in [
                "Exemple-d-aile-volante-basique-Elevon.md",
                "Etape-1-Confirmer-les-parametres-du-systeme.md",
                "Etape-2-Identifier-les-servos-voies-requis.md",
                "Etape-3-Creez-un-nouveau-modele.md",
                "Etape-4-Examiner-et-configurer-les-mixages.md",
                "Etape-5-Lier-le-recepteur.md",
                "Etape-6-Revoir-les-mixages.md",
                "Etape-7-Configurer-les-courses-maximales-des-servos.md",
            ]
        ],
        "tutorials/basic-flybarless-heli.md": [
            f"french/Tutoriels-de-programmation/Exemple-d-helicoptere-flybarless-basique/{f}"
            for f in [
                "Exemple-d-helicoptere-flybarless-basique.md",
                "Etape-1-Confirmer-les-parametres-du-système.md",
                "Etape-2-Identifier-les-servos-voies-requis.md",
                "Etape-3-Creez-un-nouveau-modele.md",
                "Etape-4-Examiner-et-configurer-les-mixages.md",
                "Etape-5-Configuration-FBL.md",
            ]
        ],
        "how-to/low-battery-warning.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/1-Comment-configurer-un-avertissement-de-tension-de-batterie-faible.md"
        ],
        "how-to/battery-capacity-warning.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/2-Comment-configurer-un-avertissement-de-capacite-de-batterie-à-l'aide-d'un-ESC-Neuron.md",
            "french/Tutoriels-de-programmation/Section-Comment-faire/3-Comment-configurer-un-avertissement-de-capacite-de-batterie-à-l'aide-d'un-capteur-calcule.md",
        ],
        "how-to/sr8-sr10-setup.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/4-Comment-creer-un-modèle-pour-SR8-SR10.md",
            "french/Tutoriels-de-programmation/Section-Comment-faire/5-Comment-reorganiser-les-voies-par-exemple-pour-SR8-SR10.md",
        ],
        "how-to/butterfly-mixer.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/6-Comment-configurer-un-mixage-Butterfly-alias-Crocodile.md"
        ],
        "how-to/fbus-setup.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/7-Comment-configurer-un-systeme-FBUS.md"
        ],
        "how-to/test-redundant-receiver.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/8-Comment-tester-la-configuration-d'un-recepteur-redondant.md"
        ],
        "how-to/user-defined-checklist.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/9-Comment-mettre-en-place-une-liste-de-controle-de-texte-definie-par-l-utilisateur.md"
        ],
        "how-to/in-flight-compensation-curve.md": [
            "french/Tutoriels-de-programmation/Section-Comment-faire/10-Comment-configurer-une-courbe-de-compensation-des-volets-reglable-en-vol.md"
        ],
    },
}

SYSTEM_PROMPT_TEMPLATE = """You are revising an existing machine-translated {locale_name} page for the Ethos radio manual using a REAL, human-written {locale_name} reference text as a quality/terminology guide.

Context: the reference text is genuine {locale_name} prose written by FrSky's own translation team for an earlier version of this manual (possibly an older firmware version). It may not be 100% current -- it can be missing features/sections that exist in the current English source, or describe UI slightly differently than the current version. Your job is a REVISION, not a replacement:

1. Read the CURRENT ENGLISH SOURCE first -- it defines what must be covered and is authoritative for accuracy/completeness.
2. Read the CURRENT {locale_name} AI TRANSLATION -- this is what you're revising.
3. Read the HUMAN REFERENCE TEXT -- adopt its terminology, phrasing, idiom, and natural {locale_name} style wherever it covers the same content as the current English source.
4. Produce a revised {locale_name} translation that:
   - Fully and accurately covers everything in the current English source (do not drop anything the AI translation had that the human reference doesn't mention -- the human reference is older/partial, not authoritative for coverage).
   - Uses the human reference's actual wording/terminology wherever the topics overlap, instead of the AI translation's original wording, when the human phrasing is natural and still accurate.
   - Falls back to revising the AI translation's own wording (improving naturalness where you can) for anything the human reference doesn't cover.

Hard rules -- do not violate these:

1. Output ONLY the revised Markdown body. No commentary, no preamble, no code fence wrapping the whole output.
2. Preserve the Markdown structure exactly: identical headings (same levels, same order, same count as the CURRENT ENGLISH SOURCE -- not the human reference, which may have different structure), identical list/table structure, identical paragraph breaks.
3. NEVER translate or alter, copy verbatim character-for-character:
   - Anchor IDs in attr_list syntax, e.g. `{{: #choosing-a-source }}` at the end of a heading.
   - URLs and relative file paths inside links and images, e.g. `(../assets/foo.png)` or `(../model-setup/mixes.md)`.
   - Anchor fragments in links, e.g. `#choosing-a-source` in `(../page.md#choosing-a-source)`.
   - Content inside fenced code blocks (``` ... ```).
   - These technical terms, brand names, and protocol names -- keep them exactly as written: {no_translate_terms}.
4. DO translate/revise: headings, paragraph text, list item text, table cell text, image alt text, admonition title text.
"""

# Same NO_TRANSLATE_TERMS as translate.py -- kept in sync manually since
# this is a separate, less-frequently-run tool.
NO_TRANSLATE_TERMS = (
    "ENT", "RTN", "PAGE", "MDL", "TELE", "DISP", "SYS",
    "FrSky", "Ethos", "Rotorflight", "Rotorflight LUA", "Ethos Suite",
    "X20S", "X20", "X20 PRO", "X20 PRO AW", "X18S", "X18", "X-Lite",
    "Horus", "Taranis",
    "ACCESS", "ACCST", "S.Port", "F.Port", "F.BUS", "SBUS", "CRSF",
    "ELRS", "ExpressLRS", "Multi-protocol", "MSP",
    "SD card", "USB", "Wi-Fi", "Bluetooth", "MicroSD",
    "Lua",
)

LOCALE_NAMES = {"fr": "French"}


def load_reference(locale: str, rel_path: str) -> str | None:
    files = REFERENCE_MAP.get(locale, {}).get(rel_path)
    if not files:
        return None
    parts = []
    for f in files:
        p = OLD_REPO / f
        if not p.exists():
            print(f"  WARNING: reference file missing: {p}")
            continue
        parts.append(p.read_text(encoding="utf-8"))
    return "\n\n---\n\n".join(parts) if parts else None


def _clean_output(text: str) -> str:
    text = text.strip()
    lines = text.split("\n")
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text + "\n"


def _strip_leading_frontmatter(text: str) -> str:
    """Remove a leading ---...--- block, if the model echoed one despite
    being told to output only the Markdown body."""
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        return text
    end = stripped.find("\n---", 3)
    if end == -1:
        return text
    return stripped[end + 4:].lstrip("\n")


def revise_page(client: anthropic.Anthropic, model: str, locale: str, rel_path: str,
                 en_text: str, current_translation: str, reference_text: str) -> str:
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        locale_name=LOCALE_NAMES.get(locale, locale),
        no_translate_terms=", ".join(NO_TRANSLATE_TERMS),
    )
    user_message = (
        "=== CURRENT ENGLISH SOURCE ===\n"
        f"{en_text}\n\n"
        "=== CURRENT AI TRANSLATION (to revise) ===\n"
        f"{current_translation}\n\n"
        "=== HUMAN REFERENCE TEXT (terminology/style guide, may be incomplete/older) ===\n"
        f"{reference_text}\n"
    )
    with client.messages.stream(
        model=model,
        max_tokens=16000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        message = stream.get_final_message()
    text = "".join(block.text for block in message.content if block.type == "text")
    return _clean_output(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Revise AI translations against real human reference text")
    ap.add_argument("--locale", required=True, choices=sorted(REFERENCE_MAP), help="Target locale")
    ap.add_argument("--pages", nargs="*", metavar="PATH", help="Limit to these pages")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args(argv)

    if not OLD_REPO.exists():
        raise SystemExit(f"ERROR: old repo not found at {OLD_REPO} (expected a sibling checkout)")

    mapping = REFERENCE_MAP[args.locale]
    pages = args.pages if args.pages else sorted(mapping)
    unknown = [p for p in pages if p not in mapping]
    if unknown:
        raise SystemExit(f"ERROR: no reference mapped for: {', '.join(unknown)}")

    print(f"Revising {len(pages)} {args.locale} page(s) against human reference text (model: {args.model})\n")
    for p in pages:
        files = mapping[p]
        print(f"  {p}  <-  {', '.join(files)}")

    if args.dry_run:
        print("\nDry run -- no API calls made, no files written.")
        return 0

    if not args.yes:
        answer = input(f"\nRevise {len(pages)} page(s) with {args.model}? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted.")
            return 0

    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    revised = 0
    failed: list[str] = []
    for i, rel_path in enumerate(pages, 1):
        print(f"[{i}/{len(pages)}] {args.locale}/{rel_path}...", end=" ", flush=True)
        en_path = EN_DIR / rel_path
        fr_path = DOCS_DIR / args.locale / rel_path
        if not en_path.exists() or not fr_path.exists():
            print("SKIP (missing en or current translation)")
            continue
        reference_text = load_reference(args.locale, rel_path)
        if not reference_text:
            print("SKIP (no reference text)")
            continue
        en_text = en_path.read_text(encoding="utf-8")
        current_translation = fr_path.read_text(encoding="utf-8")
        try:
            revised_text = revise_page(client, args.model, args.locale, rel_path, en_text, current_translation, reference_text)
        except anthropic.APIError as exc:
            print(f"FAILED: {exc}")
            failed.append(rel_path)
            time.sleep(2)
            continue

        # Preserve the existing translated_from frontmatter -- the English
        # source hasn't changed, only translation quality has.
        existing = current_translation
        if existing.startswith("---"):
            end = existing.find("\n---", 3)
            frontmatter = existing[: end + 4] if end != -1 else ""
        else:
            frontmatter = ""
        # Claude's output sometimes echoes a frontmatter-like block despite
        # being told to output only the Markdown body (it saw one in the
        # "current translation" it was revising) -- strip any leading
        # ---...--- block from its output before prepending our own, or
        # the file ends up with the same translated_from block twice.
        revised_text = _strip_leading_frontmatter(revised_text)
        fr_path.write_text(f"{frontmatter}\n\n{revised_text}" if frontmatter else revised_text, encoding="utf-8")
        print("done")
        revised += 1

    print(f"\nDone: {revised} revised, {len(failed)} failed.")
    if failed:
        print("Failed pages (re-run to retry):")
        for f in failed:
            print(f"  {f}")
    print("\nNothing was committed. Review the diff (`git diff docs/`), then commit/PR as usual.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
