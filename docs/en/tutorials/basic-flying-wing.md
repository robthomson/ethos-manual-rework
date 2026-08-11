# Basic Flying-Wing (Elevon) Example

A 2-servo elevon flying wing, using the Dreamflight Weasel's recommended
rates/Expo/mix ratios as a concrete worked example. Complete [Initial
Radio Setup](initial-radio-setup.md) first.

## Step 1. Confirm System settings

Default **AETR** order, with **[First four channels
fixed](../system-setup/controls.md#first-four-channels-fixed)** **OFF**.
Register (if ACCESS) and bind the receiver via
[RF System](../model-setup/rf-system.md) before continuing.

## Step 2. Identify the servos/channels required

For an elevon airframe, [mixes](../model-setup/mixes.md) combine aileron
and elevator input onto both physical surfaces — just 2 channels total,
each one a blend of both inputs.

## Step 3. Create a new model

![Create airplane model](../assets/tut-wing-eg-wiz-create-airplane.png)

From [Model Select](../model-setup/model-select.md), start the
**Airplane** wizard, choosing **Non stabilized receiver**.

![No engine](../assets/tut-wing-eg-wiz-no-engine.png)

Select **No engine**, accept the default 2 aileron channels, and select
**No flaps**.

![No tail](../assets/tut-wing-eg-wiz-no-tail.png)

Select **None** for tail type — this is what triggers Ethos to build the
elevon mix (aileron + elevator inputs, both onto the same two channels)
automatically. Name the model (e.g. "Weasel"), pick a bitmap, and finish
— it becomes the active model in the Airplane category.

## Step 4. Review and configure the mixes

![Mixes overview](../assets/tut-wing-eg-mixes.png)

The wizard creates an Ailerons mix on channels 1+2, followed by an
Elevators mix *also* on channels 1+2 — both inputs act on both elevon
channels, which is the entire elevon mixing trick.

### Ailerons

![Aileron mix](../assets/tut-wing-eg-mixes-ail-mix.png)

**Weight/Rates** — per the Weasel's manual, aileron deflection should be
roughly 3× elevator's, and the two should sum to 100%: **75%** aileron,
**25%** elevator. Low rates run about half of high rates: **36%**
aileron low, **12%** elevator low.

![Aileron mix weight](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo** — Weasel-recommended 35% high / 20% low, active on switch SB
down, flattening the response around center stick.

**Differential** — small on this airframe, about **4%**:

![Aileron differential](../assets/tut-wing-eg-mixes-ail-diff-04.png)

(See [Basic Fixed-Wing
Example](basic-fixed-wing.md#ailerons) for why differential matters —
same adverse-yaw reasoning applies here.)

### Elevator

![Elevator mix](../assets/tut-wing-eg-mixes-ele-mix.png)

The same pattern: **25%**/**12%** high/low rates, same Expo values as
aileron.

### Rudder

![Rudder mix](../assets/tut-wing-eg-mixes-rud-mix.png)

The Weasel has none — flying wings generally don't need one. Where a
rudder *is* needed on an elevon model, add it as a [Free
Mix](../model-setup/mixes.md#mix-libraries) on channel 3.

## Step 5. Bind the receiver

As in [Step 1](#step-1-confirm-system-settings) — register/bind before
proceeding, and consider disconnecting servo linkages or reducing travel
until Min/Max limits are set, to avoid over-driving anything.

## Step 6. Review the Mixes

Output channels 1/2 can be renamed **Elevon1**/**Elevon2**. With full
right aileron applied, channel 1 (right, up-going) reads 75%, while
channel 2 (left, down-going) reads 72% — the 3% difference *is*
differential at work. Add full down elevator on top and channel 1 becomes
75+25 = 100%, channel 2 becomes 72−25 = 47%.

## Step 7. Configure the maximum servo throws

![Full aileron](../assets/tut-wing-eg-outputs-full-ail.png)
![Full aileron + full elevator](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

Center each servo with **PWM center** first. The Weasel's recommended
maximum throw is 25mm aileron + 10mm elevator = 35mm combined — apply
full aiding *and* full opposing aileron/elevator input and confirm
neither exceeds mechanical or servo limits before setting final
deflections.

- **Min/Max** — hard limits, never overridden; reducing them reduces
  throw rather than clipping. Default ±100%, extendable to ±150% if
  needed.
- **Curve** — often faster and more flexible than juggling Min/Max/
  Subtrim directly, with the benefit of a live graph. A 3-point curve
  suits most outputs; a 5-point curve on the second elevon makes it easy
  to synchronize travel at 5 points against the first. When using a
  curve for this, leave Min/Max/Subtrim at their pass-through values
  (−100/100/0, or −150/150/0 with extended limits) and let the curve do
  the shaping instead.
