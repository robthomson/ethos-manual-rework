# SR8/SR10 Model Setup and Channel Reordering

FrSky's SRx stabilized receivers expect a specific channel order. Two
scenarios: building a new model for one from scratch, or converting an
existing model to match.

!!! note "Screenshots pending"
    This page doesn't have simulator screenshots yet — see [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## Creating a new model

The [Model Select](../model-setup/model-select.md) wizard groups
same-function surfaces by default (e.g. 2 ailerons → `AAETR`), but SRx
receivers need the first four channels fixed as **AETRA** instead.

1. In [Controls](../system-setup/controls.md), confirm **Channel order**
   is `AETR`.
2. Enable **[First four channels
   fixed](../system-setup/controls.md#first-four-channels-fixed)** — this
   stops the wizard from grouping the first four channels, keeping them
   strictly in `AETRA…` order regardless of how many of each surface the
   airframe has.
3. Run the model creation wizard as normal — the first 5 channels come
   out as `AETRA`.

!!! tip "As of Ethos 26.1"
    The wizard's channel-numbering convention changed to match FrSky's
    stabilized-receiver documentation directly (see [Model
    Select](../model-setup/model-select.md#stabilized-receivers-and-channel-order))
    — with **First four channels fixed** on, a freshly built model already
    comes out in the correct SRx-compatible order with no further work.
    The manual reordering below is only needed for a model that already
    existed before upgrading to 26.1.

!!! note "Archer receiver self-check"
    Self-check for Archer receivers now runs through [Device Config →
    SxR](../system-setup/devices.md) (firmware v2.1.10+) rather than a
    dedicated self-check procedure. The throttle channel must be at
    −100% or self-check won't start — except on receiver firmware v3.0.0
    and later, where that's no longer required. Also as of v3.0.0, there's
    no longer a panic mode on channel 12.

## Reordering an existing (pre-26.1) model

Converting an existing model (e.g. currently `AAETRFF`) to the
stabilized-receiver order (`AETRAE`, then channel 9 Gain, 10/11 flight
modes, 12 self-check on older SxR units) is a sequence of channel swaps
in [Outputs](../model-setup/outputs.md#swap-channels).

Starting point:

| Ch | Function |
|---|---|
| 1 | Aileron1 (right) |
| 2 | Aileron2 (left) |
| 3 | Elevator |
| 4 | Throttle |
| 5 | Rudder |
| 6 | Flap1 (right) |
| 7 | Flap2 (left) |
| 8 | Retracts |

Target order: `AETRAE` — Ch1 Aileron1, Ch2 Elevator, Ch3 Throttle,
Ch4 Rudder, Ch5 Aileron2, Ch6 Elevator2/AUX2 (then Gain/flight
modes/self-check on 9–12).

1. **Move Aileron2 out of the way first**: in Outputs, select CH2
   (Aileron2), tap again, **Swap Channels**, and swap it with an unused
   channel (e.g. CH9). The swap is immediate — every mix referencing
   either channel updates automatically.
2. **Swap CH3 (Elevator) → CH2.**
3. **Swap CH4 (Throttle) → CH3.**
4. **Swap CH5 (Rudder) → CH4.**
5. **Swap CH9 (Aileron2, parked in step 1) → CH5.**

Result:

| Ch | Function |
|---|---|
| 1 | Aileron1 (right) |
| 2 | Elevator |
| 3 | Throttle |
| 4 | Rudder |
| 5 | Aileron2 (left) |
| 6 | Flap1 (right) |
| 7 | Flap2 (left) |
| 8 | Retracts |

— now in the order FrSky stabilized receivers expect.

See also [Converting 1.6.x Models to 26.1](converting-1.6-models.md) for
the general aileron-differential mix reordering Ethos itself performs
automatically on any pre-26.1 model — this page's manual channel-swap
sequence is specifically about reaching the SRx receiver's own expected
order, not about preserving differential.
