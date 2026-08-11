# Checklist

![Checklist](../assets/model-checklist.png)

A set of preflight safety checks that run when the radio powers up and/or
a model is loaded. Built-in checks include silent mode, failsafe not set,
switch/pot positions, radio and RTC battery — the switches check shows
which direction each switch needs to move, marked with red dots on the
warning screen:

![Checklist at startup](../assets/model-checklist-at_start.png)

!!! note
    Either `OK` or `RTN` skips the preflight checks entirely, regardless
    of what the on-screen warning implies.

## Throttle check

![Check function](../assets/model-checklist-check_function.png)

Enable and choose an operator — `<` (less than), `~` (approximately
equal), or `>` (greater than) — against a value; warns if the throttle
stick is outside what that comparison allows.

## Failsafe check

Warns if [failsafe](rf-system.md#failsafe) hasn't been set for the current
model.

!!! tip
    Strongly recommended to leave this enabled.

## Switches check

![Switches](../assets/model-checklist-switches.png)
![Switch check options](../assets/model-checklist-switches-options.png)

Per switch, request a specific position at startup (switches with custom
names from [System Setup →
Hardware](../system-setup/hardware.md#switches-settings) show those
names). **Load all switch positions** captures the *current* physical
positions as the desired ones for every switch not marked **No check**.

## Function switches check

![Function switches](../assets/model-checklist-function-switches.png)
![Function switch check options](../assets/model-checklist-function-switches-options.png)

The same idea, for the six [function
switches](model-edit.md#function-switches). **Load all function switch
positions** works the same way as above.

## Pots / Sliders check

![Pots](../assets/model-checklist-pots.png)
![Pot check options](../assets/model-checklist-pots-options.png)

Requests specific pot/slider positions at startup, individually per
control (`~`/`<`/`>`, same as the throttle check). **Load all pot
positions** captures current positions automatically — check the
auto-selected operators carefully afterward, since `~` vs. `<`/`>` may
not match what you actually intended.

## User defined text

![User checklist text](../assets/model-checklist-user-checklist.png)

Displays a plain- or enhanced-text file as part of the startup checklist,
once installed for the model. See [How-To: User Defined Text
Checklist](../how-to/user-defined-checklist.md) for the full setup.
