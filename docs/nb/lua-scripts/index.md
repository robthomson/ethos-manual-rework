---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-skript

Lua-skript gjør det mulig å lage egne [skjermwidgeter](../displays/custom-widgets.md)
som viser informasjon Ethos ikke dekker fra før, og (per modell) egne
[kilder og oppgaver](../model-setup/lua-scripts.md) — et grunnlag som er
planlagt å vokse videre, mot spesialiserte egendefinerte funksjoner og
integrasjon med flykontrollere.

Lua er i seg selv et lett, innebyggbart generelt skriptspråk (brukt overalt
fra spill til nettapplikasjoner); Ethos bygger det inn nettopp for denne
typen tilpasning på senderen.

!!! warning
    Lua-skript øker senderens oppstartstid. Forsinkelsen fra et velskrevet
    skript skal være umerkelig — et dårlig skrevet skript kan forsinke
    oppstarten nesten i det uendelige.

- [Lua-fortolker](lua-interpreter.md) — hvilken Lua-versjon og hvilke
  biblioteker Ethos bygger inn.
- [Ethos Lua-dokumentasjon](ethos-lua-documentation.md) — hvor den fullstendige
  API-referansen finnes.
- [Plassering av eksempelskript](example-script-locations.md) — hvor du finner
  og laster ned fungerende eksempler.
- [Konfigurasjonsgrenser](configuration-limits.md) — minnebudsjett for
  punktgrafikk og skript.
- [Grunnleggende widgetoppbygging](basic-widget-layout.md) — kodestrukturen et
  egendefinert widgetskript trenger.
