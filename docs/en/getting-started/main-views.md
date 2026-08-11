# Main Views

## Home screen

![Home screen](../assets/mainview.png)

The home screen is what you see whenever no menu is open — a stack of up to
**eight** display screens you configure yourself (see
[Displays](../displays/index.md)), swiped or paged between with the `PAGE`
key or a touch swipe. A freshly created model starts with just one screen
showing a model image, three timer widgets, and the trim/pot indicators;
everything on it is user-configurable from there.

Screens normally share the top and bottom bars described below, but a
screen can also be set to full-screen, hiding both.

## The top bar

The top bar shows the model name on the left (plus the active flight mode,
if one is configured), and a row of status icons on the right:

- Data logging active
- Trainer status (master or slave, as applicable)
- RSSI — 2.4GHz link
- RSSI — 900MHz link (if a dual-band/long-range module is fitted)
- Speaker volume
- Radio battery status

Touching the speaker or battery icon jumps straight to the matching
[General](../system-setup/general.md) (audio) or
[Battery](../system-setup/battery.md) settings panel.

### Error warning

A red triangle appears in the top bar whenever Ethos detects an error —
a Lua script error, a RAM backup error, or running a nightly/unstable
firmware build are the common causes. The detail behind the warning is
always in **System → Info**, on the same page as radio runtime and
[error logs](../system-setup/information.md).

## The bottom bar

![Bottom bar](../assets/bottombar.png)

Four tabs run along the bottom for the top-level sections — **Home**,
**Model Setup**, **Configure Screens**, **System Setup** — with the system
clock on the right (touch it to jump straight to
[Date & Time](../system-setup/date-and-time.md)).

## The widgets area

The middle of each screen is filled with **widgets**: model image, timers,
telemetry readouts, trim/pot bars, and more, all placed and configured by
you. See [Displays](../displays/index.md) for how to add, move, and
configure widgets, and [Additional Displays](../displays/additional-displays.md)
for adding more than the default single screen.
