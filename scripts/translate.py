#!/usr/bin/env python3
"""
Auto-translate Ethos manual pages using the Claude API.

For each configured locale (from mkdocs.yml's i18n plugin), finds English
pages under docs/en/ that are missing or stale in that locale (same
missing/stale/current logic as hooks/i18n_status.py, which drives
docs/en/contributing/translation-status.md), translates them with Claude,
and writes docs/<locale>/<same path> stamped with the English commit sha it
was translated from.

This is a LOCAL, standalone tool -- not part of the site build or CI. You
run it yourself, review the diff, then commit/PR like any other change (see
docs/en/contributing/index.md -> Translation plan). It never commits or
pushes anything itself.

Usage:
    python scripts/translate.py                      # all configured locales, all missing/stale pages
    python scripts/translate.py --only fr             # just French
    python scripts/translate.py --only fr de          # French and German
    python scripts/translate.py --pages model-setup/mixes.md   # just this page (any/all target locales)
    python scripts/translate.py --dry-run             # list what would be translated, no API calls
    python scripts/translate.py --force               # retranslate already-current pages too
    python scripts/translate.py --limit 5             # cap how many pages get translated this run
    python scripts/translate.py --model claude-sonnet-5  # cheaper/faster than the default Opus

Requires: pip install anthropic pyyaml
Environment: ANTHROPIC_API_KEY must be set (or an `ant auth login` profile).
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
import time
from pathlib import Path

# Locale names/glossaries include non-Latin scripts (e.g. Chinese) that
# don't exist in the Windows console's default codepage (cp1252) --
# without this, printing them crashes with UnicodeEncodeError partway
# through a run. Safe on non-Windows too (reconfigure is a no-op there
# since stdout is already UTF-8).
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
EN_DIR = DOCS_DIR / "en"
DEFAULT_MODEL = "claude-opus-5"
STATUS_FILENAME = "translation-status.md"

# hooks/i18n_status.py already implements git-last-commit lookup and
# frontmatter parsing for the exact same missing/stale/current logic that
# drives docs/en/contributing/translation-status.md. Reuse it rather than
# maintaining a second copy that could drift out of sync.
_spec = importlib.util.spec_from_file_location(
    "i18n_status", REPO_ROOT / "hooks" / "i18n_status.py"
)
_i18n_status = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_i18n_status)
_git_last_commit = _i18n_status._git_last_commit
_read_frontmatter = _i18n_status._read_frontmatter

# Terms that must never be translated -- keep exactly as printed on the
# radio / in the firmware, in every language. Mirrors the same technique
# (and much of the same vocabulary) as the sister project's
# rotorflight-lua-ethos-suite/bin/i18n/auto-translate.py, adapted for the
# Ethos radio manual rather than Rotorflight flight-controller firmware.
NO_TRANSLATE_TERMS = (
    # Physical keys / buttons printed on the radio
    "ENT", "RTN", "PAGE", "MDL", "TELE", "DISP", "SYS",
    # Brands / products
    "FrSky", "Ethos", "Rotorflight", "Rotorflight LUA", "Ethos Suite",
    "X20S", "X20", "X20 PRO", "X20 PRO AW", "X18S", "X18", "X-Lite",
    "Horus", "Taranis",
    # Protocols / radio-link technology
    "ACCESS", "ACCST", "S.Port", "F.Port", "F.BUS", "SBUS", "CRSF",
    "ELRS", "ExpressLRS", "Multi-protocol", "MSP",
    # File / connectivity terms
    "SD card", "USB", "Wi-Fi", "Bluetooth", "MicroSD",
    # Scripting
    "Lua",
)

SYSTEM_PROMPT_TEMPLATE = """You are a professional technical translator producing {locale_name} documentation for the Ethos radio manual -- the user manual for FrSky's Ethos firmware, which runs on FrSky radio transmitters (X20S, X20 PRO, X18S and similar) used for RC (radio control) model aircraft, helicopters, and drones.

Translate the given English Markdown page into natural, technically precise {locale_name}, matching the register of professional {locale_name} RC-hobbyist documentation (accurate terminology, formal register, no marketing fluff).

Hard rules -- do not violate these:

