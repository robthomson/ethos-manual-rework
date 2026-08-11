# Main Views

## Home screen

![Home screen](../assets/mainview.png)

The home screen is what you see whenever no menu is open — it's a stack of
one or more **display screens** you configure yourself (see
[Displays](../displays/index.md)), swiped or paged between with the `PAGE`
key. The default screen shows the model name and icon, a status widget
(link quality, battery, timers), and the channel bar along the bottom
([Auxiliary](../reference/toolbars.md) inputs and outputs).

Nothing shown on the home screen is fixed — every widget on it is added,
removed, and resized through the [Displays](../displays/index.md) section.
What you see above is only the default layout for a freshly created model.

## USB connection menu

![USB menu](../assets/usbmenu.png)

Plugging the radio into a computer opens this menu instead of mounting a
drive automatically, letting you choose what the connection is for:

- **Storage** — mounts the radio's SD card as a USB drive, for copying
  models, sounds, firmware files, or Lua scripts to and from a PC.
- **Joystick** — presents the radio as a USB HID joystick, for use with PC
  flight simulators.
- **SWD/serial** modes used for development and firmware recovery.

See [USB Connection Modes](usb-connection-modes.md) for the full breakdown
of what each mode does and when to use it.
