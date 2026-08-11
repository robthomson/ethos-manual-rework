---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Waarschuwing accucapaciteit

Waarschuwing op basis van de **verbruikte capaciteit** (mAh) in plaats van
de spanning — een directere maat voor hoeveel van het accupack werkelijk
is verbruikt. Er zijn twee manieren om dit te bereiken, afhankelijk van de
aanwezige hardware.

## Optie A: een ESC uit de Neuron-serie

De Neuron-ESC's van FrSky rapporteren het verbruik direct — er is geen
berekende sensor nodig. Zet [Ontvangeropties →
Telemetrieport](../system-setup/devices.md) op S.Port, sluit de
telemetriedraad van de Neuron aan en [zoek de
sensoren](../model-setup/telemetry.md#discovering-sensors) — de sensor
waar het om gaat is **ESC Consumption**.

1. Voeg een [logische schakelaar](../model-setup/logical-switches.md) toe
   op `ESC Consumption`, waar boven (bijvoorbeeld) 900mAh de voorwaarde
   waar is — ruwweg 60% van een accupack dat zo gedimensioneerd is dat je
   landt met nog ~30% in reserve.
2. Voeg een [speciale functie Play
   audio](../model-setup/special-functions.md) toe, met de nieuwe
   schakelaar als actieve voorwaarde en een stap **Play value** voor
   `ESC Consumption`.

Als tweede beveiligingslaag rapporteren Neuron-ESC's ook **ESC Voltage** —
stel op dezelfde manier een tweede logische schakelaar in als bij
[Waarschuwing lage accuspanning](low-battery-warning.md) (onder 3,4V/cel
gedurende 4s — bijvoorbeeld 13,6V voor een 4S-pack), met een eigen Play
audio-functie die elke 5 seconden wordt herhaald.

## Optie B: een stroomsensor + berekende sensor

Als de ESC het verbruik niet rapporteert, doet een stroomsensor
(bijvoorbeeld FrSky FASxxx) in combinatie met een [berekende sensor
**Consumption**](../model-setup/telemetry.md#calculated-sensors) hetzelfde
werk.

### 1. Aansluiten en zoeken

![Stroomsensor](../assets/how-to-consumption-telemetry-current-sensor.png)

Sluit de S.Port-draad van de stroomsensor aan en zoek de sensor — deze
verschijnt als **Current**. Stel het **Bereik** in overeenkomstig de
sensor (bijvoorbeeld 0–100A voor een FAS100):

![Stroomsensor bewerken](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. De berekende sensor Consumption aanmaken

![Berekende sensor aanmaken](../assets/how-to-consumption-create-calc-select.png)
![Consumption-sensor](../assets/how-to-consumption-create-calc-sensor.png)

Kies in Telemetrie **Berekende sensor aanmaken** → **Consumption**. Stel
de eenheid in op `mAh` en het **Bereik** op de capaciteit van het
accupack (bijvoorbeeld 2800mAh); zet **Bron** op `Current`.

![Sensor bewerken](../assets/how-to-consumption-sensor-edit.png)
![Sensor bewerken 2](../assets/how-to-consumption-sensor-edit2.png)

Zet **Reset** op de systeemgebeurtenis `!Telemetry Active` — selecteer
**Telemetry Active**, houd `ENT` lang ingedrukt en kies **Invert** — zodat
de lopende totaalwaarde automatisch wordt gereset zodra de telemetrie
wegvalt (dus wanneer het model wordt uitgeschakeld).

### 3. Meldingen bij mijlpalen

![Logische schakelaar delta 200mAh](../assets/how-to-consumption-lsw-delta200mAh.png)

Voeg een logische schakelaar toe met de functie **Δ > X** op
`Consumption`, die afgaat telkens wanneer de waarde met een vaste stap
toeneemt — bijvoorbeeld elke 200mAh, een handige fractie van een
2800mAh-pack.

!!! tip
    Zet **Controle-interval** op `---` (oneindig), zodat de waarde
    onbeperkt blijft oplopen richting de volgende drempel in plaats van
    na een vast tijdvenster te worden gereset. Geef **Min. duur** tijdens
    het testen een kleine waarde ongelijk aan nul — bij 0.0 is de trigger
    te kort om op het scherm te zien.

Voeg een Play audio-functie toe, met deze schakelaar als actieve
voorwaarde en een Play value-stap voor `Consumption`:

![Deltamelding afspelen](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Waarschuwing bij lage capaciteit

![Tweede logische schakelaar](../assets/how-to-consumption-lsw2-play-battlow.png)

Een tweede logische schakelaar gaat eenmalig af zodra een harde drempel
voor lage capaciteit wordt overschreden — bijvoorbeeld 2000mAh van een
2800mAh-pack — gekoppeld aan een Play audio-functie die elke 10 seconden
wordt herhaald totdat het model wordt gereset:

![Play value bij lage accu](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value: consumption bij lage accu](../assets/how-to-consumption-sf2-play-value-consumption.png)
