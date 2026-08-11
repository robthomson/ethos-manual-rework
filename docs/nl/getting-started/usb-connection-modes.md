---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# USB-verbindingsmodi

![USB-menu](../assets/usbmenu.png)

Wat een USB-verbinding met een pc doet, hangt af van de manier waarop de
zender werd gevoed op het moment dat u de kabel aansloot.

## Modus uitgeschakeld

Wanneer u de zender via USB op een pc aansluit **terwijl deze uitgeschakeld
is**, komt hij in DFU-modus, die gebruikt wordt om de bootloader zelf te
flashen.

## Bootloader-modus {: #bootloader-mode }

Schakel de zender in **terwijl u `ENT` ingedrukt houdt** om op te starten in
de bootloader-modus (het scherm toont "Bootloader"). Als u nu USB aansluit,
verandert de status naar "USB Plugged" en koppelt de pc **twee** schijven
aan: het interne flashgeheugen van de zender en de inhoud van de SD card/eMMC.
Dit is de modus om bestanden direct naar een van beide opslaggebieden te
lezen en te schrijven, en het is ook de manier waarop [Ethos
Suite](../ethos-suite/index.md) de firmware van de zender bijwerkt — zie het
hoofdstuk Bootloader-modus van Ethos Suite zelf.

## Modus ingeschakeld

Wanneer u USB aansluit terwijl de zender **normaal ingeschakeld** is,
verschijnt er een moduskeuze:

- **Joystick** — presenteert de zender als een USB HID-joystick, voor het
  besturen van flightsimulators op de pc.
- **FrSky Suite** — zet de zender in "Ethos mode" voor communicatie met
  [Ethos Suite](../ethos-suite/index.md).
- **Serial** — stuurt Lua-debugtraces via USB-serieel (115200 bps). Het
  tabblad Lua Development Tools van Ethos Suite heeft een geïntegreerde
  terminal om deze weer te geven; mogelijk is een Windows Virtual COM
  Port-driver nodig.
