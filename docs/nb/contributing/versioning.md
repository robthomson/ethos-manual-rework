---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Versjonering

Ethos utgis i dag med fastvare under versjonsnumre (1.6.x), og det er
signalisert en overgang til årsbasert merking (f.eks. «Ethos26»). Denne
håndboken må holde dokumentasjonen for gamle versjoner tilgjengelig og
korrekt samtidig som nye versjoner aktivt skrives — denne siden forklarer
hvordan.

## Slik fungerer det

Versjonering håndteres av [mike](https://github.com/jimporter/mike),
verktøyet som Material for MkDocs selv anbefaler.
`.github/workflows/deploy.yml` kjører `mike deploy` i stedet for å
publisere direkte til roten av `gh-pages`: hver versjon bygges og
committes til sin egen undermappe der (`/1.6/`, `/26/`, …), og
`manual.rt-rc.com/` videresender til den versjonen som for øyeblikket har
aliaset `latest`. Material viser automatisk en nedtrekksmeny for valg av
versjon, basert på `versions.json` (som `mike` vedlikeholder) — dette er
uavhengig av, og fungerer rent sammen med, språkvelgeren: versjon er det
ytre banesegmentet, språk (når det finnes flere enn `en`) er det indre,
f.eks. `manual.rt-rc.com/26/fr/...`.

Dette gjenbruker samme mekanisme med «undermappe på `gh-pages`» som
[PR-forhåndsvisninger](index.md#pr-previews) — `mike`s versjonsmapper og
mappen `pr-preview/` sameksisterer på samme branch uten å komme i konflikt,
siden hver av dem kun berører sine egne baner.

## Kildeoppsett: `main` + frosne brancher

- **`main` følger alltid innholdet for gjeldende/nyeste fastvareversjon.**
  Daglig redigering skjer her akkurat som i dag — ingenting endres i den
  vanlige arbeidsflyten for bidrag.
- Så snart håndboken for en ny fastvareversjon må begynne å avvike fra det
  som ligger på `main`, **opprett først en branch navngitt etter den gamle
  versjonen**, f.eks. `1.6`, for å frese den permanent. `main` blir da
  innholdet for den nye versjonen.
- En frossen branch er ikke død — den kan fortsatt motta rettelser via sine
  egne PR-er. Den følger bare ikke lenger utviklingen av den nye versjonen.

## Opprette en ny versjon

Når håndboken for neste versjon skal begynne (f.eks. Ethos26):

1. Fra `main`, opprett og push den frosne branchen for versjonen som
   forlates:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   Kopien av `.github/workflows/deploy.yml` i `1.6` distribuerer nå
   permanent `mike deploy --push --update-aliases 1.6 latest` ved hver push
   til den branchen — korrekt som den er, ingen endring nødvendig, siden en
   branch er et fullstendig øyeblikksbilde inkludert sin egen CI-konfigurasjon.

2. På `main`, rediger `.github/workflows/deploy.yml`: endre
   versjonsstrengen i steget `Deploy version 1.6 with mike` (og navnet på
   steget) fra `1.6` til merkelappen for den nye versjonen (f.eks. `26`).
   Dette er den **eneste** nødvendige endringen for å begynne å distribuere
   den nye versjonen — neste push til `main` publiserer den til `/26/` og
   flytter aliaset `latest` dit, mens `/1.6/` forblir helt uendret.

3. Oppdater innholdet for den nye versjonen på `main` i tråd med det som
   faktisk er endret — nye/omdøpte menyseksjoner, nye skjermbilder,
   oppdatert terminologi. `nav` i `mkdocs.yml` kan avvike fritt mellom
   brancher; det finnes ingen delt konfigurasjon som må holdes synkronisert.

4. Legg navnet på den nye branchen til i utløserlisten `branches:` i
   `.github/workflows/pr-preview.yml` hvis PR-er mot den også skal få
   direkte forhåndsvisninger (frosne brancher trenger vanligvis ikke dette,
   siden de bare mottar sporadiske PR-er med rettelser).

## Skjermbilder på tvers av versjoner

Skjermbilder tas fra en spesifikk Ethos-build (se
[Skjermbilde-pipeline](screenshot-pipeline.md)) og tilhører den branchen
hvis brukergrensesnitt de viser — en versjonsdeling forgrener naturlig
skjermbildesamlingen sammen med alt annet, slik at `1.6/assets/` og (når de
er regenerert for det nye grensesnittet) `docs/en/assets/` på `main`
utvikler seg uavhengig av hverandre etter delingspunktet.
