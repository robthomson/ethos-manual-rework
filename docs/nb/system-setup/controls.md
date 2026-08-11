---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Kontroller

![Spaker](../assets/system-sticks.png)

Kalles **Sticks** i menyen – spakmodus og standard rekkefølge for
kanaltilordning.

## Spakmodus

- **Modus 1** – gass og krengeror på høyre spak, høyderor og sideror på
  venstre.
- **Modus 2** – gass og sideror på venstre spak, krengeror og høyderor på
  høyre.

Spakene er som standard navngitt etter de bransjestandardiserte modusene,
og kan gis nye navn.

## Kanalrekkefølge

Definerer rekkefølgen de fire spakinngangene tilordnes kanaler i når en ny
modell opprettes av veiviserne i [Modellvalg](../model-setup/model-select.md).
Standard er **AETR**. Der en flystruktur har mer enn ett av et gitt ror,
grupperes de sammen med mindre [Første fire kanaler
fast](#first-four-channels-fixed) er slått på – for eksempel blir 2
krengeror **AAETR**.

![Kanalrekkefølge for mottaker](../assets/system-sticks-rx-order.png)

## Første fire kanaler fast {: #first-four-channels-fixed }

Når dette er aktivert, grupperes aldri de fire første kanalene. Med
rekkefølgen **AETR** og en flystruktur med 2 krengeror, 1 høyderor, 1
motor, 1 sideror og 2 flaps, produserer veiviseren **AETRAFF** (kanal 1–4
forblir nøyaktig A-E-T-R, med det andre krengeroret og begge flaps lagt til
etterpå) i stedet for **AAETRFF**. Dette er innstillingen som gjør at
veiviseren bygger modeller tilpasset SRx-stabiliserte mottakere, som
forventer nettopp dette faste oppsettet.

![Fast rekkefølge for 4 kanaler](../assets/system-sticks-4ch-fixed.png)
