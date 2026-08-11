# Initial Radio Setup

The one-time setup to work through before programming any model. The
[Tutorials](index.md) that follow all assume this is done first.

!!! note
    These tutorials aren't a strict cookbook — they assume basic RC
    vocabulary and comfort navigating the Ethos menus. If anything here
    is unclear, revisit [User Interface &
    Navigation](../getting-started/user-interface-and-navigation.md)
    first.

## Step 1. Charge the radio and flight batteries

Charge the radio battery per the guidelines that came with the radio, and
the flight batteries with a charger suited to their chemistry — take
particular care with Lithium packs.

## Step 2. Calibrate the hardware

Confirm [Hardware
calibration](../system-setup/hardware.md#analogs-calibration) has been
done (it runs automatically on first startup) so the radio knows the
exact center and limits of every gimbal, pot, and slider. Redo it under
**System → Hardware** any time a gimbal, pot, or slider is replaced.

## Step 3. Perform the radio system setup

[System Setup](../system-setup/index.md) covers everything common to
every model, as distinct from [Model Setup](../model-setup/index.md)'s
per-model settings. Most defaults are fine to start, but review:

- **[Date & Time](../system-setup/date-and-time.md)** — set correctly.
- **[Audio → Choice of
  Voices](../system-setup/general.md#audio-settings)** — set up voice
  announcements, including any custom audio files.
- **[Controls (Sticks)](../system-setup/controls.md)**:
  - **Stick mode** — Mode 1 (throttle/aileron right, elevator/rudder
    left) or Mode 2 (throttle/rudder left, aileron/elevator right —
    Ethos's default).

    !!! warning
        If a model is configured for one stick mode while the
        transmitter is set to the other, an electric motor can spin up
        the instant the receiver powers on.

  - **Channel order** — Ethos defaults to **AETR** (Aileron, Elevator,
    Throttle, Rudder); Spektrum/JR convention is **TAER**, Futaba/Hitec
    is **AETR**. This sets the order stick inputs are assigned when a new
    model is created — models can still be adjusted individually later.

    !!! note "FrSky stabilized receivers"
        These require **AETR** specifically. With more than one surface
        per function (e.g. 2 ailerons), the wizard normally groups them
        (giving **AAETR**) — but SRx receivers expect **AETRA**/**AETRAE**
        instead, so enable **[First four channels
        fixed](../system-setup/controls.md#first-four-channels-fixed)**
        under Sticks to keep the first four channels in strict AETR order
        regardless.

- **[Battery](../system-setup/battery.md)** — set **Main voltage**, **Low
  voltage**, and **Display voltage range** to match the radio's actual
  battery.
- **[Owner Registration ID](../model-setup/rf-system.md#owner-registration-id)**
  — used by ACCESS receivers, and shared across transmitters for Smart
  Share. Configured under Model Setup, but functions as a system-wide
  setting in practice, since every new model uses it (it can still be
  changed per-receiver during registration if needed).

!!! note "Units"
    Ethos has no global metric/imperial toggle — [telemetry sensor
    units](../model-setup/telemetry.md#editing-a-sensor) are set
    individually, per sensor.
