---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Varsler

![Varsler](../assets/system-alerts.png)

Fire varsler som gjelder for hele senderen, hver med sin egen av/på-bryter — atskilt
fra [spesialfunksjonene](../model-setup/special-functions.md)
og [logiske bryterne](../model-setup/logical-switches.md) du selv setter opp
per modell.

- **Stillemodus** — et talevarsel ved oppstart når denne kontrollen er slått på og
  [Generelt → Lydmodus](general.md) er satt til Stille, som en påminnelse om at
  senderen er dempet.
- **Hovedspenning** — "Radio battery is low" når senderens hovedbatteri
  faller under terskelen **Lav spenning** som er satt i [Batteri](battery.md).
- **RTC-spenning** — "RTC battery is low" når RTC-knappcellen faller
  under 2,5 V (standardterskelen). Datalogging er avhengig av sanntidsklokken;
  et ugyldig klokkeslett gjør loggene vanskelige å lese, særlig når man skal
  skille flyøktene fra hverandre. Dette kan dempes midlertidig mens man venter på
  å skifte batteriet, men bør ikke stå avslått i det uendelige.
- **Advarsel om sensorkonflikt** — oppdager telemetrisensorer med motstridende ID-er.
  Bare verdt å slå av dersom du har sensorer som ikke oppfyller S.Port-
  spesifikasjonen.
- **Inaktivitet** — et talevarsel, "Prolonged inactivity" (i tillegg til en
  vibrasjon, i tilfelle volumet er skrudd ned), etter at senderen har stått
  ubrukt lenger enn den innstilte tiden — 10 minutter som standard.
