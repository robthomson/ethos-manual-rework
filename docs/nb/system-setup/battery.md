---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Batteri

![Innstillinger for senderbatteri](../assets/system-battery.png)

Kalibrerer senderens interne batterimåling og angir alarmgrenser — dette er
skilt fra en modells innstillinger for flypakken (se [Praktisk guide:
Varsel om lav batterispenning](../how-to/low-battery-warning.md)).

- **Hovedspenning** — viser gjeldende måling, og fungerer samtidig som
  kalibreringsjustering: legg inn den faktiske spenningen målt med et
  multimeter. Standardverdien er 8,4 V (en fullt ladet 2S Li-ion-pakke).
- **Lav spenning** — alarmgrensen, standard 7,2 V (7,4 V gir ekstra
  margin). Når [varsel om hovedspenning](alerts.md) er aktivert, utløser
  spenningsfall under denne grensen en varseldialog og et talevarsel,
  «Radio battery is low», hvert minutt, uansett om dialogen er åpen eller
  ikke.

  !!! warning "Advarsel"
      Land og lad senderbatteriet så snart dette varselet lyder — det
      gjentas hvert minutt uansett. Ved 6,0 V slår senderen seg av
      ubetinget for å beskytte de to Li-ion-cellene på 3,0 V.

- **Visningsspenningsområde** — min/maks for den grafiske batterivisningen
  øverst i høyre hjørne: MIN er der det første stolpesegmentet slukker,
  MAX er der det fjerde tennes. Standardverdiene er 6,4–8,4 V for den
  innebygde Li-ion-pakken; mange piloter hever den nedre grensen for å få
  et tidligere varsel om lav spenning og unngå å utlade batteriet for
  dypt. Still disse verdiene slik at de passer til batteritypen som
  faktisk er montert.
- **RTC-spenning** — spenningen til knappcellen for sanntidsklokken. 3,0 V
  når den er ny; bytt den ut når spenningen er under 2,7 V for at klokken
  skal holde seg nøyaktig, og forvent [varsel om RTC-spenning](alerts.md)
  under 2,5 V.
