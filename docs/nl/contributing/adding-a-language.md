---
translated_from: 23549d0bf136da221c75de9a0c5695864d338cab
---

# Een nieuwe taal toevoegen

Een stap-voor-stap-draaiboek om een locale van nul naar een volledig
vertaalde, volledig navigeerbare handleiding te brengen — geschreven voor
wie (mens of agent) de volgende doet. Elke stap hieronder is daadwerkelijk
in deze volgorde uitgevoerd voor `de`, `fr`, `es`, `it`, `pt-BR` en `zh`;
de genoemde valkuilen zijn echte problemen die daarbij optraden, geen
hypothetische.

## Checklist

Werk de lijst in volgorde af; elk item verwijst naar de sectie met de
daadwerkelijke commando's en de valkuilen die zich in de praktijk
voordeden. Sla stap 4 niet direct over — stappen 1 en 3 kosten weinig en
voorkomen later herstelwerk.

- [ ] **[1](#1-confirm-the-locale-code-before-touching-anything)** — Controleer of Ethos een gebruikersinterface in deze taal levert, en kies een localecode waarvoor `mkdocs-material` daadwerkelijk een template heeft (niet noodzakelijk de code die FrSky's eigen tooling intern gebruikt — `pb` versus `pt-BR` heeft ons hier de nek gekost).
- [ ] **[2](#2-add-the-locale-to-mkdocsyml)** — Voeg de locale toe aan `mkdocs.yml` (nog geen `nav_translations`).
- [ ] **[3](#3-seed-a-glossary-in-scriptstranslatepy)** — Leg een verklarende lijst van ~30 termen aan in `GLOSSARIES` van `scripts/translate.py`.
- [ ] **[4](#4-translate)** — Voer `scripts/translate.py --only <code>` uit (eerst als dry-run); controleer op `0 failed`.
- [ ] **[5](#5-check-for-existing-screenshots-before-considering-the-simulator)** — Kijk in de oude `ethos-manual`-repository of er al een set schermafbeeldingen is opgenomen voordat je aanneemt dat de simulator-pijplijn nodig is; kopieer in bulk en controleer visueel steekproefsgewijs als er een overeenkomt.
- [ ] **[6](#6-check-and-fix-anchor-links)** — Voer `python scripts/check_anchors.py --fix` uit.
- [ ] **[7](#7-verify-for-real)** — `mkdocs build --strict` en controleer of `$?` gelijk is aan `0` (niet alleen of de uitvoer er schoon uitziet); `check_anchors.py` meldt 0.
- [ ] **[8](#8-add-nav_translations-once-after-page-coverage-is-complete)** — Zodra de paginadekking volledig is, voeg `nav_translations` toe (labels van eindpagina's uit de eigen H1 van elke pagina, sectietabbladen uit de terminologielijst).
- [ ] **[9](#9-ship-it)** — Committen, pushen, de Action in de gaten houden, live verifiëren (reken op vertraging door CDN-propagatie bij volledig nieuwe paden).

## 1. Bevestig de localecode voordat je iets aanraakt {: #1-confirm-the-locale-code-before-touching-anything }

Twee afzonderlijke zaken moeten overeenkomen, en als een van beide fout
gaat is dat later lastig terug te draaien (URL's bakken de code permanent
in):

- **Levert Ethos daadwerkelijk een gebruikersinterface in deze taal?** Een
  handleiding in een taal die de firmware niet ondersteunt is verwarrend,
  niet nuttig. FrSky's eigen desktopapplicatie
  [Ethos Suite](https://www.frsky-rc.com/) bevat per ondersteunde taal een
  `i18n/*.json`-bestand — lokaal geïnstalleerd staat dat in
  `Program Files/Ethos Suite/i18n/`. Die lijst (`cs`, `de`, `en`, `es`,
  `fr`, `he`, `it`, `nl`, `no`, `pb`, `sk`, `zh-CN` bij de laatste
  controle) is een betrouwbare indicatie van wat Ethos zelf ondersteunt.
- **Levert `mkdocs-material` een taalwisselaar-template voor die code?**
  Dit is een *andere* lijst, en de twee komen niet altijd overeen — de map
  van Ethos Suite heet letterlijk `pb`, maar Material heeft geen
  `partials/languages/pb.html`, alleen `pt-BR.html`. Met `pb` bouwt alles
  prima tot aan de sitemap-stap na de build van `mkdocs build`, waar het
  crasht met `jinja2.exceptions.TemplateNotFound` — **en die crash bevat
  het woord "error" of "warning" niet**, dus wie de build-uitvoer daarop
  doorzoekt (een volkomen redelijke aanpak) ziet een schone build die in
  werkelijkheid met een niet-nul exitcode is afgesloten. Controleer altijd
  `$?` na `mkdocs build --strict`, niet alleen de afgedrukte uitvoer. Om de
  exacte codes te zien die Material ondersteunt:

  ```python
  import material
  from pathlib import Path
  p = Path(material.__file__).parent / "templates" / "partials" / "languages"
  print(sorted(x.stem for x in p.glob("*.html")))
  ```

## 2. Voeg de locale toe aan `mkdocs.yml` {: #2-add-the-locale-to-mkdocsyml }

```yaml
languages:
  - locale: <code>
    name: <native display name>
    build: true
```

Nog geen `nav_translations` — dat is stap 6, zodra er echte inhoud is om
labels tegen af te stemmen.

## 3. Leg een terminologielijst aan in `scripts/translate.py` {: #3-seed-a-glossary-in-scriptstranslatepy }

Voeg een `GLOSSARIES["<code>"]`-vermelding toe (zie de bestaande
`fr`/`de`/`es`/`it`-vermeldingen voor de te dekken termenlijst — namen van
stuurvlakken, vocabulaire rond mixen/uitgangen/timers/trims, schakelaars,
sensoren, enzovoort). Dit houdt de terminologie consistent vanaf de
allereerste vertaalde pagina, in plaats van dat die per pagina afdrijft.
~30 termen is voldoende; het is een basis om op voort te bouwen, geen
volledig woordenboek.

Als de console halverwege een run een `UnicodeEncodeError` geeft — dit
gebeurde specifiek bij `zh` — dan komt dat doordat de Windows-console
standaard `cp1252` gebruikt, dat niet-Latijnse schriften niet kan
coderen. Dit is al opgelost aan het begin van het script
(`sys.stdout.reconfigure(encoding="utf-8", ...)`); als het opnieuw
opduikt, moet je daar kijken.

## 4. Vertalen {: #4-translate }

```bash
python scripts/translate.py --only <code> --dry-run   # confirm scope/cost first
python scripts/translate.py --only <code> --yes
```

Onafhankelijke locales kunnen **parallel** lopen (afzonderlijke
achtergrondprocessen) — ze lezen alleen gedeelde bestanden (`docs/en/`,
`mkdocs.yml`) en schrijven naar volledig gescheiden
`docs/<code>/`-boomstructuren, dus er is geen race condition. Vier locales
die gelijktijdig vertaalden waren ongeveer even snel klaar in
kloktijd als één.

Controleer in het logboek op `Done: N translated, 0 failed` voordat je
verdergaat.

## 5. Kijk naar bestaande schermafbeeldingen voordat je de simulator overweegt {: #5-check-for-existing-screenshots-before-considering-the-simulator }

**Neem niet aan dat nieuwe schermafbeeldingen het uitvoeren van de
simulator-pijplijn vereisen — controleer dat eerst.** De voorgaande
repository
([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), doorgaans
gekloond als een zustermap) heeft mogelijk al een opgenomen, per taal
ingedeelde set schermafbeeldingen van FrSky's eigen team die ongebruikt
ligt. Dat was zo voor Duits, Frans (via de map `french_LT/` — niet de
kleinere, incomplete `french/`), Italiaans en Spaans; voor Portugees en
Chinees was er niets. Controleer de overlap in bestandsnamen met wat deze
repository momenteel gebruikt:

```python
from pathlib import Path
old_repo_lang_assets = Path("../ethos-manual/<language-folder>/assets")  # sibling checkout
current = {p.name for p in Path("docs/en/assets").iterdir() if p.suffix.lower() == ".png"}
old = {p.name for p in old_repo_lang_assets.glob("*.png")}
print(f"{len(old & current)} / {len(current)} would match")
```

Een hoog overeenkomstpercentage (in de praktijk ≥90%) betekent dat het een
rechtstreekse kopie naar `docs/<code>/assets/` is — `fallback_to_default`
in `mkdocs.yml` zorgt ervoor dat dat *alles* is wat nodig is; geen
wijzigingen in markdown. **Controleer ten minste één gekopieerde
afbeelding visueel** voordat je op de overeenkomst vertrouwt (open die,
bevestig dat het werkelijk de gebruikersinterface in de doeltaal is en
geen verouderde of verkeerde opname) — overeenkomende bestandsnamen
garanderen niet strikt dat de inhoud overeenkomt, ook al was dat tot nu
toe altijd zo.

Als er geen overeenkomst is (Portugees, Chinees, of elke toekomstige taal
die de oude repository nooit heeft gedekt), valt de locale automatisch en
correct terug op de Engelse schermafbeeldingen. Dat is de verwachte,
werkende toestand — het gat echt dichten betekent de eigenlijke
macropijplijn overzetten en tegen de simulator uitvoeren (zie
[Screenshot-pijplijn](screenshot-pipeline.md)), wat buiten het bereik van
een tekstvertaalronde valt en een lokale simulatorinstallatie vereist.

## 6. Ankerkoppelingen controleren en repareren {: #6-check-and-fix-anchor-links }

Het vertalen van een kop wijzigt de automatisch gegenereerde slug, wat
elke `#die-kop-slug`-koppeling vanaf een andere pagina stilzwijgend
onklaar maakt — en **dit is geen build-fout**: `mkdocs build --strict`
faalt hier niet op, dus niets waarschuwt je ervoor behalve een dode
koppeling waarop een lezer klikt.

```bash
python scripts/check_anchors.py         # report only
python scripts/check_anchors.py --fix   # pin every finding, in en + every locale that has the page
```

Dit is een echte, terugkerende soort fout, geen eenmalige opruimactie —
elke tot nu toe toegevoegde locale bracht een handvol nieuwe gevallen aan
het licht (juist die gevallen waarin een voor `<locale>` specifieke
vertaalde slug afweek van het Engels, terwijl de vertaling van een
*andere* locale dat niet deed). Voer het uit na elke batch nieuwe of
bijgewerkte vertalingen. Het bouwt de site standaard zelf opnieuw op
(eerst `mkdocs build --strict`) zodat de resultaten nooit verouderd zijn.

## 7. Echt verifiëren {: #7-verify-for-real }

```bash
mkdocs build --strict; echo "exit code: $?"   # must be 0, not just free of "error"/"warn" text
python scripts/check_anchors.py                # must report 0
```

## 8. `nav_translations` toevoegen — eenmalig, nadat de paginadekking volledig is {: #8-add-nav_translations-once-after-page-coverage-is-complete }

Labels van tabbladen en de zijbalk in `nav:` nemen de vertaalde
paginatitel van een locale niet automatisch over, tenzij de nav-vermelding
helemaal geen expliciet label heeft. Voeg `nav_translations` toe onder de
`mkdocs.yml`-vermelding van de locale zodra (en niet eerder dan) de locale
volledige — of vrijwel volledige — paginadekking heeft; het vertalen van
de omlijsting vóór de inhoud waarnaar die verwijst leest vreemd. Labels
van eindpagina's moeten letterlijk worden overgenomen uit de eigen H1 van
elke vertaalde pagina (zodat de zijbalktekst exact overeenkomt met de
paginakop); labels van sectietabbladen (Start, Aan de slag, ...) moeten
overeenkomen met de terminologielijst uit stap 3. Haal elke H1
programmatisch op in plaats van labels met de hand opnieuw te typen — dat
is sneller en sluit elke kans op een transcriptiefout uit:

```python
import re
h1 = re.search(r"^#\s+(.+)$", Path(f"docs/{code}/{rel_path}").read_text(encoding="utf-8"), re.MULTILINE).group(1).strip()
```

Slaag `Translation Status` over — dat is een gegenereerde,
uitsluitend Engelse pagina voor beheerders zonder vertaald equivalent in
enige locale.

## 9. Uitleveren {: #9-ship-it }

Committen, naar `main` pushen en de `Deploy Docs`-Action in de gaten
houden. Het CDN van GitHub Pages kan een volledig nieuw locale-pad de
eerste 15–30+ seconden na een werkelijk geslaagde deploy met een 404
antwoorden — dat is vertraging door propagatie van de edge-cache, geen
fout. Bevestig via de GitHub API dat het bestand op `gh-pages` bestaat
voordat je je zorgen maakt:

```bash
gh api "repos/<owner>/<repo>/contents/<version>/<code>/<path>?ref=gh-pages" --jq '.sha, .size'
```

en probeer daarna de live-URL opnieuw met een korte wachttijd.
