---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# Režimy připojení USB

![Nabídka USB](../assets/usbmenu.png)

Co se stane při připojení vysílače k počítači přes USB, závisí na tom, jak byl
vysílač napájen v okamžiku připojení.

## Režim vypnutého vysílače

Připojení vysílače k počítači přes USB **ve vypnutém stavu** jej přepne do
režimu DFU, který slouží k nahrání samotného bootloaderu.

## Režim bootloaderu {: #bootloader-mode }

Zapněte vysílač **se stisknutým `ENT`**, čímž nastartuje do režimu bootloaderu
(na displeji se zobrazí „Bootloader“). Připojení USB nyní změní stav na
„USB Plugged“ a počítač připojí **dva** disky: interní flash paměť vysílače a
obsah SD karty/eMMC. Tento režim slouží ke čtení a zapisování souborů přímo do
kteréhokoli z obou úložišť a rovněž jej využívá [Ethos
Suite](../ethos-suite/index.md) k aktualizaci firmwaru vysílače — viz vlastní
oddíl Ethos Suite o režimu bootloaderu.

## Režim zapnutého vysílače

Připojení USB při **normálně zapnutém vysílači** vyvolá nabídku volby režimu:

- **Joystick** — vysílač se hlásí jako USB HID joystick pro ovládání
  leteckých simulátorů na počítači.
- **FrSky Suite** — přepne vysílač do „Ethos mode“ pro komunikaci
  s [Ethos Suite](../ethos-suite/index.md).
- **Serial** — přesměruje ladicí výstupy Lua přes USB-serial (115200 bps).
  Karta Lua Development Tools v Ethos Suite obsahuje integrovaný terminál pro
  jejich zobrazení; ve Windows může být zapotřebí ovladač virtuálního COM portu.
