---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# USB-tilkoblingsmoduser

![USB-meny](../assets/usbmenu.png)

Hva en USB-tilkobling til en PC gjør, avhenger av hvordan senderen var
strømsatt da du koblet den til.

## Avslått modus

Når senderen kobles til en PC via USB **mens den er avslått**, settes den i
DFU-modus, som brukes til å flashe selve bootloaderen.

## Bootloader-modus {: #bootloader-mode }

Slå på senderen **med `ENT` holdt inne** for å starte i bootloader-modus
(skjermen viser «Bootloader»). Når USB kobles til nå, endres statusen til
«USB Plugged», og PC-en monterer **to** disker: senderens interne
flashminne, og innholdet på SD card/eMMC. Dette er modusen for å lese og
skrive filer direkte til begge lagringsområdene, og det er også slik [Ethos
Suite](../ethos-suite/index.md) oppdaterer senderens firmware — se Ethos
Suites eget avsnitt om bootloader-modus.

## Påslått modus

Når USB kobles til mens senderen er **slått på som normalt**, vises en
modusvelger:

- **Joystick** — presenterer senderen som en USB HID-joystick, for å styre
  flysimulatorer på PC.
- **FrSky Suite** — setter senderen i «Ethos-modus» for kommunikasjon med
  [Ethos Suite](../ethos-suite/index.md).
- **Serial** — sender Lua-feilsøkingsmeldinger over USB-serieport (115200
  bps). Fanen Lua Development Tools i Ethos Suite har en integrert terminal
  for å vise dem; det kan være nødvendig med en driver for virtuell
  COM-port i Windows.
