---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![Maskinvaresjekk X20 Pro](../assets/system-hardware-check-x20pro.png)

Forskjeller fra X20S-grunnlaget denne håndboken er skrevet for —
disse gjelder for **X20 Pro**, og i hovedsak også for **X20 Pro AW**
og **X20R/RS**-familien.

- **Lagring** — internt 8GB eMMC som standard, SD card som tilvalg — se
  [Generelt → Lagringsplassering](../system-setup/general.md#storage-location-x18-and-x20-prorrs).
- **Ekstra trim** — legger til trimbryterne **T5** og **T6** — se
  [Trim](../model-setup/trims.md#trim-settings).
- **Ekstra brytere** — to låsende trykknappbrytere, **K** og **L**,
  på de bakre skuldrene, i tillegg til bryterposisjonene **M**/**N** dersom
  de er tilkoblet (vanligvis brytere i spakendene) — se [Maskinvare →
  Brytere](../system-setup/hardware.md#switches-settings).
- **Ekstra potensiometere** — **Ext1**/**Ext2**, vanligvis brukt med 3-akse
  gimbaler — se [Maskinvare → Potensiometere/glidebrytere](../system-setup/hardware.md#potssliders-settings).
  Dette forskyver indeksen i [ADC-verdiinspektøren](../system-setup/hardware.md#adc-value-inspector):
  Ext1/Ext2 ligger mellom Pot2 og glidebryterne.
- **Haptisk tilbakemelding** — **X20 Pro AW** og **X20RS** leveres med MC20R-gimbaler
  med innebygde haptiske vibrasjonsmotorer (stick-shaker); en **X20 Pro** eller
  **X20R** kan få det samme ved å ettermontere en MC20R-gimbaloppgradering, som
  aktiveres under [Maskinvare → Aktivere haptiske
  gimbaloppgraderinger](../system-setup/hardware.md#radio-specific-hardware-options).
  Når funksjonen er aktivert, gir [Velg haptiske
  motorer](../model-setup/special-functions.md#actions) valgene Standard,
  Alle motorer, Venstre spak eller Høyre spak.
- **Rotasjonsenkoder** — X20 Pro AW og X20R/RS bruker en mer følsom
  enkoder; alternativet **halve steg** under [Maskinvare →
  Enkoderalternativ](../system-setup/hardware.md#radio-specific-hardware-options)
  demper følsomheten.
- **Intern RF-modul** — X20 Pro/R/RS bruker modulen **TD-ISRM Pro**
  (LoRa-kompatibel, med tandem dobbeltbånd- og TD-Pro-moduser i
  tillegg til ACCESS/ACCST D16), i stedet for TD-ISRM-modulen i
  X18/X20/X20S/X20HD — se [RF-system](../model-setup/rf-system.md).
