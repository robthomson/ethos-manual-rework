---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Waarschuwingen

![Waarschuwingen](../assets/system-alerts.png)

Vier zenderbrede waarschuwingen, elk afzonderlijk in- en uitschakelbaar — los van
de per-model [speciale functies](../model-setup/special-functions.md)
en [logische schakelaars](../model-setup/logical-switches.md) die u zelf
opbouwt.

- **Stille modus** — een gesproken melding bij het opstarten wanneer deze controle
  is ingeschakeld en [Algemeen → Audiomodus](general.md) op Stil staat, als
  herinnering dat de zender gedempt is.
- **Hoofdspanning** — "Radio battery is low" wanneer de hoofdaccu van de zender
  onder de drempelwaarde **Lage spanning** komt die is ingesteld in [Batterij](battery.md).
- **RTC-spanning** — "RTC battery is low" wanneer de RTC-knoopcel onder
  2,5 V komt (de standaarddrempel). Datalogging is afhankelijk van de real-time
  klok; een ongeldige tijd maakt logbestanden moeilijk leesbaar, met name bij het
  onderscheiden van vluchtsessies. Dit kan tijdelijk worden uitgeschakeld terwijl
  u wacht om de batterij te vervangen, maar mag niet permanent uit blijven staan.
- **Waarschuwing sensorconflict** — detecteert conflicterende telemetrie-sensor-ID's.
  Uitschakelen is alleen zinvol als u sensoren hebt die niet aan de S.Port-specificatie
  voldoen.
- **Inactiviteit** — een gesproken melding "Prolonged inactivity" (plus een
  trilsignaal, voor het geval het volume laag staat) nadat de zender langer dan
  de ingestelde tijd ongebruikt is gebleven — standaard 10 minuten.