1. Output ONLY the translated Markdown body. No commentary, no preamble, no code fence wrapping the whole output.
2. Preserve the Markdown structure exactly: identical headings (same levels, same order, same count), identical list/table structure, identical paragraph breaks.
3. NEVER translate or alter, copy verbatim character-for-character:
   - Anchor IDs in attr_list syntax, e.g. `{{: #choosing-a-source }}` at the end of a heading.
   - URLs and relative file paths inside links and images, e.g. `(../assets/foo.png)` or `(../model-setup/mixes.md)` -- translate only the link text / image alt text, never the path.
   - Anchor fragments in links, e.g. `#choosing-a-source` in `(../page.md#choosing-a-source)`.
   - Content inside fenced code blocks (``` ... ```), including any comments inside -- copy verbatim.
   - Inline code spans that name physical keys, protocols, or file/variable names (backtick-quoted).
   - Admonition type keywords -- the word immediately after `!!!` (e.g. `note`, `warning`, `danger`, `tip`, `example`) stays in English exactly as-is; only translate the quoted title text that follows it.
   - YAML frontmatter -- there is none in the input; do not add any (it is added separately after translation).
   - These technical terms, brand names, and protocol names -- keep them exactly as written, in every context: {no_translate_terms}.
4. DO translate: headings, paragraph text, list item text, table cell text, image alt text, admonition title text (the quoted string after the keyword).
5. Maintain terminology consistency using this glossary wherever the term applies (English -> {locale_name}):
{glossary_block}
"""

# Established terminology from the French pilot translation (see
# docs/fr/*.md and docs/en/contributing/index.md -> Translation plan).
# Locales without an entry here still translate correctly -- they just
# don't get a pre-seeded glossary, so terminology may vary until one is
# built the same way (translate a handful of pages, extract the terms that
# came out consistently, add them here).
GLOSSARIES: dict[str, str] = {
    "fr": """
- Getting Started -> Prise en main
- Model Setup -> Configuration du modèle
- System Setup -> Configuration du système
- Displays -> Écrans
- Tutorials -> Tutoriels
- How-To Guides -> Guides pratiques
- Lua Scripts -> Scripts Lua
- Radio Notes -> Notes sur les radios
- Home -> Accueil
- Model Select -> Choix du modèle
- Configure Screens -> Configurer les écrans
- Checklist -> Liste de vérification
- Ailerons -> Ailerons
- Elevator -> Profondeur
- Rudder -> Dérive
- Throttle -> Gaz
- Mix / Mixes -> Mixage / Mixages
- Free mix -> Mixage libre
- Outputs -> Sorties
- Timers -> Chronos
- Timer -> Chronomètre
- Trim / Trims -> Trim / Trims (kept)
- Flight mode -> Phase de vol
- Logical switch -> Interrupteur logique
- Special function -> Fonction spéciale
- Switch -> Interrupteur
- Source -> Source (kept)
- Sensor -> Capteur
- Receiver -> Récepteur
- Widget -> Widget (kept)
- Screen -> Écran
- Stick -> Manche
- Potentiometer / pot -> Potentiomètre
- Slider -> Curseur
- Channel -> Voie
- Differential -> Différentiel
- Throttle cut -> Coupure gaz
- Throttle hold -> Maintien gaz
- Idle -> Ralenti
""".strip(),
    "de": """
- Getting Started -> Erste Schritte
- Model Setup -> Modellkonfiguration
- System Setup -> Systemeinstellungen
- Displays -> Anzeigen
- Tutorials -> Tutorials (kept)
- How-To Guides -> Anleitungen
- Lua Scripts -> Lua-Skripte
- Radio Notes -> Senderhinweise
- Home -> Start
- Model Select -> Modellauswahl
- Configure Screens -> Bildschirme konfigurieren
- Checklist -> Checkliste
- Ailerons -> Querruder
- Elevator -> Höhenruder
- Rudder -> Seitenruder
- Throttle -> Gas
- Mix / Mixes -> Mischer / Mischungen
- Free mix -> Freier Mischer
- Outputs -> Ausgänge
- Timers -> Timer (kept)
- Trim / Trims -> Trimmung
- Flight mode -> Flugphase
- Logical switch -> Logischer Schalter
- Special function -> Sonderfunktion
- Switch -> Schalter
- Source -> Quelle
- Sensor -> Sensor (kept)
- Receiver -> Empfänger
- Widget -> Widget (kept)
- Screen -> Bildschirm
- Stick -> Steuerknüppel
- Potentiometer / pot -> Potentiometer
- Slider -> Schieberegler
- Channel -> Kanal
- Differential -> Differential (kept)
- Throttle cut -> Gas-Abschaltung
- Throttle hold -> Leerlaufsperre
- Idle -> Leerlauf
""".strip(),
    "es": """
