---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua skripty

Lua skripty umožňují vytvářet vlastní [widgety pro displej](../displays/custom-widgets.md),
které zobrazují informace, jež Ethos nativně nepokrývá, a (pro každý model)
vlastní [zdroje a úlohy](../model-setup/lua-scripts.md) — základ, jehož další
rozvoj je plánován směrem ke specializovaným vlastním funkcím a integraci
s letovými kontroléry.

Lua je sama o sobě odlehčený, vestavitelný skriptovací jazyk pro obecné použití
(používaný všude od her po webové aplikace); Ethos jej vestavuje právě pro
tento druh přizpůsobení přímo ve vysílači.

!!! warning
    Lua skripty prodlužují dobu startu vysílače. U dobře napsaného skriptu
    by mělo být zpoždění nepostřehnutelné — špatně napsaný skript může start
    zdržet téměř na neurčito.

- [Lua interpret](lua-interpreter.md) — jakou verzi Lua a které knihovny
  Ethos vestavuje.
- [Dokumentace Ethos Lua](ethos-lua-documentation.md) — kde najdete kompletní
  referenci API.
- [Umístění ukázkových skriptů](example-script-locations.md) — kde najít
  a stáhnout funkční příklady.
- [Konfigurační limity](configuration-limits.md) — paměťové limity pro
  bitmapy a skripty.
- [Základní rozvržení widgetu](basic-widget-layout.md) — struktura kódu,
  kterou skript vlastního widgetu potřebuje.
