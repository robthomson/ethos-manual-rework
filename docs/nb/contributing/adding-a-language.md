---
translated_from: 23549d0bf136da221c75de9a0c5695864d338cab
---

# Legge til et nytt språk

En trinnvis oppskrift for å få et språk fra ingenting til en fullstendig
oversatt, fullt navigerbar manual — skrevet for den (menneske eller agent)
som skal gjøre den neste. Hvert trinn nedenfor er faktisk kjørt, i denne
rekkefølgen, for `de`, `fr`, `es`, `it`, `pt-BR` og `zh`; fallgruvene som
nevnes er reelle feil som oppsto underveis, ikke hypotetiske.

## Sjekkliste

Arbeid gjennom i rekkefølge; hvert punkt lenker til avsnittet med de
faktiske kommandoene og fallgruvene som oppsto i praksis. Ikke hopp rett
til trinn 4 — trinn 1 og 3 er billige og sparer omarbeid senere.

- [ ] **[1](#1-confirm-the-locale-code-before-touching-anything)** — Bekreft at Ethos leveres med et brukergrensesnitt på dette språket, og velg en språkkode som `mkdocs-material` faktisk har en mal for (ikke nødvendigvis koden FrSkys eget verktøy bruker internt — `pb` mot `pt-BR` bet oss her).
- [ ] **[2](#2-add-the-locale-to-mkdocsyml)** — Legg språket til i `mkdocs.yml` (ingen `nav_translations` ennå).
- [ ] **[3](#3-seed-a-glossary-in-scriptstranslatepy)** — Legg inn en ordliste på ca. 30 termer i `GLOSSARIES` i `scripts/translate.py`.
- [ ] **[4](#4-translate)** — Kjør `scripts/translate.py --only <code>` (tørrkjøring først); bekreft `0 failed`.
- [ ] **[5](#5-check-for-existing-screenshots-before-considering-the-simulator)** — Sjekk det gamle `ethos-manual`-repoet for et allerede innhentet sett med skjermbilder før du antar at simulator-pipelinen er nødvendig; masse-kopier og kontroller visuelt hvis et sett passer.
- [ ] **[6](#6-check-and-fix-anchor-links)** — Kjør `python scripts/check_anchors.py --fix`.
- [ ] **[7](#7-verify-for-real)** — `mkdocs build --strict` og sjekk at `$?` er `0` (ikke bare at utdataene ser rene ut); `check_anchors.py` rapporterer 0.
- [ ] **[8](#8-add-nav_translations-once-after-page-coverage-is-complete)** — Når sidedekningen er komplett, legg til `nav_translations` (bladetiketter fra hver sides egen H1, seksjonsfaner fra ordlisten).
- [ ] **[9](#9-ship-it)** — Commit, push, følg Action-kjøringen, verifiser live (ta høyde for forsinkelse i CDN-propagering for helt nye stier).

## 1. Bekreft språkkoden før du rører noe {: #1-confirm-the-locale-code-before-touching-anything }

To separate ting må stemme, og å ta feil på en av dem er kjedelig å
reversere senere (URL-ene bygger inn koden permanent):

- **Leveres Ethos faktisk med et brukergrensesnitt på dette språket?** En
  manual på et språk fastvaren ikke støtter er forvirrende, ikke nyttig.
  FrSkys egen skrivebordsapplikasjon [Ethos Suite](https://www.frsky-rc.com/)
  leveres med en `i18n/*.json`-fil per støttet språk — lokalt installert
  ligger den i `Program Files/Ethos Suite/i18n/`. Den listen (`cs`, `de`,
  `en`, `es`, `fr`, `he`, `it`, `nl`, `no`, `pb`, `sk`, `zh-CN` ved siste
  kontroll) er en pålitelig indikator på hva Ethos selv støtter.
- **Leveres `mkdocs-material` med en språkvelger-mal for den koden?** Dette
  er en *annen* liste, og de to stemmer ikke alltid — Ethos Suites egen
  mappe heter bokstavelig talt `pb`, men Material har ingen
  `partials/languages/pb.html`, bare `pt-BR.html`. Å bruke `pb` bygger helt
  fint frem til `mkdocs build`s sitemap-steg etter bygget, der det krasjer
  med `jinja2.exceptions.TemplateNotFound` — **og den krasjen inneholder
  ikke ordet «error» eller «warning»**, så å grep-e byggeutdataene for disse
  (noe som er helt rimelig å gjøre) vil rapportere et rent bygg som faktisk
  avsluttet med annet enn null. Sjekk alltid `$?` etter
  `mkdocs build --strict`, ikke bare det som skrives ut. For å se de
  eksakte kodene Material støtter:

  ```python
  import material
  from pathlib import Path
  p = Path(material.__file__).parent / "templates" / "partials" / "languages"
  print(sorted(x.stem for x in p.glob("*.html")))
  ```

## 2. Legg språket til i `mkdocs.yml` {: #2-add-the-locale-to-mkdocsyml }

```yaml
languages:
  - locale: <code>
    name: <native display name>
    build: true
```

Ingen `nav_translations` ennå — det er trinn 6, etter at det finnes reelt
innhold å matche etiketter mot.

## 3. Legg inn en ordliste i `scripts/translate.py` {: #3-seed-a-glossary-in-scriptstranslatepy }

Legg til en `GLOSSARIES["<code>"]`-oppføring (se de eksisterende
`fr`/`de`/`es`/`it`-oppføringene for termlisten som skal dekkes — navn på
styreflater, vokabular for miks/utganger/timer/trim, brytere, sensorer
osv.). Dette er det som holder terminologien konsistent fra den aller
første oversatte siden i stedet for at den glir fra side til side. Ca. 30
termer er nok; det er et gulv å bygge videre på, ikke en komplett ordbok.

Hvis konsollen feiler med `UnicodeEncodeError` midt i en kjøring — dette
skjedde spesifikt for `zh` — er det fordi Windows-konsollen som standard
bruker `cp1252`, som ikke kan kode ikke-latinske skrifter. Allerede fikset
øverst i skriptet (`sys.stdout.reconfigure(encoding="utf-8", ...)`); hvis
det dukker opp igjen, er det der du skal se.

## 4. Oversett {: #4-translate }

```bash
python scripts/translate.py --only <code> --dry-run   # confirm scope/cost first
python scripts/translate.py --only <code> --yes
```

Uavhengige språk kan kjøres **parallelt** (separate bakgrunnsprosesser) —
de leser bare delte filer (`docs/en/`, `mkdocs.yml`) og skriver til helt
separate `docs/<code>/`-trær, så det finnes ingen kappløpssituasjon. Fire
språk som ble oversatt samtidig ble ferdige på omtrent samme klokketid som
ett.

Sjekk loggen for `Done: N translated, 0 failed` før du går videre.

## 5. Sjekk om det finnes skjermbilder før du vurderer simulatoren {: #5-check-for-existing-screenshots-before-considering-the-simulator }

**Ikke anta at nye skjermbilder krever at simulator-pipelinen kjøres —
sjekk først.** Forgjengerrepoet
([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), typisk klonet
som en sidestilt katalog) kan allerede ha et innhentet sett med
skjermbilder per språk fra FrSkys eget team som ligger ubrukt. Det gjorde
det for tysk, fransk (via mappen `french_LT/` — ikke den mindre,
ufullstendige `french/`), italiensk og spansk; det hadde ingenting for
portugisisk eller kinesisk. Sjekk filnavn-overlappen mot det dette repoet
refererer til i dag:

```python
from pathlib import Path
old_repo_lang_assets = Path("../ethos-manual/<language-folder>/assets")  # sibling checkout
current = {p.name for p in Path("docs/en/assets").iterdir() if p.suffix.lower() == ".png"}
old = {p.name for p in old_repo_lang_assets.glob("*.png")}
print(f"{len(old & current)} / {len(current)} would match")
```

En høy treffrate (≥90 %, i praksis) betyr at det er en ren kopiering inn i
`docs/<code>/assets/` — `fallback_to_default` i `mkdocs.yml` betyr at det
er *alt* som trengs; ingen endringer i markdown. **Kontroller visuelt minst
ett kopiert bilde** før du stoler på treffet (åpne det, bekreft at det
virkelig er brukergrensesnittet på målspråket, ikke et utdatert eller
feilmatchet skjermbilde) — at filnavn stemmer garanterer ikke strengt tatt
at innholdet stemmer, selv om det alltid har gjort det så langt.

Hvis det ikke finnes noe treff (portugisisk, kinesisk, eller et fremtidig
språk det gamle repoet aldri dekket), faller språket korrekt tilbake til
engelske skjermbilder automatisk. Det er den forventede, fungerende
tilstanden — å tette gapet for reelt betyr å portere/kjøre den faktiske
makro-pipelinen mot simulatoren (se [Skjermbilde-pipeline](screenshot-pipeline.md)),
noe som er utenfor omfanget av en ren tekstoversettelse og krever en lokal
simulatorinstallasjon.

## 6. Sjekk og reparer ankerlenker {: #6-check-and-fix-anchor-links }

Å oversette en overskrift endrer den autogenererte slug-en, noe som stille
ødelegger enhver `#that-heading-slug`-lenke fra en annen side — og **dette
er ikke en byggefeil**: `mkdocs build --strict` feiler ikke på det, så
ingenting vil fortelle deg at det har skjedd bortsett fra en død lenke en
leser klikker på.

```bash
python scripts/check_anchors.py         # report only
python scripts/check_anchors.py --fix   # pin every finding, in en + every locale that has the page
```

Dette er en reell, tilbakevendende feilklasse, ikke en engangsopprydding —
hvert språk som er lagt til så langt har avdekket en håndfull nye tilfeller
(de som tilfeldigvis sammenfalt med en `<locale>`-spesifikk oversatt slug
som avvek fra engelsk, der et *annet* språks oversettelse ikke gjorde det).
Kjør det etter hver bunke nye eller oppdaterte oversettelser. Det bygger
nettstedet selv som standard (`mkdocs build --strict` først), slik at
resultatene aldri er utdaterte.

## 7. Verifiser for reelt {: #7-verify-for-real }

```bash
mkdocs build --strict; echo "exit code: $?"   # must be 0, not just free of "error"/"warn" text
python scripts/check_anchors.py                # must report 0
```

## 8. Legg til `nav_translations` — én gang, etter at sidedekningen er komplett {: #8-add-nav_translations-once-after-page-coverage-is-complete }

Fane- og sidepanel-etiketter i `nav:` henter ikke automatisk et språks
oversatte sidetittel med mindre nav-oppføringen ikke har noen eksplisitt
etikett i det hele tatt. Legg til `nav_translations` under språkets
oppføring i `mkdocs.yml` når (ikke før) språket har full — eller nesten
full — sidedekning; å oversette rammeverket før innholdet det peker til
leses merkelig. Bladetiketter bør kopieres ordrett fra hver oversatte sides
egen H1 (slik at teksten i sidepanelet stemmer eksakt med sideoverskriften);
seksjonsfane-etiketter (Hjem, Komme i gang, ...) bør stemme med ordlisten
fra trinn 3. Hent ut hver H1 programmatisk i stedet for å skrive inn
etikettene manuelt — det er raskere og eliminerer all sjanse for en
transkripsjonsfeil:

```python
import re
h1 = re.search(r"^#\s+(.+)$", Path(f"docs/{code}/{rel_path}").read_text(encoding="utf-8"), re.MULTILINE).group(1).strip()
```

Hopp over `Translation Status` — det er en generert vedlikeholderside kun på
engelsk, uten oversatt motstykke på noe språk.

## 9. Publiser {: #9-ship-it }

Commit, push til `main`, og følg kjøringen av `Deploy Docs`-Action. CDN-en
til GitHub Pages kan gi 404 på en helt ny språksti de første 15–30+
sekundene etter en genuint vellykket utrulling — det er forsinkelse i
edge-cache-propagering, ikke en feil. Bekreft via GitHub-API-et at filen
finnes på `gh-pages` før du bekymrer deg:

```bash
gh api "repos/<owner>/<repo>/contents/<version>/<code>/<path>?ref=gh-pages" --jq '.sha, .size'
```

og prøv deretter live-URL-en på nytt med en kort ventetid.
