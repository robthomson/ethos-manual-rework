---
translated_from: 580ab32c931309705fbb3b1f3e47ca9471b21e01
---

# Bidra

## Hvorfor denne manualen finnes

Den tidligere manualen ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
var delt i to usammenhengende halvdeler per språk. Det engelske treet var kun
et **rigg for generering av skjermbilder** — skallskript som kjørte den
virkelige Ethos-simulatoren gjennom et Lua-makro-API for å ta opp
skjermbilder av brukergrensesnittet — uten Markdown-kilde (eller noen annen
ren tekstkilde) for manualens faktiske brødtekst; den engelske teksten
eksisterte bare som en stabel med PDF/ODT-eksporter. Det franske treet var
derimot en fullstendig skrevet GitBook-eksport med reelt innhold, men bygget
og vedlikeholdt uavhengig, med sitt eget separate sett av manuelt innlimte
skjermbilder. Andre språk hadde ingen av delene. Det fantes ingen enkelt
sannhetskilde å oversette *fra*, og ingen måte å se når en oversatt side
hadde blitt utdatert i forhold til den (ikke-eksisterende) engelske kilden.

Dette repoet begynner på nytt med ett format for hver side, på hvert språk:
ren Markdown, bygget med [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(samme teknologistabel som brukes for [wingflight-docs](https://doc.wingflight.org)),
publisert til GitHub Pages ved hver push til `main`.

## Arbeidsflyt

Det finnes ingen CMS eller nettbasert editor foran innholdet — forfattere og
oversettere arbeider direkte i git, på samme måte som ved enhver annen
endring i dette repoet:

1. Opprett en gren fra `main` (direkte i dette repoet — se merknaden om
   forker nedenfor).
2. Rediger de relevante `.md`-filene under `docs/en/`.
3. Forhåndsvis lokalt med `mkdocs serve` (se
   [README](https://github.com/robthomson/ethos-manual-rework) i rotmappen),
   eller bare opprett pull-forespørselen og bruk den automatiske
   PR-forhåndsvisningen beskrevet nedenfor.
4. Opprett en pull-forespørsel.

Skjermbilder som refereres fra en side ligger ved siden av den i
`docs/en/assets/` og er bare Markdown-bildelenker — ingen spesiell syntaks. Se
[Skjermbilde-pipeline](screenshot-pipeline.md) for hvordan de genereres.

### PR-forhåndsvisninger {: #pr-previews }

Hver pull-forespørsel mot `main` får sin egen live forhåndsvisning, bygget og
publisert automatisk av `.github/workflows/pr-preview.yml`: på
`manual.rt-rc.com/pr-preview/<PR number>/`, lenket i en bot-kommentar på
pull-forespørselen og oppdatert ved hver push. Den fjernes automatisk når
pull-forespørselen lukkes. Selve hovednettstedet (`manual.rt-rc.com`) berøres
ikke — forhåndsvisningene ligger side om side med det i en `pr-preview/`-mappe
på `gh-pages`-grenen, som overlever hver produksjonsutrulling.

Dette kjører kun for grener som pushes direkte til dette repoet, ikke for
forker — en pull-forespørsel fra en fork får ingen live forhåndsvisning
(GitHub holder bevisst tilbake skrivetilgang til `GITHUB_TOKEN` for
`pull_request`-arbeidsflyter utløst av forker, slik at en fork ikke kan bruke
CI til å pushe vilkårlig innhold til `gh-pages`). Bidragsytere som jobber i en
fork kan fortsatt forhåndsvise lokalt med `mkdocs serve`.

## Versjonering

Manualer for flere fastvareversjoner (f.eks. 1.6 sammen med en framtidig
Ethos26) ligger i samme repo som separate grener, hver publisert til sin egen
`manual.rt-rc.com/<version>/`-sti med en nedtrekksmeny for versjonsvalg — se
[Versjonering](versioning.md) for hele ordningen og hvordan du lager en ny.

## Oversettelsesplan {: #translation-plan }

Oversettere (menneskelige eller AI) arbeider direkte i git, på samme måte som
ved enhver annen endring — ingen CMS, ingen separat oversettelsesapplikasjon.
Et første fransk pilotprosjekt (en håndfull sider) beviste at mekanikken
fungerer fra ende til ende; her er hvordan det faktisk fungerer.

### Legge til/oppdatere en oversettelse {: #addingupdating-a-translation }

1. Opprett en gren, opprett/rediger `docs/<locale>/<samme sti som den engelske siden>`
   og oversett brødteksten. Behold tekst som er kodelitteral (tastenavn som
   `ENT` og `RTN`, samt navn på grensesnittelementer som vises på skjermen)
   som de er.
2. Merk siden med hvilken engelsk commit den ble oversatt fra:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Finn denne sha-en med `git log -1 --format=%H -- docs/en/<path>`.
3. **Hvis den engelske siden har en overskrift som andre sider lenker til via
   anker** (sjekk ved å søke etter `#that-heading-slug` på tvers av
   `docs/en/`), må du ikke la den oversatte overskriftens egen
   automatisk genererte slug endre målet — fest den samme,
   språkuavhengige ID-en eksplisitt med `attr_list` (allerede aktivert):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Å hoppe over dette bryter ikke byggingen, men det ødelegger stille
   ankerrullingen for alle andre, ennå ikke oversatte sider som lenker inn til
   den overskriften via reserveløsningen.
4. Opprett en pull-forespørsel — [forhåndsvis den](#pr-previews) som ved enhver
   annen endring, inkludert språkvelgeren.

### Skjermbilder

Ingenting må dupliseres på forhånd. [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
faller tilbake til den engelske filen for *hver* ressurs et språk ikke har sin
egen kopi av — en oversatt sides `../assets/foo.png` fungerer bare, uendret,
og viser det engelske skjermbildet, helt til et reelt lokalisert bilde legges
inn med samme filnavn under `docs/<locale>/assets/`, som deretter stille
overstyrer reserveløsningen.

**`de` og `fr` har allerede reelle lokaliserte skjermbilder** — ikke tatt opp
her, men masseimportert fra det gamle [`ethos-manual`](https://github.com/FrSkyRC/ethos-manual)-repoet,
som viste seg å ha nesten komplette skjermbildesett per språk som FrSkys eget
team allerede hadde tatt opp (`german/assets/` og, for fransk,
`french_LT/assets/` — det mest komplette av de to franske ressurssettene, ikke
det mindre `french/assets/` som README-en beskriver som «halvveis»). Filnavnene
samsvarer 1:1 med våre egne i `docs/en/assets/`, så importen var en rett
kopiering: 586 av våre 589 skjermbilder som refereres i dag kom på plass for
begge språk i én omgang, uten simulator involvert. De få som ikke samsvarte
(2–3 filer, hovedsakelig nyere sider som makroene i det gamle repoet aldri
dekket) faller fortsatt tilbake til engelsk som normalt.

For alle språk utover `de`/`fr`, eller for å lukke de siste få prosentene,
betyr det å ta opp nye skjermbilder å bruke
[skjermbilde-pipelinen](screenshot-pipeline.md) — å portere/kjøre det
virkelige makroriggen mot simulatoren — siden dette arbeidet ikke allerede var
gjort oppstrøms.

### Sporing av utdaterte oversettelser

[Oversettelsesstatus](translation-status.md) genereres automatisk før hver
bygging (`hooks/i18n_status.py`, koblet inn via `hooks:` i `mkdocs.yml` —
kjører lokalt, i PR-forhåndsvisninger og i produksjon på samme måte, alltid
oppdatert, aldri committet til git) og sammenligner hvert språks
`translated_from`-markør mot den faktiske siste endringscommiten for hver
engelske side: **oppdatert**, **utdatert** (engelsk har blitt endret) eller
**mangler**. Den siden er arbeidslisten — ingen GitHub Issues, ingen graving i
Actions-logger.

### Automatisert oversettelse (valgfritt)

`scripts/translate.py` er et frittstående lokalt skript (ikke en del av
nettstedsbyggingen eller CI) som kjører den samme
arbeidslisten over manglende/utdaterte sider gjennom Claude-API-et for å
produsere et første utkast til oversettelse for hver side, automatisk merket
med korrekt `translated_from:`-frontmatter:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Det leser som standard alle språk fra `i18n`-plugin-konfigurasjonen i
`mkdocs.yml` (`--only` begrenser til bestemte språk), hopper over alt som
allerede er oppdatert med mindre `--force` angis, og committer eller pusher
aldri — det skriver kun filer under `docs/<locale>/`, på samme måte som om du
hadde redigert dem manuelt. Gå gjennom diffen, gjør
[ankerfesting](#addingupdating-a-translation)-sjekken for alle nylig oversatte
overskrifter, og opprett deretter en pull-forespørsel som vanlig.

Systemprompten forsyner Claude på forhånd med manualens fagområde (FrSky
Ethos radiofastvare, RC-hobbypublikum) og en liste over termer som aldri skal
oversettes (fysiske tastenavn, protokollnavn, merkenavn), samme teknikk som
brukes i søsterrepoet
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite)
sitt eget `bin/i18n/auto-translate.py`. Hvert støttet språk har sin egen
ordliste innebygd i `GLOSSARIES` i skriptet for terminologisk konsistens fra
den første oversatte siden.

Å starte opp et helt nytt språk — fra valg av riktig språkkode til
oversettelse, skjermbilder, ankerkorrigeringer og navigasjonsetiketter — er en
repeterbar prosess fra ende til ende: se [Legge til et nytt
språk](adding-a-language.md) for hele oppskriften.

### Navigasjonsetiketter (`nav_translations`)

Fane- og sidepaneletiketter i `nav:` (f.eks. «Model Setup») plukker ikke
automatisk opp et språks oversatte sidetittel med mindre navigasjonsoppføringen
ikke har noen eksplisitt etikett i det hele tatt (f.eks. `- how-to/index.md` —
MkDocs bruker da sidens egen H1). Overalt der `nav:` angir en eksplisitt
`Label: path.md`-streng, eller navngir en seksjon (`Model Setup:` som en
nøkkel i en dict med underelementer), forblir denne etiketten på engelsk til
språkets `nav_translations`-kart i `mkdocs.yml` dekker den — lagt til for et
språk først når sidedekningen er tilstrekkelig omfattende til at det ikke
virker underlig å oversette rammeverket før det meste av innholdet. Kartet for
`fr` ble fylt ut da fransk oppnådde full sidedekning; hver bladetikett ble
kopiert ordrett fra den aktuelle sidens egen oversatte H1, slik at teksten i
sidepanelet samsvarer nøyaktig med sidens overskrift.
