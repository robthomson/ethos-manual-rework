---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Vluchtmodi

![Vluchtmodi](../assets/model-fm.png)

Met vluchtmodi (vluchtfasen) kunt u met een schakelaar kiezen tussen
verschillende gedragingen voor hetzelfde model — zwevers gebruiken
bijvoorbeeld Start/Kruisvlucht/Snelheid/Thermiek, motormodellen
Normaal/Opstijgen/Landen, helikopters Normaal (opstarten,
opstijgen/landen) / Idle Up 1 (aerobatics) / Idle Up 2 (3D). Ze nemen de
piloot het grootste deel van het handmatige schakelen en hertrimmen uit
handen: een vluchtmodus kan zijn eigen onafhankelijke trims meenemen en kan
zowel [Vars](variables.md) als [Mixen](mixes.md) vrijgeven — gecombineerd
is dat genoeg voor werkelijk complexe opzetten. Zie [Eenvoudig voorbeeld
met vaste vleugel](../tutorials/basic-fixed-wing.md) voor vluchtmodi
toegepast op een echt model.

Standaard zijn er geen vluchtmodi gedefinieerd. Tik op de standaard
vluchtmodus en kies **Bewerken** om deze een andere naam te geven, of
**Toevoegen** om een nieuwe aan te maken — maximaal 20 in totaal.

## Naam

Een omschrijvende naam — Kruisvlucht, Snelheid, Thermiek, Opstijgen,
Landen, wat ook past.

## Actieve conditie

![Vluchtmodusformulier](../assets/model-fm-form.png)

Een nieuwe vluchtmodus begint als inactief (`---`). Zodra deze is
ingesteld, kan hij worden gestuurd door een schakelaar- of knoppositie,
een functieschakelaar, een logische schakelaar, een systeemgebeurtenis
(gas-afsnijding/gas vasthouden) of een trimpositie.

De **standaard** vluchtmodus heeft helemaal geen actieve conditie — dit is
de modus die actief is zodra de conditie van geen enkele andere vluchtmodus
waar is. Er is altijd slechts één vluchtmodus tegelijk actief: de eerste
(in prioriteitsvolgorde) waarvan de conditie op dat moment waar is. De
actieve modus wordt vet weergegeven.

!!! warning "Een vluchtmodus toevoegen aan een bestaand model"
    Een nieuw toegevoegde vluchtmodus is standaard actief in elke mix die
    al vluchtmodus-afhankelijk is — controleer of elk van die mixen zich
    nog correct gedraagt, in het bijzonder een **Lock**-mix die een kanaal
    aan een specifieke vluchtmodus vastzet.

## Fade in, fade out

Overgangstijden om vloeiend tussen vluchtmodi over te vloeien (bijv. 1
seconde in beide richtingen) — dit heeft alleen effect op mixen die zelf
vluchtmodus-afhankelijk zijn.

## Beheer van vluchtmodi

![Vluchtmodus verplaatsen](../assets/model-fm-move.png)
![Selecteren om te verplaatsen](../assets/model-fm-move-select.png)
![Modi 0-3](../assets/model-fm-0to3.png)

Tik op een vluchtmodus voor **Bewerken**, **Toevoegen**, **Klonen** of
**Verwijderen**. Een **gekloonde** vluchtmodus neemt de instellingen van
de bronmodus over in elke mix die vluchtmodi gebruikt — hetzelfde gedrag,
dezelfde actieve/inactieve status — daarom wordt een kloon standaard als
laatste vluchtmodus toegevoegd, om bestaande modi niet te verstoren. Met
**Verplaatsen** wijzigt u de prioriteit van een vluchtmodus: de prioriteit
loopt in oplopende volgorde en (zoals hierboven) de eerste waarvan de
conditie waar is, is de actieve.
