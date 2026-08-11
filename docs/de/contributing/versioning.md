---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Versionierung

Ethos wird derzeit unter Versionsnummern (1.6.x) veröffentlicht, hat aber
einen Wechsel zu einer jahresbasierten Bezeichnung angekündigt (z. B. „Ethos26“).
Dieses Handbuch muss die Dokumentation älterer Versionen verfügbar und korrekt
halten, während gleichzeitig an neuen Versionen aktiv geschrieben wird — diese
Seite beschreibt, wie das funktioniert.

## Funktionsweise

Die Versionierung erfolgt über [mike](https://github.com/jimporter/mike), das
Werkzeug, das Material for MkDocs selbst empfiehlt. `.github/workflows/deploy.yml`
führt `mike deploy` aus, anstatt direkt in das Wurzelverzeichnis von `gh-pages`
zu veröffentlichen: Jede Version wird gebaut und dort in einen eigenen Unterordner
committet (`/1.6/`, `/26/`, …), und `manual.rt-rc.com/` leitet auf diejenige
Version weiter, die aktuell den Alias `latest` trägt. Material zeigt automatisch
ein Auswahlmenü für die Version an und liest dazu `versions.json` (das von `mike`
gepflegt wird) — dies ist unabhängig vom Sprachumschalter und lässt sich sauber
mit ihm kombinieren: Die Version bildet das äußere Pfadsegment, die Sprache
(sobald es mehr als `en` gibt) das innere, z. B. `manual.rt-rc.com/26/fr/...`.

Damit wird derselbe Mechanismus „Unterordner auf `gh-pages`“ wiederverwendet wie
bei den [PR-Vorschauen](index.md#pr-previews) — die Versionsordner von `mike` und
der Ordner `pr-preview/` existieren konfliktfrei auf demselben Branch nebeneinander,
da jeder nur seine eigenen Pfade anfasst.

## Quellstruktur: `main` + eingefrorene Branches

- **`main` bildet stets den Inhalt der aktuellen/neuesten Firmware-Version ab.**
  Die tägliche Bearbeitung findet genau wie bisher hier statt — am normalen
  Beitragsworkflow ändert sich nichts.
- Sobald das Handbuch einer neuen Firmware-Version von dem abweichen muss, was
  auf `main` steht, **wird zuerst ein Branch mit dem Namen der alten Version
  abgezweigt**, z. B. `1.6`, um sie dauerhaft einzufrieren. `main` enthält
  anschließend den Inhalt der neuen Version.
- Ein eingefrorener Branch ist nicht tot — er kann weiterhin über eigene PRs
  Korrekturen erhalten. Er verfolgt lediglich die Entwicklung der neuen Version
  nicht mehr.

## Eine neue Version abzweigen

Wenn das Handbuch der nächsten Version beginnen soll (z. B. Ethos26):

1. Ausgehend von `main` den eingefrorenen Branch für die zurückbleibende Version
   anlegen und pushen:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   Die Kopie von `.github/workflows/deploy.yml` auf `1.6` führt nun bei jedem Push
   auf diesen Branch dauerhaft `mike deploy --push --update-aliases 1.6 latest`
   aus — so wie sie ist korrekt, keine Änderung nötig, da ein Branch ein
   vollständiger Schnappschuss inklusive eigener CI-Konfiguration ist.

2. Auf `main` die Datei `.github/workflows/deploy.yml` bearbeiten: die
   Versionsbezeichnung im Schritt `Deploy version 1.6 with mike` (und dessen Namen)
   von `1.6` auf die Bezeichnung der neuen Version ändern (z. B. `26`). Dies ist die
   **einzige** erforderliche Änderung, um mit der Veröffentlichung der neuen Version
   zu beginnen — der nächste Push auf `main` veröffentlicht sie unter `/26/` und
   verschiebt den Alias `latest` dorthin, während `/1.6/` exakt so bleibt, wie es war.

3. Den Inhalt der neuen Version auf `main` an das anpassen, was sich tatsächlich
   geändert hat — neue/umbenannte Menübereiche, neue Screenshots, aktualisierte
   Terminologie. Der Abschnitt `nav` in `mkdocs.yml` darf sich zwischen den Branches
   beliebig unterscheiden; es gibt keine gemeinsame Konfiguration, die synchron
   gehalten werden müsste.

4. Den Namen des neuen Branches der Trigger-Liste `branches:` in
   `.github/workflows/pr-preview.yml` hinzufügen, wenn auch PRs gegen diesen Branch
   Live-Vorschauen erhalten sollen (bei eingefrorenen Branches ist das in der Regel
   nicht nötig, da dort nur gelegentlich Korrektur-PRs eingehen).

## Screenshots über Versionen hinweg

Screenshots werden aus einem bestimmten Ethos-Build erstellt (siehe
[Screenshot-Pipeline](screenshot-pipeline.md)) und gehören zu dem Branch, dessen
Benutzeroberfläche sie zeigen — eine Versionsabzweigung teilt den Screenshot-Bestand
also ganz natürlich zusammen mit allem anderen auf, sodass `1.6/assets/` und (sobald
für die neue Benutzeroberfläche neu erzeugt) `docs/en/assets/` auf `main` nach dem
Abzweigpunkt unabhängig voneinander auseinanderlaufen.
