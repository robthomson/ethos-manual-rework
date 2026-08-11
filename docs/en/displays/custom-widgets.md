# Custom Widgets

Beyond the [built-in widget types](index.md), Lua scripts can implement
entirely custom widgets — typically a single `main.lua` file kept in a
subfolder named for what it does.

## Installing one

Copy the widget's subfolder into `scripts/` on the SD card/eMMC (see
[File Manager](../system-setup/file-manager.md#top-level-folders)). It
registers itself automatically at the next startup, and from then on
appears in the **Change widget** category picker in [Configure
Screens](additional-displays.md) alongside the built-in types — configured
exactly the same way.

## Writing one

See [Lua Scripts → Basic Widget Layout](../lua-scripts/basic-widget-layout.md)
for the code structure a widget script needs to implement.
