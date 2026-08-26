# Configure a Gear Door and Landing Gear Sequencer

The [Sequencer mix](../model-setup/mixes.md) drives multiple output
channels forwards and backwards on independent, curve-shaped timebases —
a natural fit for landing gear and gear door sequences, where doors and
retracts need to move in a specific order with specific timing.

!!! note "Screenshots pending"
    This page doesn't have simulator screenshots yet — see [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

This example sequences a gear door (channel 7) and retracts (channel 8):
the doors open first, then the gear retracts, then the doors close again
— all from a single switch.

Before configuring anything, plan the timing — a stopwatch against the
real mechanism is the easiest way to get real numbers. Consider whether
gear doors should move in a scale-like ramp or snap open/closed, and
whether the retracts themselves need a smooth ramp or a simple step (e.g.
retracts that just take a switch-style signal).

## 1. Assign the gear door and retracts channels first

Naming these [Outputs](../model-setup/outputs.md) channels before
building the sequencer means they already have readable names when you
pick the sequencer's own output channels. This example uses CH7 for the
gear doors and CH8 for the retracts.

## 2. Add a Sequencer mix

In the main Mixes screen, tap **+** and add a **Sequencer** mix, placed
after the last existing mix.

## 3. Configure the sequencer

- **Name** — e.g. "Gear Sequencer".
- **Active condition** / **Flight modes** — as for any other mix; default
  is *Always on*.
- **Loop mode** — leave **Off** (a continuous forward/backward loop is
  more useful for something like a servo tester than for landing gear).
- **Forward condition** / **Backward condition** — the switch positions
  that trigger each direction, e.g. switch SF down for forward, SF up for
  backward.
- **Forward duration** / **Backward duration** — the timebase each
  direction runs over. This example uses 6 seconds each way.
- **Outputs** — Output1 → CH7 (Gear Doors), Output2 → CH8 (Retracts).

### Output1: gear door curve

Tap the **⋮** menu on Output1 to edit its curve — 5 points by default, up
to 21. For a 6-second sequence with scale-like door movement:

- Points 1→2 ramp from −100 to +100 over 1.5s (doors opening).
- Point 2 is where the retracts (Output2) should activate.
- A 1-second gap follows, to give the 2-second retract cycle room to
  complete before the doors start closing.
- Points 4→5 ramp back from +100 to −100 over 1.5s (doors closing).

This adds up to 6 seconds total, and — importantly — the same curve works
for both forward and backward operation, since it's symmetric.

### Output2: retracts curve

Tap Output2's **⋮** menu. If the retracts expect a simple switch-style
signal rather than a ramp, edit the **forward curve** to step instead of
ramp — set point 3's X value equal to point 2's, which turns that segment
into an instant step rather than a slope.

**Add a backward curve** (from the same menu) if the retract timing needs
to differ by direction — the curve editor shows a direction arrow once
both curves exist, to keep them distinguishable. In this example, the
backward curve moves the step to point 4 instead of point 3, so the
retracts come up as soon as the gear doors have finished opening.
