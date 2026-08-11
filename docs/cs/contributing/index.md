---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# Přispívání

## Proč tento manuál existuje

Předchozí manuál ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
se rozpadl na dvě navzájem nepropojené poloviny podle jazyka. Anglická větev
byla vždy jen **aparát pro generování snímků obrazovky** — shellové skripty
ovládající skutečný simulátor Ethos přes Lua makro API za účelem zachycení
snímků uživatelského rozhraní — bez jakéhokoli zdroje v Markdownu (nebo v jiném
formátu čistého textu) pro vlastní text manuálu; anglický text existoval pouze
jako hromada exportů do PDF/ODT. Francouzská větev naproti tomu byla plně
napsaný export z GitBooku se skutečným obsahem, ale sestavovaný a udržovaný
nezávisle, s vlastní samostatnou sadou ručně vložených snímků obrazovky.
Ostatní jazyky neměly ani jedno. Neexistoval jediný zdroj pravdy, *z* něhož
překládat, a nebylo možné zjistit, kdy se přeložená stránka rozešla s
(neexistujícím) anglickým originálem.

Tento repozitář začíná znovu s jedním formátem pro každou stránku v každém
jazyce: čistý Markdown, sestavovaný pomocí [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(stejná technologie, jakou používá [wingflight-docs](https://doc.wingflight.org)),
nasazovaný na GitHub Pages při každém pushi do `main`.

## Pracovní postup

Před obsahem nestojí žádný CMS ani webový editor — autoři a překladatelé
pracují přímo v gitu, stejně jako u jakékoli jiné změny v tomto
repozitáři:

1. Vytvořte větev z `main` (přímo v tomto repozitáři — viz poznámka o forcích níže).
2. Upravte příslušné soubory `.md` v `docs/en/`.
3. Prohlédněte si výsledek lokálně pomocí `mkdocs serve` (viz
   [README](https://github.com/robthomson/ethos-manual-rework) v korenovém adresáři),
   nebo prostě otevřete pull request a využijte automatický náhled PR popsaný níže.
4. Otevřete pull request.

Snímky obrazovky odkazované ze stránky leží vedle ní v `docs/en/assets/` a
jsou to jen obrázkové odkazy v Markdownu — žádná speciální syntaxe. Jak se
generují, popisuje [Pipeline snímků obrazovky](screenshot-pipeline.md).

### Náhledy PR {: #pr-previews }

Každý pull request proti `main` získá svůj vlastní živý náhled, sestavený a
nasazený automaticky pomocí `.github/workflows/pr-preview.yml`: na adrese
`manual.rt-rc.com/pr-preview/<číslo PR>/`, odkazovaný v komentáři bota v
daném PR a aktualizovaný při každém pushi. Po zavření PR je automaticky
odstraněn. Hlavní web samotný (`manual.rt-rc.com`) tím není ovlivněn — náhledy
existují vedle něj ve složce `pr-preview/` ve větvi `gh-pages`, která přežije
každé produkční nasazení.

Toto funguje pouze pro větve pushnuté přímo do tohoto repozitáře, ne pro
forky — PR z forku živý náhled nedostane (GitHub záměrně odepírá zapisovací
přístup k `GITHUB_TOKEN` u workflow `pull_request` spouštěných z forku, aby
fork nemohl přes CI pushovat libovolný obsah do `gh-pages`). Přispěvatelé
používající fork si i tak mohou udělat náhled lokálně pomocí `mkdocs serve`.

## Verzování

Manuály pro více verzí firmwaru (např. 1.6 vedle budoucího Ethos26) žijí
ve stejném repozitáři jako samostatné větve, každá nasazená na vlastní cestu
`manual.rt-rc.com/<verze>/` s rozbalovacím výběrem verze — celé schéma a
postup vytvoření nové verze viz [Verzování](versioning.md).

## Plán překladů {: #translation-plan }

Překladatelé (lidští i AI) pracují přímo v gitu, stejně jako u jakékoli jiné
změny — žádný CMS, žádná samostatná překladatelská aplikace. První francouzský
pilot (několik stránek) ověřil celý mechanismus od začátku do konce; níže je,
jak to skutečně funguje.

### Přidání/aktualizace překladu {: #addingupdating-a-translation }

1. Vytvořte větev, vytvořte/upravte `docs/<locale>/<stejná cesta jako u anglické stránky>`
   a přeložte text. Kód a literály (názvy tlačítek jako `ENT`,
   `RTN`, názvy prvků rozhraní zobrazené na displeji) ponechte tak, jak jsou.
2. Označte stránku tím, ze kterého anglického commitu byla přeložena:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Tuto sha najdete příkazem `git log -1 --format=%H -- docs/en/<path>`.
3. **Pokud anglická stránka obsahuje nadpis, na který jiné stránky odkazují
   pomocí kotvy** (zkontrolujte vyhledáním `#that-heading-slug` v celém
   `docs/en/`), nedovolte, aby vlastní automaticky generovaný slug přeloženého
   nadpisu změnil cíl odkazu — připněte explicitně stejné ID, stabilní napříč
   jazyky, pomocí `attr_list` (již povoleno):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Vynechání tohoto kroku sestavení nerozbije, ale tiše rozbije odskok na
   kotvu pro každou jinou, dosud nepřeloženou stránku, která na tento nadpis
   odkazuje přes fallback.
4. Otevřete PR — [udělejte si náhled](#pr-previews) jako u jakékoli jiné změny,
   včetně přepínače jazyků.

### Snímky obrazovky

Není nutné nic předem duplikovat. [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
se vrací k anglickému souboru u *jakéhokoli* prostředku, jehož vlastní kopii
daný jazyk nemá — odkaz `../assets/foo.png` na přeložené stránce prostě
funguje, bez úprav, a zobrazí anglický snímek, dokud se pod stejným názvem
souboru nevloží skutečný lokalizovaný snímek do `docs/<locale>/assets/`, což
od té chvíle fallback tiše přepíše.

**`de` a `fr` už skutečné lokalizované snímky mají** — nebyly zachyceny zde,
ale hromadně importovány ze starého repozitáře [`ethos-manual`](https://github.com/FrSkyRC/ethos-manual),
u kterého se ukázalo, že obsahuje téměř kompletní sady snímků pro jednotlivé
jazyky, které už tým FrSky sám zachytil (`german/assets/` a pro francouzštinu
`french_LT/assets/` — úplnější ze dvou francouzských sad, ne menší
`french/assets/`, kterou její README popisuje jako „half way"). Názvy souborů
odpovídají našemu `docs/en/assets/` 1:1, takže import byl přímé kopírování:
586 z našich 589 aktuálně odkazovaných snímků se v jednom průchodu podařilo
získat pro oba jazyky, bez zapojení simulátoru. Těch několik, které neodpovídaly
(2–3 soubory, převážně novější stránky, které makra starého repozitáře nikdy
nepokrývala), se normálně vrací k angličtině.

Pro jakýkoli jazyk kromě `de`/`fr` nebo pro dokončení posledních několika
procent znamená zachycení nových snímků použití [pipeline snímků obrazovky](screenshot-pipeline.md)
— tedy přenesení a spuštění skutečného aparátu maker proti simulátoru — protože
tato práce nebyla upstream provedena.

### Sledování zastaralosti

[Stav překladů](translation-status.md) se generuje automaticky
před každým sestavením (`hooks/i18n_status.py`, zapojeno prostřednictvím
`hooks:` v `mkdocs.yml` — běží lokálně, v náhledech PR i v produkci stejně,
vždy aktuální, nikdy se necommituje do gitu) a porovnává značku
`translated_from` každého jazyka s commitem, ve kterém se daná anglická
stránka skutečně naposledy změnila: **aktuální**, **zastaralá** (angličtina
se posunula) nebo **chybějící**. Tato stránka je pracovní seznam — žádné
GitHub Issues, žádné prohrabávání logů v Actions.

### Automatický překlad (nepovinné)

`scripts/translate.py` je samostatný lokální skript (není součástí sestavení
webu ani CI), který provádí stejný pracovní seznam chybějících/zastaralých
stránek přes Claude API a vytváří pro každou stránku první návrh překladu,
automaticky opatřený správným frontmatterem `translated_from:`:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Ve výchozím nastavení čte všechny jazyky z konfigurace pluginu `i18n` v
`mkdocs.yml` (`--only` omezuje na konkrétní), přeskakuje vše, co je již
aktuální, pokud není zadáno `--force`, a nikdy necommituje ani nepushuje —
pouze zapisuje soubory do `docs/<locale>/`, stejně jako byste je upravili
ručně. Zkontrolujte diff, provedte kontrolu [připnutí kotev](#addingupdating-a-translation)
u každého nově přeloženého nadpisu a pak jako obvykle otevřete PR.

Systémový prompt předem seznámí Claude s doménou manuálu (firmware FrSky
Ethos pro vysílače, publikum RC modelářů) a se seznamem termínů, které se
nikdy nesmí překládat (názvy fyzických tlačítek, názvy protokolů, značky) —
stejná technika, jakou používá sesterský repozitář
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite)
ve svém `bin/i18n/auto-translate.py`. Každý podporovaný jazyk má vlastní
glosář zapečený v `GLOSSARIES` ve skriptu, aby byla terminologie konzistentní
už od první přeložené stránky.

Rozjezd úplně nového jazyka — od volby správného kódu jazyka přes překlad,
snímky obrazovky, opravy kotev až po popisky navigace — je opakovatelný
proces od začátku do konce: celý postup viz [Přidání nového
jazyka](adding-a-language.md).

### Popisky navigace (`nav_translations`)

Popisky karet a bočního panelu v `nav:` (např. „Model Setup") automaticky
nepřeberou přeložený titulek stránky v daném jazyce, pokud položka navigace
nemá vůbec žádný explicitní popisek (např. `- how-to/index.md` — MkDocs pak
použije vlastní H1 dané stránky). Všude, kde `nav:` uvádí explicitní řetězec
`Label: path.md` nebo pojmenovává sekci (`Model Setup:` jako klíč slovníku
s potomky), zůstává tento popisek v angličtině, dokud jej nepokryje mapa
`nav_translations` daného jazyka v `mkdocs.yml` — ta se pro jazyk přidává,
až je pokrytí stránek dostatečně rozsáhlé, aby překlad rámce webu před
většinou obsahu nepůsobil zvláštně. Mapa pro `fr` byla doplněna, jakmile
francouzština dosáhla plného pokrytí stránek; každý koncový popisek byl
zkopírován slovo za slovem z přeloženého H1 dané stránky, takže text v
bočním panelu přesně odpovídá nadpisu stránky.
