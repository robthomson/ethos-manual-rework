# Lua Scripts

Lua scripts let you build custom [display widgets](../displays/custom-widgets.md)
to show information Ethos doesn't natively cover, and (per model) custom
[sources and tasks](../model-setup/lua-scripts.md) — a foundation planned
to grow further, toward specialized custom functions and flight
controller integration.

Lua itself is a lightweight, embeddable general-purpose scripting
language (used everywhere from games to web apps); Ethos embeds it for
exactly this kind of on-radio customization.

!!! warning
    Lua scripts add to the radio's startup time. A well-written script's
    delay should be unnoticeable — a poorly written one can delay startup
    almost indefinitely.

- [Lua Interpreter](lua-interpreter.md) — which Lua version and libraries
  Ethos embeds.
- [Ethos Lua Documentation](ethos-lua-documentation.md) — where the full
  API reference lives.
- [Example Script Locations](example-script-locations.md) — where to find
  and download working examples.
- [Configuration Limits](configuration-limits.md) — memory budgets for
  bitmaps and scripts.
- [Basic Widget Layout](basic-widget-layout.md) — the code structure a
  custom widget script needs.
- [Alternative Display Themes](alternative-display-themes.md) — installing
  extra selectable themes beyond Dark/Light.
