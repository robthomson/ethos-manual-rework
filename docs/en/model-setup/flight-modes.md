# Flight Modes

![Flight modes](../assets/model-fm.png)

Flight modes (flight phases) let a switch select between distinct
behaviors for the same model — gliders might use Launch/Cruise/Speed/
Thermal, power planes Normal/Take Off/Landing, helicopters Normal (spool
up, take off/landing) / Idle Up 1 (aerobatics) / Idle Up 2 (3D). They take
most of the manual switching and re-trimming burden off the pilot: a
flight mode can carry its own independent trims, and can gate both
[Vars](variables.md) and [Mixes](mixes.md) — combined, that's enough for
real complexity. See [Basic Fixed-Wing
Example](../tutorials/basic-fixed-wing.md) for flight modes applied to a
real model.

No flight modes are defined by default. Tap the default flight mode and
choose **Edit** to rename it, or **Add** to create a new one — up to 20
in total.

## Name

A descriptive name — Cruise, Speed, Thermal, Take Off, Landing, whatever
fits.

## Active condition

![Flight mode form](../assets/model-fm-form.png)

A new flight mode starts inactive (`---`). Once set, it can be driven by a
switch or button position, a function switch, a logical switch, a system
event (throttle cut/hold), or a trim position.

The **default** flight mode has no Active condition at all — it's what's
active whenever no other flight mode's condition is true. Only ever one
flight mode is active at a time: the first one (in priority order) whose
condition is currently true. The active mode is shown in bold.

!!! warning "Adding a flight mode to an existing model"
    A newly added flight mode is, by default, active in every mix that's
    already flight-mode-dependent — check each such mix still behaves
    correctly, particularly a **Lock** mix locking a channel to a specific
    flight mode.

## Fade in, out

Transition times for smoothly blending between flight modes (e.g. 1
second each way) — this only has an effect on mixes that are themselves
flight-mode dependent.

## Flight mode management

![Move flight mode](../assets/model-fm-move.png)
![Select for move](../assets/model-fm-move-select.png)
![Modes 0-3](../assets/model-fm-0to3.png)

Tap a flight mode for **Edit**, **Add**, **Clone**, or **Delete**. A
**cloned** flight mode inherits its parent's settings in every mix that
uses flight modes — same behavior, same active/inactive state — so a
clone is added as the last flight mode by default, to avoid interfering
with existing ones. **Move** changes a flight mode's priority: priority
runs in ascending order, and (as above) the first one with its condition
true is the one that's active.
