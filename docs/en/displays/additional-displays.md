# Additional Displays

![Screen config options](../assets/display-screen-config-options.png)

The default model comes with one screen (a model bitmap plus three timer
widgets), but up to **eight** screens total are supported. Tap the **+**
next to "Screen1" to add another:

- Choose from **15** layouts, including two dedicated home-screen layouts
  and a full-screen option, holding up to 9 widgets — configured exactly
  like the first screen.
- Screens can be reordered or deleted from their own edit dialog (tap
  Screen1, Screen2, etc.).

## Worked example

![Main view](../assets/display-main-view.png)

A typical layout: the model bitmap (configured in [Model Edit →
Picture](../model-setup/model-edit.md)) on the left, with receiver
battery voltage, RSSI, and a "Throttle ACTIVE" Status widget (a
community-built Lua widget from the *FrSky - ETHOS Lua Script
Programming* rcgroups thread) stacked on the right. Tapping any widget
opens its configuration, or jumps to the main Configure Screens function.

## Screen-level options

Beyond individual widgets, each screen has its own settings — layout grid
size, background, and which screens are included in the `PAGE` cycle.

See [Displays](index.md) for the widgets themselves, and [Custom
Widgets](custom-widgets.md) for adding Lua-scripted widgets beyond the
built-in set.