- Getting Started -> Primeros pasos
- Model Setup -> Configuración del modelo
- System Setup -> Configuración del sistema
- Displays -> Pantallas
- Tutorials -> Tutoriales
- How-To Guides -> Guías prácticas
- Lua Scripts -> Scripts Lua
- Radio Notes -> Notas de la emisora
- Home -> Inicio
- Model Select -> Selección de modelo
- Configure Screens -> Configurar pantallas
- Checklist -> Lista de verificación
- Ailerons -> Alerones
- Elevator -> Profundidad
- Rudder -> Dirección
- Throttle -> Acelerador
- Mix / Mixes -> Mezcla / Mezclas
- Free mix -> Mezcla libre
- Outputs -> Salidas
- Timers -> Temporizadores
- Timer -> Temporizador
- Trim / Trims -> Trim (kept)
- Flight mode -> Fase de vuelo
- Logical switch -> Interruptor lógico
- Special function -> Función especial
- Switch -> Interruptor
- Source -> Fuente
- Sensor -> Sensor (kept)
- Receiver -> Receptor
- Widget -> Widget (kept)
- Screen -> Pantalla
- Stick -> Stick (kept)
- Potentiometer / pot -> Potenciómetro
- Slider -> Deslizador
- Channel -> Canal
- Differential -> Diferencial
- Throttle cut -> Corte de gas
- Throttle hold -> Retención de gas
- Idle -> Ralentí
""".strip(),
    "it": """
- Getting Started -> Per iniziare
- Model Setup -> Configurazione del modello
- System Setup -> Configurazione di sistema
- Displays -> Display
- Tutorials -> Tutorial
- How-To Guides -> Guide pratiche
- Lua Scripts -> Script Lua
- Radio Notes -> Note sulla radio
- Home -> Home (kept)
- Model Select -> Selezione modello
- Configure Screens -> Configura schermate
- Checklist -> Checklist (kept)
- Ailerons -> Alettoni
- Elevator -> Profondità
- Rudder -> Timone
- Throttle -> Gas
- Mix / Mixes -> Mix (kept)
- Free mix -> Mix libero
- Outputs -> Uscite
- Timers -> Timer (kept)
- Timer -> Timer (kept)
- Trim / Trims -> Trim (kept)
- Flight mode -> Fase di volo
- Logical switch -> Interruttore logico
- Special function -> Funzione speciale
- Switch -> Interruttore
- Source -> Sorgente
- Sensor -> Sensore
- Receiver -> Ricevitore
- Widget -> Widget (kept)
- Screen -> Schermata
- Stick -> Stick (kept)
- Potentiometer / pot -> Potenziometro
- Slider -> Slider (kept)
- Channel -> Canale
- Differential -> Differenziale
- Throttle cut -> Taglio gas
- Throttle hold -> Blocco gas
- Idle -> Minimo
""".strip(),
    "pt-BR": """
- Getting Started -> Primeiros passos
- Model Setup -> Configuração do modelo
- System Setup -> Configuração do sistema
- Displays -> Telas
- Tutorials -> Tutoriais
- How-To Guides -> Guias práticos
- Lua Scripts -> Scripts Lua
- Radio Notes -> Notas do rádio
- Home -> Início
- Model Select -> Seleção de modelo
- Configure Screens -> Configurar telas
- Checklist -> Lista de verificação
- Ailerons -> Aileron (kept)
- Elevator -> Profundor
- Rudder -> Leme
- Throttle -> Acelerador
- Mix / Mixes -> Mixagem / Mixagens
- Free mix -> Mixagem livre
- Outputs -> Saídas
- Timers -> Temporizadores
- Timer -> Temporizador
- Trim / Trims -> Trim (kept)
- Flight mode -> Fase de voo
- Logical switch -> Interruptor lógico
- Special function -> Função especial
- Switch -> Interruptor
- Source -> Fonte
- Sensor -> Sensor (kept)
- Receiver -> Receptor
- Widget -> Widget (kept)
- Screen -> Tela
- Stick -> Stick (kept)
- Potentiometer / pot -> Potenciômetro
- Slider -> Slider (kept)
- Channel -> Canal
- Differential -> Diferencial
- Throttle cut -> Corte de acelerador
- Throttle hold -> Retenção de acelerador
- Idle -> Marcha lenta
""".strip(),
    "zh": """
