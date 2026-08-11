---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Batterij

![Batterij-instellingen van de zender](../assets/system-battery.png)

Kalibreert de meting van de interne batterij van de zender en stelt de
alarmdrempels in — dit staat los van de instellingen voor het vluchtpakket
van een model (zie [Handleiding: Waarschuwing bij lage
accuspanning](../how-to/low-battery-warning.md)).

- **Hoofdspanning** — toont de huidige meetwaarde en dient tevens als
  kalibratie-instelling: voer de werkelijke spanning in zoals gemeten met
  een multimeter. Standaard is 8,4 V (een volledig geladen 2S Li-ion-pakket).
- **Lage spanning** — de alarmdrempel, standaard 7,2 V (7,4 V geeft extra
  marge). Wanneer de [waarschuwing voor
  hoofdspanning](alerts.md) is ingeschakeld, veroorzaakt het zakken onder
  deze waarde een waarschuwingsvenster en elke minuut een gesproken melding
  "Radio battery is low", ongeacht of het venster geopend is.

  !!! warning
      Land en laad de zenderaccu zodra deze waarschuwing klinkt — hij wordt
      elke minuut herhaald. Bij 6,0 V schakelt de zender onvoorwaardelijk uit
      om de 2×3,0 V Li-ion-cellen te beschermen.

- **Weergegeven spanningsbereik** — de min./max. waarden voor de grafische
  batterijweergave in de rechterbovenhoek: MIN is de waarde waarbij het
  eerste balksegment dooft, MAX de waarde waarbij het vierde oplicht. De
  standaardwaarden zijn 6,4–8,4 V voor het ingebouwde Li-ion-pakket; veel
  piloten verhogen de ondergrens om eerder een waarschuwing voor lage
  spanning te krijgen en te diep ontladen te voorkomen. Stel deze waarden af
  op het batterijtype dat daadwerkelijk is geïnstalleerd.
- **RTC-spanning** — de spanning van de knoopcel voor de realtimeklok. 3,0 V
  wanneer nieuw; vervang de cel onder 2,7 V om de klok nauwkeurig te houden,
  en verwacht de [waarschuwing voor RTC-spanning](alerts.md) onder 2,5 V.
