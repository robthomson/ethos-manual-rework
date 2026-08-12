# Alternative Display Themes

New in Ethos 26.1: beyond the built-in **Dark** and **Light** themes (see
[System Setup → General](../system-setup/general.md)), a Lua script can
install additional selectable themes.

Four example themes are provided in the `lua/examples/theme` folder of the
26.1 branch of [ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/tree/main/lua)
on GitHub:

- **Dark (Ethos 1.6)** — the colors and shading from Ethos 1.6.6, for
  anyone who prefers the previous look.
- **Dark Outline** — the default Dark theme's colors, but with a 2px
  outline focus style instead of inverted highlighting.
- **Dark (Copy)** / **Light (Copy)** — commented-out copies of the two
  built-in themes, meant as a starting point to write your own.

## Installing

Following [Example Script Locations](example-script-locations.md), download
the `theme/main.lua` file (or the whole `theme` folder) into a `theme`
folder under `scripts/` on the SD card/eMMC, then restart the radio. The
installed themes then appear in **System → General → Theme**:

![Theme selection](../assets/system-general-theme-select.png)

The **Dark Outline** example, selected:

![Dark Outline theme example](../assets/system-general-theme-outline-example.png)