- Getting Started -> 快速入门
- Model Setup -> 模型设置
- System Setup -> 系统设置
- Displays -> 显示屏
- Tutorials -> 教程
- How-To Guides -> 操作指南
- Lua Scripts -> Lua 脚本
- Radio Notes -> 遥控器说明
- Home -> 主页
- Model Select -> 模型选择
- Configure Screens -> 配置显示屏
- Checklist -> 检查清单
- Ailerons -> 副翼
- Elevator -> 升降舵
- Rudder -> 方向舵
- Throttle -> 油门
- Mix / Mixes -> 混控 / 混控设置
- Free mix -> 自由混控
- Outputs -> 输出
- Timers -> 计时器
- Timer -> 计时器
- Trim / Trims -> 微调
- Flight mode -> 飞行模式
- Logical switch -> 逻辑开关
- Special function -> 特殊功能
- Switch -> 开关
- Source -> 信号源
- Sensor -> 传感器
- Receiver -> 接收机
- Widget -> 小组件
- Screen -> 屏幕
- Stick -> 摇杆
- Potentiometer / pot -> 电位器
- Slider -> 滑块
- Channel -> 通道
- Differential -> 差动
- Throttle cut -> 油门切断
- Throttle hold -> 油门保持
- Idle -> 怠速
""".strip(),
}


def _load_configured_locales(repo_root: Path) -> dict[str, str]:
    """Return {locale: display_name} for every non-default locale in mkdocs.yml."""
    mkdocs_path = repo_root / "mkdocs.yml"
    try:
        config = yaml.safe_load(mkdocs_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        print(f"WARNING: could not parse mkdocs.yml ({exc}); use --only to name locales explicitly")
        return {}
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "i18n" in plugin:
            languages = (plugin["i18n"] or {}).get("languages", [])
            return {
                lang["locale"]: lang.get("name", lang["locale"])
                for lang in languages
                if not lang.get("default")
            }
    return {}


def _page_status(en_sha: str | None, locale_path: Path) -> str:
    if not locale_path.exists():
        return "missing"
    translated_from = _read_frontmatter(locale_path).get("translated_from")
    if translated_from is None:
        return "stale (no marker)"
    if en_sha and translated_from == en_sha:
        return "current"
    return "stale"


def _en_pages(only_pages: list[str] | None) -> list[str]:
    all_pages = sorted(
        p.relative_to(EN_DIR).as_posix()
        for p in EN_DIR.rglob("*.md")
        if p.name != STATUS_FILENAME
    )
    if not only_pages:
        return all_pages
    unknown = [p for p in only_pages if p not in all_pages]
    if unknown:
        raise SystemExit(f"ERROR: not a page under docs/en/: {', '.join(unknown)}")
    return only_pages


def gather_candidates(
    locale: str, only_pages: list[str] | None, force: bool
) -> list[tuple[str, str, str]]:
    """Return [(rel_path, en_sha, status), ...] for pages needing translation."""
    candidates = []
    for rel in _en_pages(only_pages):
        en_sha, _en_date = _git_last_commit(REPO_ROOT, EN_DIR / rel)
        if en_sha is None:
            print(f"  WARNING: {rel} has no git history yet (uncommitted?) -- skipping")
            continue
        locale_path = DOCS_DIR / locale / rel
        status = _page_status(en_sha, locale_path)
        if status == "current" and not force:
            continue
        candidates.append((rel, en_sha, status))
    return candidates


def _clean_output(text: str) -> str:
    """Defensively strip a fenced-code wrapper if the model added one despite instructions."""
    text = text.strip()
    lines = text.split("\n")
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text + "\n"


def translate_page(
    client: anthropic.Anthropic,
    model: str,
    locale: str,
    locale_name: str,
    source_text: str,
) -> str:
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        locale_name=locale_name,
        no_translate_terms=", ".join(NO_TRANSLATE_TERMS),
        glossary_block=GLOSSARIES.get(locale, "(no glossary yet for this locale)"),
    )
    with client.messages.stream(
        model=model,
        max_tokens=16000,
        system=system_prompt,
        messages=[{"role": "user", "content": source_text}],
    ) as stream:
        message = stream.get_final_message()
    text = "".join(block.text for block in message.content if block.type == "text")
    return _clean_output(text)


def write_translation(locale: str, rel: str, en_sha: str, translated_text: str) -> Path:
    out_path = DOCS_DIR / locale / rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(f"---\ntranslated_from: {en_sha}\n---\n\n{translated_text}", encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Auto-translate Ethos manual pages via the Claude API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--only", nargs="*", metavar="LOCALE", help="Limit to these locales (e.g. fr de)")
    ap.add_argument("--pages", nargs="*", metavar="PATH", help="Limit to these pages (e.g. model-setup/mixes.md)")
    ap.add_argument("--dry-run", action="store_true", help="List what would be translated, no API calls")
    ap.add_argument("--force", action="store_true", help="Retranslate already-current pages too")
    ap.add_argument("--limit", type=int, metavar="N", help="Cap how many pages get translated this run")
    ap.add_argument("--model", default=DEFAULT_MODEL, metavar="MODEL_ID",
                     help=f"Claude model id (default: {DEFAULT_MODEL})")
    ap.add_argument("--yes", action="store_true", help="Skip the confirmation prompt")
    args = ap.parse_args(argv)

    configured = _load_configured_locales(REPO_ROOT)
    if args.only:
        unknown = set(args.only) - set(configured) if configured else set()
        if unknown:
            print(f"WARNING: not in mkdocs.yml's i18n languages list: {', '.join(sorted(unknown))}")
        locales = args.only
    else:
        if not configured:
            raise SystemExit("ERROR: could not determine locales from mkdocs.yml -- pass --only explicitly")
        locales = sorted(configured)

    print(f"Ethos manual auto-translator  (model: {args.model})")
    print(f"Locales: {', '.join(locales)}\n")

    plan: list[tuple[str, str, str, str]] = []  # (locale, rel, en_sha, status)
    for locale in locales:
        locale_name = configured.get(locale, locale)
        candidates = gather_candidates(locale, args.pages, args.force)
        print(f"  {locale} ({locale_name}): {len(candidates)} page(s) to translate")
        for rel, en_sha, status in candidates:
            print(f"    [{status}] {rel}")
            plan.append((locale, rel, en_sha, status))

    if args.limit is not None:
        plan = plan[: args.limit]

    if not plan:
        print("\nNothing to translate.")
        return 0

    print(f"\n{len(plan)} page(s) queued.")

    if args.dry_run:
        print("Dry run -- no API calls made, no files written.")
        return 0

    if not args.yes:
        answer = input(f"\nTranslate {len(plan)} page(s) with {args.model}? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted.")
            return 0

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    translated = 0
    failed: list[str] = []
    for i, (locale, rel, en_sha, status) in enumerate(plan, 1):
        locale_name = configured.get(locale, locale)
        print(f"[{i}/{len(plan)}] {locale}/{rel} ({status})...", end=" ", flush=True)
        source_text = (EN_DIR / rel).read_text(encoding="utf-8")
        try:
            translated_text = translate_page(client, args.model, locale, locale_name, source_text)
        except anthropic.APIError as exc:
            print(f"FAILED: {exc}")
            failed.append(f"{locale}/{rel}")
            time.sleep(2)
            continue
        out_path = write_translation(locale, rel, en_sha, translated_text)
        print(f"-> {out_path.relative_to(REPO_ROOT)}")
        translated += 1

    print(f"\nDone: {translated} translated, {len(failed)} failed.")
    if failed:
        print("Failed pages (re-run to retry):")
        for f in failed:
            print(f"  {f}")
    print(
        "\nNothing was committed. Review the diff (`git diff docs/`), fix up any "
        "anchor-pinning per docs/en/contributing/index.md, then commit/PR as usual."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
