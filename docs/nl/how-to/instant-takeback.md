---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Directe overname voor de trainerfunctie

Een nuttige uitbreiding van de [Trainer](../model-setup/trainer.md)-functie:
in plaats van uitsluitend een schakelaar kan de instructeur de besturing
onmiddellijk terugnemen door simpelweg de rolroer- of hoogteroerstick te
bewegen — er hoeft niet eerst naar de trainerschakelaar gezocht te worden
als er iets misgaat.

De trainerschakelaar start de sessie nog steeds; een [Sticky logische
schakelaar](../model-setup/logical-switches.md#sticky) stuurt de
trainerfunctie zelf aan, die wordt beëindigd doordat de schakelaar
uitgaat **of** doordat stickbeweging van de instructeur wordt
gedetecteerd.

![Trainer actief](../assets/trainer-take-back-trainer-active.png)

## 1. Logische schakelaar voor rolroerdetectie

![Rolroerinvoer detecteren](../assets/trainer-take-back-ailinput.png)

Een logische schakelaar met **|A| > X** op de rolroerstick, waar wanneer
deze in beide richtingen meer dan 10% uit het midden beweegt.
Houd de rolroerbron lang ingedrukt en selecteer **Trainerinvoer negeren**,
zodat de rolroerbeweging van de *leerling* (die via de trainerverbinding
binnenkomt) de schakelaar niet ook activeert:

![Trainerinvoer negeren](../assets/trainer-take-back-ailinput-ignore.png)

## 2. Logische schakelaar voor hoogteroerdetectie

![Hoogteroerinvoer detecteren](../assets/trainer-take-back-eleinput.png)

Hetzelfde principe, maar op de hoogteroerstick.

## 3. Logische schakelaar voor beëindiging

Een **OR** logische schakelaar, waar wanneer de rolroerdetectie- of de
hoogteroerdetectieschakelaar waar is, **of** wanneer de trainerschakelaar
(bijvoorbeeld SD) niet omlaag staat — dus zowel "instructeur heeft een
stick bewogen" als "trainerschakelaar uitgezet" beëindigt de sessie.

## 4. Sticky logische schakelaar voor trainerinschakeling

![Trainer uitschakelen](../assets/trainer-take-back-disable-trainer.png)

Een **Sticky** logische schakelaar: **Trigger ON** is de trainerschakelaar
(SD omlaag), **Trigger OFF** is de beëindigingsschakelaar uit stap 3.
Gebruik deze Sticky-schakelaar — noem hem `TrainerActive` — als
activeringsvoorwaarde van de Trainer-functie zelf, in plaats van de
schakelaar zelf.

## 5. Audiofeedback

Voeg [speciale functies Play Audio](../model-setup/special-functions.md)
toe die aankondigen wanneer `TrainerActive` waar wordt en wanneer deze
weer vervalt, zodat beide piloten een duidelijk hoorbaar signaal krijgen
op het exacte moment dat de besturing van hand wisselt.
