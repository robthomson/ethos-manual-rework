---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-scripts

Met Lua-scripts kunt u eigen [display-widgets](../displays/custom-widgets.md)
bouwen om informatie weer te geven die Ethos zelf niet ondersteunt, en (per model) eigen
[bronnen en taken](../model-setup/lua-scripts.md) maken — een basis die
nog verder zal worden uitgebreid, richting gespecialiseerde eigen functies en integratie met
flightcontrollers.

Lua zelf is een lichtgewicht, insluitbare scripttaal voor algemeen gebruik
(toegepast in alles van games tot webapplicaties); Ethos sluit Lua in voor
precies dit soort aanpassingen op de zender.

!!! warning
    Lua-scripts verlengen de opstarttijd van de zender. De vertraging van een goed
    geschreven script is nauwelijks merkbaar — een slecht geschreven script kan het opstarten
    vrijwel onbeperkt vertragen.

- [Lua-interpreter](lua-interpreter.md) — welke Lua-versie en bibliotheken
  Ethos insluit.
- [Ethos Lua-documentatie](ethos-lua-documentation.md) — waar de volledige
  API-referentie te vinden is.
- [Locaties van voorbeeldscripts](example-script-locations.md) — waar u werkende
  voorbeelden kunt vinden en downloaden.
- [Configuratielimieten](configuration-limits.md) — geheugenbudgetten voor
  bitmaps en scripts.
- [Basisopbouw van een widget](basic-widget-layout.md) — de codestructuur die een
  eigen widgetscript nodig heeft.
