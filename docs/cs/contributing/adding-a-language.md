---
translated_from: 23549d0bf136da221c75de9a0c5695864d338cab
---

# Přidání nového jazyka

Postup krok za krokem pro rozjezd nové jazykové verze od nuly až po plně
přeložený a plně navigovatelný manuál — napsaný pro toho (člověka i agenta),
kdo bude dělat další. Každý krok níže byl skutečně proveden, právě v tomto
pořadí, pro `de`, `fr`, `es`, `it`, `pt-BR` a `zh`; zmíněné zrádnosti jsou
reálné chyby, na které jsme při tom narazili, nikoli hypotetické.

## Kontrolní seznam

Postupujte v uvedeném pořadí; každá položka odkazuje na sekci se skutečnými
příkazy a s problémy, na které jsme při reálném nasazení narazili. Nepřeskakujte
přímo ke kroku 4 — kroky 1 a 3 jsou levné a šetří pozdější přepracování.

- [ ] **[1](#1-confirm-the-locale-code-before-touching-anything)** — Ověřte, že Ethos v tomto jazyce vůbec nabízí uživatelské rozhraní, a zvolte kód jazyka, pro který `mkdocs-material` skutečně má šablonu (nemusí to být kód, který interně používají nástroje FrSky — na tomhle jsme narazili u `pb` vs. `pt-BR`).
- [ ] **[2](#2-add-the-locale-to-mkdocsyml)** — Přidejte jazyk do `mkdocs.yml` (zatím bez `nav_translations`).
- [ ] **[3](#3-seed-a-glossary-in-scriptstranslatepy)** — Založte cca 30položkový glosář v `GLOSSARIES` ve skriptu `scripts/translate.py`.
- [ ] **[4](#4-translate)** — Spusťte `scripts/translate.py --only <code>` (nejprve nasucho); potvrďte `0 failed`.
- [ ] **[5](#5-check-for-existing-screenshots-before-considering-the-simulator)** — Než budete předpokládat, že je potřeba pipeline se simulátorem, zkontrolujte, zda ve starém repozitáři `ethos-manual` už neexistuje sada snímků obrazovky; pokud odpovídá, hromadně ji zkopírujte a vizuálně prověřte.
- [ ] **[6](#6-check-and-fix-anchor-links)** — Spusťte `python scripts/check_anchors.py --fix`.
- [ ] **[7](#7-verify-for-real)** — `mkdocs build --strict` a kontrola, že `$?` je `0` (nejen že výstup vypadá čistě); `check_anchors.py` hlásí 0.
- [ ] **[8](#8-add-nav_translations-once-after-page-coverage-is-complete)** — Až je pokrytí stránek kompletní, přidejte `nav_translations` (názvy listů z vlastního H1 každé stránky, karty sekcí z glosáře).
- [ ] **[9](#9-ship-it)** — Commitněte, pushněte, sledujte Action, ověřte naživo (počítejte s prodlevou propagace CDN u zbrusu nových cest).

## 1. Před jakoukoli prací potvrďte kód jazyka {: #1-confirm-the-locale-code-before-touching-anything }

Musí souhlasit dvě samostatné věci a chyba v kterékoli z nich se pak nepříjemně
napravuje (kód je natrvalo zapečený v URL):

- **Nabízí Ethos v tomto jazyce vůbec uživatelské rozhraní?** Manuál v jazyce,
  který firmware nepodporuje, je matoucí, ne užitečný. Desktopová aplikace
  [Ethos Suite](https://www.frsky-rc.com/) od FrSky obsahuje soubor
  `i18n/*.json` pro každý podporovaný jazyk — po lokální instalaci je najdete v
  `Program Files/Ethos Suite/i18n/`. Tento seznam (`cs`, `de`, `en`, `es`,
  `fr`, `he`, `it`, `nl`, `no`, `pb`, `sk`, `zh-CN` při poslední kontrole) je
  spolehlivým vodítkem toho, co podporuje samotný Ethos.
- **Nabízí `mkdocs-material` šablonu přepínače jazyků pro tento kód?** To je
  *jiný* seznam a oba se vždy neshodují — vlastní složka Ethos Suite se
  jmenuje doslova `pb`, ale Material žádný `partials/languages/pb.html` nemá,
  pouze `pt-BR.html`. S `pb` build bez problémů projde až do kroku generování
  sitemapy po buildu v `mkdocs build`, kde spadne s
  `jinja2.exceptions.TemplateNotFound` — **a tento pád neobsahuje slovo
  „error“ ani „warning“**, takže grepování výstupu buildu na tyto výrazy
  (což je úplně rozumný postup) ohlásí čistý build, který ovšem skončil
  nenulovým návratovým kódem. Po `mkdocs build --strict` vždy kontrolujte
  `$?`, nejen vypsaný výstup. Přesné kódy, které Material podporuje, zjistíte
  takto:

  ```python
  import material
  from pathlib import Path
  p = Path(material.__file__).parent / "templates" / "partials" / "languages"
  print(sorted(x.stem for x in p.glob("*.html")))
  ```

## 2. Přidejte jazyk do `mkdocs.yml` {: #2-add-the-locale-to-mkdocsyml }

```yaml
languages:
  - locale: <code>
    name: <native display name>
    build: true
```

Zatím žádné `nav_translations` — to je krok 6, až bude existovat skutečný
obsah, ke kterému lze názvy přiřadit.

## 3. Založte glosář v `scripts/translate.py` {: #3-seed-a-glossary-in-scriptstranslatepy }

Přidejte položku `GLOSSARIES["<code>"]` (viz existující položky `fr`/`de`/`es`/`it`
pro seznam termínů, které je třeba pokrýt — názvy kormidel, slovník
mixů/výstupů/časovačů/trimů, přepínače, senzory atd.). Právě tohle zajišťuje
konzistentní terminologii už od první přeložené stránky místo postupného
rozjezdu stránka po stránce. Cca 30 termínů stačí; je to základ, na kterém se
staví, ne kompletní slovník.

Pokud konzole v průběhu běhu ohlásí `UnicodeEncodeError` — to se stalo konkrétně
u `zh` — je to proto, že konzole Windows používá jako výchozí `cp1252`, které
neumí zakódovat nelatinská písma. Už je to opravené na začátku skriptu
(`sys.stdout.reconfigure(encoding="utf-8", ...)`); pokud by se to objevilo znovu,
hledejte tam.

## 4. Přeložte {: #4-translate }

```bash
python scripts/translate.py --only <code> --dry-run   # confirm scope/cost first
python scripts/translate.py --only <code> --yes
```

Nezávislé jazyky mohou běžet **paralelně** (jako oddělené procesy na pozadí) —
čtou pouze společné soubory (`docs/en/`, `mkdocs.yml`) a zapisují do zcela
oddělených struktur `docs/<code>/`, takže nehrozí souběh. Čtyři jazyky
překládané současně skončily v přibližně stejném reálném čase jako jeden.

Než budete pokračovat, zkontrolujte v logu `Done: N translated, 0 failed`.

## 5. Než začnete uvažovat o simulátoru, zkontrolujte existující snímky obrazovky {: #5-check-for-existing-screenshots-before-considering-the-simulator }

**Nepředpokládejte, že nové snímky vyžadují spuštění pipeline se simulátorem —
nejdřív to zkontrolujte.** Předchůdčí repozitář
([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), typicky naklonovaný
jako sousední adresář) už může obsahovat nevyužitou sadu snímků obrazovky
pořízených týmem FrSky pro daný jazyk. Tak to bylo u němčiny, francouzštiny
(ve složce `french_LT/` — ne v menší, nekompletní `french/`), italštiny a
španělštiny; pro portugalštinu a čínštinu tam nebylo nic. Porovnejte překryv
názvů souborů s tím, na co tento repozitář aktuálně odkazuje:

```python
from pathlib import Path
old_repo_lang_assets = Path("../ethos-manual/<language-folder>/assets")  # sibling checkout
current = {p.name for p in Path("docs/en/assets").iterdir() if p.suffix.lower() == ".png"}
old = {p.name for p in old_repo_lang_assets.glob("*.png")}
print(f"{len(old & current)} / {len(current)} would match")
```

Vysoká míra shody (v praxi ≥90 %) znamená, že jde o přímé zkopírování do
`docs/<code>/assets/` — `fallback_to_default` v `mkdocs.yml` znamená, že je to
*vše*, co je potřeba; žádné změny v markdownu. **Vizuálně prověřte alespoň
jeden zkopírovaný obrázek**, než shodě uvěříte (otevřete ho a potvrďte, že jde
skutečně o rozhraní v cílovém jazyce, ne o zastaralý či nesprávný snímek) —
shoda názvů souborů striktně nezaručuje shodu obsahu, i když to tak dosud vždy
bylo.

Pokud shoda není (portugalština, čínština nebo jakýkoli budoucí jazyk, který
starý repozitář nikdy nepokrýval), jazyk správně automaticky použije anglické
snímky obrazovky. To je očekávaný, funkční stav; skutečné doplnění znamená
přenést/spustit vlastní pipeline maker proti simulátoru (viz
[Pipeline snímků obrazovky](screenshot-pipeline.md)), což je mimo rozsah
textového překladu a vyžaduje lokální instalaci simulátoru.

## 6. Zkontrolujte a opravte odkazy na kotvy {: #6-check-and-fix-anchor-links }

Přeložením nadpisu se změní jeho automaticky generovaný slug, což tiše rozbije
jakýkoli odkaz `#that-heading-slug` z jiné stránky — a **není to chyba buildu**:
`mkdocs build --strict` na tom neselže, takže vám to nic neprozradí kromě
mrtvého odkazu, na který čtenář klikne.

```bash
python scripts/check_anchors.py         # report only
python scripts/check_anchors.py --fix   # pin every finding, in en + every locale that has the page
```

Jde o reálnou, opakující se kategorii chyb, ne o jednorázový úklid — každý
dosud přidaný jazyk odhalil několik nových případů (těch, které se shodou
okolností pojily s tím, že přeložený slug specifický pro daný jazyk se odchýlil
od angličtiny, zatímco překlad *jiného* jazyka nikoli). Spusťte to po každé
dávce nových či aktualizovaných překladů. Web si ve výchozím nastavení sám
znovu sestaví (nejprve `mkdocs build --strict`), takže výsledky nikdy nejsou
zastaralé.

## 7. Ověřte to doopravdy {: #7-verify-for-real }

```bash
mkdocs build --strict; echo "exit code: $?"   # must be 0, not just free of "error"/"warn" text
python scripts/check_anchors.py                # must report 0
```

## 8. Přidejte `nav_translations` — jednou, až je pokrytí stránek kompletní {: #8-add-nav_translations-once-after-page-coverage-is-complete }

Názvy karet a bočního panelu v `nav:` nepřeberou přeložený titulek stránky
daného jazyka automaticky, pokud položka navigace nemá vůbec žádný explicitní
název. `nav_translations` přidejte pod položku daného jazyka v `mkdocs.yml`
teprve tehdy (ne dříve), až má jazyk plné — nebo téměř plné — pokrytí stránek;
přeložený rám okolo obsahu, který zatím přeložený není, se čte podivně. Názvy
listů kopírujte doslova z vlastního H1 každé přeložené stránky (aby text v
bočním panelu přesně odpovídal nadpisu stránky); názvy karet sekcí (Domů,
Začínáme, …) mají odpovídat glosáři z kroku 3. Každý H1 vytáhněte programově,
místo abyste názvy přepisovali ručně — je to rychlejší a odstraňuje jakoukoli
možnost nesouladu při přepisu:

```python
import re
h1 = re.search(r"^#\s+(.+)$", Path(f"docs/{code}/{rel_path}").read_text(encoding="utf-8"), re.MULTILINE).group(1).strip()
```

`Translation Status` vynechte — jde o generovanou, pouze anglickou stránku pro
správce, která nemá v žádném jazyce přeloženou obdobu.

## 9. Vypusťte to do světa {: #9-ship-it }

Commitněte, pushněte do `main` a sledujte průběh Action `Deploy Docs`. CDN
GitHub Pages může u zbrusu nové cesty jazyka prvních 15–30 a více sekund po
skutečně úspěšném nasazení vracet 404 — to je prodleva propagace edge cache,
ne chyba. Než začnete mít obavy, ověřte přes GitHub API, že soubor na
`gh-pages` existuje:

```bash
gh api "repos/<owner>/<repo>/contents/<version>/<code>/<path>?ref=gh-pages" --jq '.sha, .size'
```

a poté zkuste živou URL znovu s krátkou prodlevou.
