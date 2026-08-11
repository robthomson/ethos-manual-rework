---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# Bijdragen

## Waarom deze handleiding bestaat

De vorige handleiding ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
viel per taal uiteen in twee losstaande helften. De Engelse boom was
uitsluitend een **installatie voor het genereren van schermafbeeldingen** —
shellscripts die de echte Ethos-simulator via een Lua-macro-API aanstuurden om
UI-schermafbeeldingen vast te leggen — zonder Markdown-bron (of enige andere
platte-tekstbron) voor de daadwerkelijke tekst van de handleiding; de Engelse
tekst bestond enkel als een stapel PDF/ODT-exports. De Franse boom was
daarentegen een volledig uitgeschreven GitBook-export met echte inhoud, maar
werd onafhankelijk gebouwd en onderhouden, met een eigen, afzonderlijke set
handmatig ingeplakte schermafbeeldingen. Andere talen hadden geen van beide. Er
was geen enkele bron van waarheid om *vanuit* te vertalen, en geen manier om te
zien wanneer een vertaalde pagina uit de pas was gaan lopen met de
(niet-bestaande) Engelse bron.

Deze repo begint opnieuw met één formaat voor elke pagina, in elke taal: platte
Markdown, gebouwd met [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(dezelfde stack als die van [wingflight-docs](https://doc.wingflight.org)),
uitgerold naar GitHub Pages bij elke push naar `main`.

## Werkwijze

Er zit geen CMS of webeditor voor de inhoud — schrijvers en vertalers werken
direct in git, net als bij elke andere wijziging in deze repo:

1. Maak een branch vanaf `main` (rechtstreeks in deze repo — zie de opmerking
   over forks hieronder).
2. Bewerk de relevante `.md`-bestand(en) onder `docs/en/`.
3. Bekijk het resultaat lokaal met `mkdocs serve` (zie de
   [README](https://github.com/robthomson/ethos-manual-rework) in de root), of
   open simpelweg de pull request en gebruik de automatische PR-preview
   hieronder.
4. Open een pull request.

Schermafbeeldingen waarnaar vanuit een pagina wordt verwezen, staan ernaast in
`docs/en/assets/` en zijn gewone Markdown-afbeeldingslinks — geen speciale
syntaxis. Zie [Screenshot-pipeline](screenshot-pipeline.md) voor hoe ze worden
gegenereerd.

### PR-previews {: #pr-previews }

Elke pull request tegen `main` krijgt zijn eigen live preview, automatisch
gebouwd en uitgerold door `.github/workflows/pr-preview.yml`: op
`manual.rt-rc.com/pr-preview/<PR-nummer>/`, gelinkt in een botreactie op de PR
en bijgewerkt bij elke push. De preview wordt automatisch verwijderd wanneer de
PR wordt gesloten. De hoofdsite zelf (`manual.rt-rc.com`) blijft ongewijzigd —
previews staan ernaast in een map `pr-preview/` op de branch `gh-pages`, die
elke productie-uitrol overleeft.

Dit werkt alleen voor branches die direct naar deze repo zijn gepusht, niet voor
forks — een PR vanuit een fork krijgt geen live preview (GitHub onthoudt
opzettelijk schrijfrechten aan `GITHUB_TOKEN` voor `pull_request`-workflows die
door een fork worden getriggerd, zodat een fork CI niet kan gebruiken om
willekeurige inhoud naar `gh-pages` te pushen). Bijdragers vanuit een fork kunnen
nog steeds lokaal een preview bekijken met `mkdocs serve`.

## Versiebeheer

Handleidingen van meerdere firmwareversies (bijv. 1.6 naast een toekomstige
Ethos26) staan in dezelfde repo als afzonderlijke branches, elk uitgerold naar
zijn eigen pad `manual.rt-rc.com/<versie>/` met een versiekeuzemenu — zie
[Versiebeheer](versioning.md) voor het volledige schema en hoe je een nieuwe
versie afsplitst.

## Vertaalplan {: #translation-plan }

Vertalers (mens of AI) werken direct in git, net als bij elke andere wijziging —
geen CMS, geen aparte vertaalapplicatie. Een eerste Franse pilot (een handvol
pagina's) heeft de werkwijze van begin tot eind bewezen; hieronder staat hoe het
in de praktijk werkt.

### Een vertaling toevoegen/bijwerken {: #addingupdating-a-translation }

1. Maak een branch, creëer/bewerk `docs/<locale>/<zelfde pad als de Engelse
   pagina>` en vertaal de tekst. Laat letterlijke code-tekst (toetsnamen zoals
   `ENT`, `RTN`, namen van UI-elementen zoals ze op het scherm staan) ongewijzigd.
2. Stempel de pagina met de Engelse commit waaruit hij is vertaald:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Zoek die sha op met `git log -1 --format=%H -- docs/en/<path>`.
3. **Als de Engelse pagina een kop heeft waarnaar andere pagina's via een anchor
   linken** (controleer dit door in `docs/en/` te zoeken op
   `#die-kop-slug`), laat dan niet toe dat de automatisch gegenereerde slug van
   de vertaalde kop het doel verandert — zet expliciet dezelfde, locale-stabiele
   ID vast met `attr_list` (al ingeschakeld):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Dit overslaan breekt de build niet, maar het breekt stilzwijgend het
   scrollen naar het anchor voor elke andere, nog niet vertaalde pagina die via
   de fallback naar die kop linkt.
4. Open een PR — [bekijk de preview](#pr-previews) zoals bij elke andere
   wijziging, inclusief de taalwisselaar.

### Schermafbeeldingen

Vooraf hoeft er niets gedupliceerd te worden.
[`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n) valt terug
op het Engelse bestand voor *elke* asset waarvan een locale geen eigen versie
heeft — de `../assets/foo.png` van een vertaalde pagina werkt zonder wijziging
en toont de Engelse schermafbeelding, totdat er een echte gelokaliseerde versie
onder dezelfde bestandsnaam in `docs/<locale>/assets/` wordt geplaatst, die
vanaf dan stilzwijgend de fallback overschrijft.

**`de` en `fr` hebben al echte gelokaliseerde schermafbeeldingen** — niet hier
vastgelegd, maar in bulk geïmporteerd uit de oude repo
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), die bleek te
beschikken over vrijwel complete sets schermafbeeldingen per taal die FrSky's
eigen team al had gemaakt (`german/assets/` en, voor het Frans, `french_LT/assets/`
— de meest complete van de twee Franse assetsets, niet de kleinere
`french/assets/` die de README beschrijft als "half way"). De bestandsnamen komen
1:1 overeen met onze eigen `docs/en/assets/`, dus importeren was een rechtstreekse
kopie: 586 van onze 589 momenteel gebruikte schermafbeeldingen belandden in één
keer voor beide talen, zonder simulator. Het handjevol dat niet overeenkwam (2-3
bestanden, vooral nieuwere pagina's die de macro's van de oude repo nooit
dekten) valt zoals gewoonlijk terug op het Engels.

Voor elke locale buiten `de`/`fr`, of om die laatste paar procent te dichten,
betekent het maken van nieuwe schermafbeeldingen het gebruik van de
[screenshot-pipeline](screenshot-pipeline.md) — het overzetten/uitvoeren van de
echte macro-installatie tegen de simulator — omdat dat werk niet al upstream was
gedaan.

### Verouderingscontrole

[Vertaalstatus](translation-status.md) wordt automatisch gegenereerd vóór elke
build (`hooks/i18n_status.py`, aangesloten via het onderdeel `hooks:` van
`mkdocs.yml` — draait zowel lokaal als in PR-previews en in productie, altijd
actueel, nooit in git vastgelegd) en vergelijkt de `translated_from`-markering
van elke locale met de daadwerkelijke laatste wijzigingscommit van elke Engelse
pagina: **actueel**, **verouderd** (het Engels is verder gegaan) of **ontbrekend**.
Die pagina is de takenlijst — geen GitHub Issues, geen gespit in Actions-logs.

### Geautomatiseerd vertalen (optioneel)

`scripts/translate.py` is een zelfstandig lokaal script (geen onderdeel van de
sitebuild of CI) dat dezelfde ontbrekend/verouderd-takenlijst door de Claude API
haalt om voor elke pagina een eerste conceptvertaling te maken, automatisch
gestempeld met de juiste `translated_from:`-frontmatter:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Het leest standaard alle locales uit de `i18n`-pluginconfiguratie in
`mkdocs.yml` (`--only` beperkt dit tot specifieke locales), slaat alles wat al
actueel is over tenzij `--force` wordt meegegeven, en commit of pusht nooit — het
schrijft alleen bestanden onder `docs/<locale>/`, net alsof je ze met de hand had
bewerkt. Controleer de diff, doe de
[anchor-vastzetting](#addingupdating-a-translation)-controle voor elke nieuw
vertaalde kop, en open dan zoals gewoonlijk een PR.

De systeemprompt voorziet Claude vooraf van het domein van de handleiding
(FrSky Ethos-zenderfirmware, RC-hobbyistenpubliek) en een lijst met termen die
nooit vertaald mogen worden (namen van fysieke toetsen, protocolnamen,
merknamen), dezelfde techniek als in het zusterproject
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite)
met zijn eigen `bin/i18n/auto-translate.py`. Elke ondersteunde locale heeft een
eigen woordenlijst die in `GLOSSARIES` in het script is ingebakken, voor
consistente terminologie vanaf de eerste vertaalde pagina.

Het opstarten van een volledig nieuwe locale — van het kiezen van de juiste
locale-code tot vertaling, schermafbeeldingen, anchor-correcties en navigatielabels
— is van begin tot eind een herhaalbaar proces: zie [Een nieuwe taal
toevoegen](adding-a-language.md) voor het volledige draaiboek.

### Navigatielabels (`nav_translations`)

Labels van tabbladen en zijbalk in `nav:` (bijv. "Model Setup") nemen niet
automatisch de vertaalde paginatitel van een locale over, tenzij het
navigatie-item helemaal geen expliciet label heeft (bijv. `- how-to/index.md` —
MkDocs gebruikt dan de eigen H1 van die pagina). Overal waar `nav:` een
expliciete `Label: path.md`-string opgeeft, of een sectie benoemt (`Model Setup:`
als dict-sleutel met onderliggende items), blijft dat label in het Engels totdat
de `nav_translations`-map van de locale in `mkdocs.yml` het dekt — die wordt voor
een locale toegevoegd zodra de paginadekking substantieel genoeg is, zodat het
vertalen van de interface vóór het merendeel van de inhoud niet vreemd
overkomt. De map van `fr` is ingevuld toen het Frans volledige paginadekking
bereikte; elk eindlabel is letterlijk gekopieerd uit de vertaalde H1 van die
pagina, zodat de tekst in de zijbalk exact overeenkomt met de paginakop.
