---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Versiebeheer

Ethos levert firmware momenteel uit onder versienummers (1.6.x) en heeft
aangegeven over te gaan op een jaargebonden naamgeving (bijv. "Ethos26").
Deze handleiding moet de documentatie van oude versies beschikbaar en
correct houden terwijl er actief aan nieuwe versies wordt geschreven — deze
pagina legt uit hoe.

## Hoe het werkt

Versiebeheer wordt verzorgd door [mike](https://github.com/jimporter/mike),
de tool die Material for MkDocs zelf aanbeveelt. `.github/workflows/deploy.yml`
voert `mike deploy` uit in plaats van direct naar de `gh-pages`-root te
publiceren: elke versie wordt gebouwd en gecommit naar een eigen submap daar
(`/1.6/`, `/26/`, …), en `manual.rt-rc.com/` verwijst door naar de versie die
op dat moment de alias `latest` heeft. Material toont automatisch een
versiekeuzemenu op basis van `versions.json` (dat door `mike` wordt
onderhouden) — dit staat los van de taalkiezer en combineert daar netjes mee:
de versie is het buitenste padsegment, de taal (zodra er meer dan `en`
bestaat) het binnenste, bijv. `manual.rt-rc.com/26/fr/...`.

Hiermee wordt hetzelfde "submap op `gh-pages`"-mechanisme hergebruikt als bij
[PR-previews](index.md#pr-previews) — de versiemappen van `mike` en de map
`pr-preview/` bestaan zonder conflicten naast elkaar op dezelfde branch, omdat
elk alleen zijn eigen paden aanraakt.

## Broncodestructuur: `main` + bevroren branches

- **`main` volgt altijd de inhoud van de huidige/nieuwste firmwareversie.**
  Het dagelijkse redactiewerk gebeurt hier precies zoals nu — aan de normale
  bijdrageworkflow verandert niets.
- Zodra de handleiding van een nieuwe firmwareversie moet gaan afwijken van
  wat er op `main` staat, **maak dan eerst een branch met de naam van de oude
  versie**, bijv. `1.6`, om die permanent te bevriezen. `main` bevat dan de
  inhoud van de nieuwe versie.
- Een bevroren branch is niet dood — die kan nog steeds correcties ontvangen
  via eigen PR's. Hij volgt alleen de ontwikkeling van de nieuwe versie niet
  meer.

## Een nieuwe versie afsplitsen

Wanneer de handleiding van de volgende versie moet beginnen (bijv. Ethos26):

1. Maak vanaf `main` de bevroren branch voor de versie die achterblijft en
   push die:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   De kopie van `.github/workflows/deploy.yml` in `1.6` voert nu permanent
   `mike deploy --push --update-aliases 1.6 latest` uit bij elke push naar die
   branch — zo is het correct, er is geen aanpassing nodig, aangezien een
   branch een volledige momentopname is inclusief de eigen CI-configuratie.

2. Bewerk op `main` het bestand `.github/workflows/deploy.yml`: wijzig de
   versiestring in de stap `Deploy version 1.6 with mike` (en de naam daarvan)
   van `1.6` naar het label van de nieuwe versie (bijv. `26`). Dit is de
   **enige** vereiste aanpassing om de nieuwe versie te gaan deployen — de
   volgende push naar `main` publiceert die naar `/26/` en verplaatst de alias
   `latest` daarheen, terwijl `/1.6/` precies blijft zoals hij was.

3. Werk de inhoud van de nieuwe versie op `main` bij voor alles wat
   daadwerkelijk is gewijzigd — nieuwe of hernoemde menusecties, nieuwe
   schermafbeeldingen, bijgewerkte terminologie. De `nav` in `mkdocs.yml` mag
   vrij verschillen tussen branches; er is geen gedeelde configuratie die
   gesynchroniseerd moet blijven.

4. Voeg de naam van de nieuwe branch toe aan de `branches:`-triggerlijst in
   `.github/workflows/pr-preview.yml` als PR's tegen die branch ook live
   previews moeten krijgen (bevroren branches hebben dit meestal niet nodig,
   omdat ze alleen af en toe een correctie-PR ontvangen).

## Schermafbeeldingen over versies heen

Schermafbeeldingen worden vastgelegd vanuit een specifieke Ethos-build (zie
[Screenshot-pipeline](screenshot-pipeline.md)) en horen bij de branch waarvan
ze de gebruikersinterface tonen — bij het afsplitsen van een versie splitst de
verzameling schermafbeeldingen zich vanzelf mee met al het andere, zodat
`1.6/assets/` en (zodra ze opnieuw zijn gegenereerd voor de nieuwe interface)
`docs/en/assets/` op `main` na het afsplitspunt onafhankelijk van elkaar
uiteenlopen.
