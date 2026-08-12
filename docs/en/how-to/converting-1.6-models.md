# Converting 1.6.x Models to 26.1

As of Ethos 26.1, the model wizards assign channels starting from the
**left** and alternating outside-in, instead of the right-to-left
convention earlier versions used — bringing the default output straight in
line with FrSky's own stabilized-receiver documentation. See [Model
Select](../model-setup/model-select.md#stabilized-receivers-and-channel-order)
for the new convention itself; this page covers what happens to a model
**built before the upgrade**.

Ethos never touches [Channels](../model-setup/outputs.md) output
assignments during conversion — no rewiring is ever required. What it may
do, the first time an affected model is selected after upgrading, is
reorder aileron-related mix outputs (the aileron mix, Ail→Flaps, Ail→Rud,
V-tail Rudders) so aileron differential keeps behaving correctly, appending
"Left"/"Right" to affected channel names. Exactly what happens depends on
how the model was originally built — there are three scenarios. (All
examples below assume channel order **AETR**; a different order follows
the same logic for its aileron channels.)

## A. Default channel usage (CH1 = Aileron Right)

The common case: a 1.6.x model built with the wizard's default output,
where CH1 is Aileron Right and CH5 is Aileron Left.

Ethos reorders the Aileron mix's output assignments (so the mix now lists
CH5 before CH1, matching the new left-first convention) but leaves the
Channels page's CH1/CH5 assignments exactly as they were. Since the
physical channel a servo is wired to never changes, **no action is
needed** — the model keeps flying exactly as before.

## B. Channels already swapped (CH1 = Aileron Left)

Some 1.6.x models used **Swap channels** in Channels (then called
Outputs) so CH1 drove the left aileron instead of the right.

Ethos again reorders the Aileron mix's output assignments to preserve
correct differential behavior; since this model's Channels assignment was
already left-first, it now matches the new convention directly. **No
action is needed** here either.

## C. Mix inverted instead of channels swapped

A few 1.6.x models achieved the same left-aileron-on-CH1 result a
different way: inverting the Aileron mix itself (negative Weight and
Differential) rather than swapping output channels, then renaming CH1/CH5
to match. Ethos's conversion logic only looks at actual channel
assignments, not user-chosen names — so it still treats CH1 as Aileron
Right internally, and this is the one scenario that needs a manual fix
after upgrading (the model flies correctly either way, but the channel
*names* end up conflicting with what Ethos now thinks is left/right).

To resolve it:

1. **Re-invert the Aileron mix** — change Weight and Differential back to
   positive values.
2. **Swap the aileron output channels** using **Swap channels** in
   [Channels](../model-setup/outputs.md#swap-channels), so the physical
   wiring matches again.
3. **Rename the two output channels** to their correct Left/Right
   functions.

!!! warning
    After making these changes, confirm the mixes and output channels
    behave correctly — **with the propeller(s) removed** — before flying.
