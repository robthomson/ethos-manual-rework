# Configure an FBUS System

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works) (formerly
F.Port2) puts control and telemetry on one line, letting several FBUS
devices share a single daisy-chained connection with full wireless
configuration. This walkthrough wires two Xact servos onto the aileron
channels (1 and 5) of the [Basic Fixed-Wing
Example](../tutorials/basic-fixed-wing.md).

!!! note "Screenshots pending"
    This page doesn't have simulator screenshots yet — see [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## 1. Download the latest firmware

FBUS needs current firmware on both receiver and devices — e.g. Xact
servos need v2.0.1+. Get the relevant updates from the
[FrSky downloads page](https://www.frsky-rc.com/download/).

## 2. Flash the firmware

Copy the firmware files to `Firmware/` on the SD card/eMMC. In [File
Manager](../system-setup/file-manager.md), plug the servo into the
radio's S.Port connector (white/yellow lead toward the notch), select the
firmware file, and **Flash External Device**.

## 3 / 5. Configure Physical IDs

Both servos default to Physical ID `0C` hex / Application ID `6800` hex —
they'll conflict on the shared bus unless one is changed. Two ways to get
there depending on receiver type:

**Via the transmitter's S.Port connector** (any receiver):

1. Plug servo 1 in, go to **Device Config → XAct**, set **Module** to
   **S.Port connector**. Leave Physical ID `0C`/Application ID `6800` and
   channel `CH1` at their defaults, then **Save to flash**.
2. Plug servo 2 in instead, same menu. Change **Physical ID** to `0D` hex
   and **Application ID** to `6801` hex (see the [Physical ID
   table](../model-setup/telemetry.md#how-frsky-telemetry-works) for
   which slots are free), set **Channel** to `CH5`, **Save to flash**.

**Via the receiver directly** (e.g. TD-R18 Tandem, both servos wired
simultaneously — see [Step 4](#4-configure-the-receiver-for-fbus)):

1. With only servo 1 connected (e.g. receiver Pin1), **Device Config →
   XAct**, **Module** → **Internal module**. Confirm defaults (`0C`/
   `6800`/`CH1`), **Save to flash**.
2. With only servo 2 connected (Pin5), same menu (Device Config talks to
   one servo at a time) — change to `0D`/`6801`/`CH5`, **Save to flash**.
   Reselect Device Config afterward to confirm the change stuck.

## 4. Configure the receiver for FBUS

**SR10 Pro**: [RF System](../model-setup/rf-system.md) → the receiver's
button → **Options** → set **Telemetry Port** to **FBUS**. Xact servos
then daisy-chain off that port; since each servo has only one connector,
an F.Port2 multichannel extender (FP2CH4/6/8) fans it out to several.

**TD-R18 Tandem**: RF System → the receiver's button → **Options** → set
individual pins (e.g. **Pin1**, **Pin5**) to **FBUS** — as many pins as
needed can be reassigned this way, avoiding extenders entirely; every
FBUS-assigned pin carries the identical FBUS signal.

## 5. Check FBUS control of the servos

Plug servo 1 into Pin1, servo 2 into Pin5 (the fixed-wing example's
aileron channels), power up, and confirm channels 1 and 5 move the
correct servos.

## 6. Check FBUS telemetry

With both servos connected, delete any existing `SRV` sensors under
[Telemetry](../model-setup/telemetry.md) and re-discover. Each servo
reports 4 sensors: current, voltage, temperature, and status (`OK` when
normal).

## 7. Making configuration changes later

Once a model is fully wired, isolating one servo to reconfigure it via
Device Config isn't practical. Instead: go to Telemetry, find a sensor
belonging to the target servo (e.g. `SRV1 curr`), and choose
**Configure** — this opens that servo's configuration directly.
**Save to flash** after any change.

!!! warning
    Don't change the Physical ID or Application ID from this screen by
    accident — that's what keeps each servo addressable on the shared
    bus.
