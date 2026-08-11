---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Umiddelbar tilbaketaking for Trainer-funksjonen

En nyttig utvidelse av [Trainer](../model-setup/trainer.md)-funksjonen:
istedenfor bare en bryter kan instruktøren ta tilbake kontrollen
umiddelbart bare ved å bevege spaken for krengeror eller høyderor — uten
å måtte finne trainer-bryteren først dersom noe går galt.

Trainer-bryteren starter fortsatt økten, mens en [Sticky logisk
bryter](../model-setup/logical-switches.md#sticky) styrer selve
trainer-funksjonen. Den avbrytes enten ved at bryteren slås av **eller**
ved at det oppdages spakbevegelse fra instruktøren.

![Trainer aktiv](../assets/trainer-take-back-trainer-active.png)

## 1. Logisk bryter for deteksjon av krengeror

![Deteksjon av krengeror-inngang](../assets/trainer-take-back-ailinput.png)

En logisk bryter som bruker **|A| > X** på krengeror-spaken, og som er
sann når spaken beveges mer enn 10 % fra midtstilling i en av retningene.
Trykk lenge på krengeror-kilden og velg **Ignore trainer input**, slik at
*elevens* krengeror-bevegelse (som kommer inn via trainer-forbindelsen)
ikke også utløser den:

![Ignore trainer input](../assets/trainer-take-back-ailinput-ignore.png)

## 2. Logisk bryter for deteksjon av høyderor

![Deteksjon av høyderor-inngang](../assets/trainer-take-back-eleinput.png)

Samme mønster, men på høyderor-spaken.

## 3. Logisk bryter for avbrytelse

En logisk bryter av typen **OR**, som er sann når enten
krengeror-deteksjonen eller høyderor-deteksjonen er sann, **eller** når
trainer-bryteren (f.eks. SD) ikke står nede — det vil si at enten
«instruktøren beveget en spak» eller «trainer-bryteren ble slått av»
avslutter økten.

## 4. Sticky logisk bryter for aktivering av trainer

![Deaktiver trainer](../assets/trainer-take-back-disable-trainer.png)

En **Sticky** logisk bryter: **Trigger ON** er trainer-bryteren (SD
nede), og **Trigger OFF** er avbrytelsesbryteren fra trinn 3. Bruk denne
Sticky-bryteren — kall den `TrainerActive` — som aktiveringsvilkår for
Trainer-funksjonen istedenfor selve bryteren.

## 5. Lydtilbakemelding

Legg til [spesialfunksjoner av typen Play
Audio](../model-setup/special-functions.md) som varsler når
`TrainerActive` blir sann og når den nullstilles, slik at begge pilotene
får et tydelig hørbart signal om nøyaktig når kontrollen skifter hender.
