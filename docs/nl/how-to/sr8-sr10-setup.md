---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# SR8/SR10 modelinstellingen en kanalen herschikken

De gestabiliseerde SRx-ontvangers van FrSky verwachten een specifieke kanaalvolgorde. Er zijn twee scenario's: een nieuw model volledig vanaf nul opbouwen, of een bestaand model aanpassen.

!!! note "Schermafbeeldingen volgen nog"
    Deze pagina heeft nog geen schermafbeeldingen uit de simulator — zie [Screenshot Pipeline](../contributing/screenshot-pipeline.md).

## Een nieuw model aanmaken

De wizard van [Modelkeuze](../model-setup/model-select.md) groepeert standaard roervlakken met dezelfde functie (bijv. 2 rolroeren → `AAETR`), maar SRx-ontvangers vereisen dat de eerste vier kanalen vast op **AETRA** staan.

1. Controleer in [Controls](../system-setup/controls.md) of **Kanaalvolgorde** op `AETR` staat.
2. Schakel **[Eerste vier kanalen vast](../system-setup/controls.md#first-four-channels-fixed)** in — hierdoor groepeert de wizard de eerste vier kanalen niet en blijven ze strikt in de volgorde `AETRA…`, ongeacht hoeveel roervlakken van elk type het model heeft.
3. Doorloop de wizard voor het aanmaken van het model zoals gebruikelijk — de eerste 5 kanalen komen er als `AETRA` uit.

!!! note "Zelftest van Archer-ontvangers"
    De zelftest voor Archer-ontvangers verloopt nu via [Apparaatconfiguratie → SxR](../system-setup/devices.md) (firmware v2.1.10+) in plaats van via een aparte zelftestprocedure. Het gaskanaal moet op −100% staan, anders start de zelftest niet.

## Een bestaand model herschikken

Het omzetten van een bestaand model (bijv. momenteel `AAETRFF`) naar de volgorde voor gestabiliseerde ontvangers (`AETRAE`, daarna kanaal 9 Gain, 10/11 vluchtmodi, 12 zelftest bij oudere SxR-units) bestaat uit een reeks kanaalwisselingen in [Uitgangen](../model-setup/outputs.md#swap-channels).

Uitgangspunt:

| Kan | Functie |
|---|---|
| 1 | Rolroer1 (rechts) |
| 2 | Rolroer2 (links) |
| 3 | Hoogteroer |
| 4 | Gas |
| 5 | Richtingsroer |
| 6 | Flap1 (rechts) |
| 7 | Flap2 (links) |
| 8 | Intrekbaar landingsgestel |

Doelvolgorde: `AETRAE` — Kan1 Rolroer1, Kan2 Hoogteroer, Kan3 Gas, Kan4 Richtingsroer, Kan5 Rolroer2, Kan6 Hoogteroer2/AUX2 (daarna Gain/vluchtmodi/zelftest op 9–12).

1. **Zet Rolroer2 eerst uit de weg**: selecteer in Uitgangen CH2 (Rolroer2), tik nogmaals, kies **Kanalen wisselen** en wissel het met een ongebruikt kanaal (bijv. CH9). De wisseling wordt direct doorgevoerd — elke mix die naar een van beide kanalen verwijst, wordt automatisch bijgewerkt.
2. **Wissel CH3 (Hoogteroer) → CH2.**
3. **Wissel CH4 (Gas) → CH3.**
4. **Wissel CH5 (Richtingsroer) → CH4.**
5. **Wissel CH9 (Rolroer2, in stap 1 geparkeerd) → CH5.**

Resultaat:

| Kan | Functie |
|---|---|
| 1 | Rolroer1 (rechts) |
| 2 | Hoogteroer |
| 3 | Gas |
| 4 | Richtingsroer |
| 5 | Rolroer2 (links) |
| 6 | Flap1 (rechts) |
| 7 | Flap2 (links) |
| 8 | Intrekbaar landingsgestel |

— nu in de volgorde die gestabiliseerde FrSky-ontvangers verwachten.
