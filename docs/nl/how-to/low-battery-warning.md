---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Waarschuwing voor lage accuspanning

Het bewaken van de spanning van de vluchtaccu **onder belasting** en het
waarschuwen zodra deze onder een drempelwaarde komt, is een
betrouwbaardere aanpak dan het vertrouwen op een vaste timer — met een
sensor zoals de FrSky FLVSS is dit eenvoudig te realiseren.

## 1. Sensor aansluiten en detecteren

![LiPo-telemetriesensor](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Zet [Ontvangeropties → Telemetriepoort](../system-setup/devices.md) op
**S.Port**, sluit de FLVSS met een S.Port-kabel op de ontvanger aan en
schakel vervolgens **Nieuwe sensoren zoeken** in onder
[Telemetrie](../model-setup/telemetry.md) — de LiPo-sensor verschijnt naast
de sensoren die al gedetecteerd zijn.

## 2. Een logische schakelaar toevoegen

![Logische schakelaar voor lage accuspanning](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Voeg een nieuwe [logische
schakelaar](../model-setup/logical-switches.md) toe met de LiPo-sensor als
bron. Houd `ENT` lang ingedrukt op de gemarkeerde sensor om te kiezen
welke van de bijbehorende waarden gebruikt wordt:

![Laagste cel selecteren](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Minimale pakspanning / Maximale pakspanning
- **Laagste celspanning** / Hoogste celspanning
- Aantal cellen
- Individuele celspanningen (alleen selecteerbaar zolang de sensor
  daadwerkelijk is aangesloten op een gebonden ontvanger met een
  aangesloten LiPo)

Selecteer **Laagste** (celspanning) — de waarde die van belang is voor
LVC-achtige bescherming.

![Laagste cel geselecteerd](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Stel de vergelijkingswaarde in op ongeveer **3,4V** en **Vertraging voor
activering** op **4 seconden** — de schakelaar wordt waar zodra de laagste
cel gedurende 4 s of langer aaneengesloten onder 3,4V per cel uitkomt.
(3,4V *onder belasting* herstelt doorgaans tot ongeveer 3,7V zodra de
belasting wegvalt, dus deze drempelwaarde duidt op een werkelijke
spanningsval en niet slechts op kortstondige ruis.)

![Voltooide logische schakelaar](../assets/how-to-low-batt-lsw-summary.png)

## 3. Een speciale functie toevoegen

![Speciale functie: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Voeg een [speciale functie Audio
afspelen](../model-setup/special-functions.md) toe, stel **Actieve
conditie** in op de logische schakelaar `BattLow`, kies een stem en voeg
onder **Reeks** een stap **Waarde afspelen** toe voor de totale
LiPo-spanning:

![Waarde afspelen: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Overzicht van de reeks](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

Met **Herhalen** ingesteld op 10 seconden wordt de LiPo-spanning elke 10 s
uitgesproken zolang de laagste cel onder de drempelwaarde van 3,4V/4 s
blijft.
