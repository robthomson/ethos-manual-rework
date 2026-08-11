# RF System

Configures the model's internal and/or external RF module(s), the Owner
Registration ID, receiver binding, and receiver options. This is also
where a model's choice of internal vs. external module lives — unlike
almost everything else in [System Setup](../system-setup/index.md), RF
hardware selection is **per model**, not radio-wide.

!!! note "Screenshots pending"
    This section's screenshot set hasn't been captured yet (see
    [Screenshot Pipeline](../contributing/screenshot-pipeline.md)) — the
    content below is accurate but text-only for now.

## Owner registration ID

An 8-character unique code (mix of upper/lower case letters and digits, no
special characters) that becomes a receiver's **Registration ID** when
registered. Set the *same* code across multiple transmitters to use
**Smart Share** between them — do this before creating the model you want
to share. Compatible with EdgeTX; only partly compatible with OpenTX.

## Disabling RF output

Hold `PAGE` during power-up to disable both internal and external RF
output for that session (a warning confirms it's off). The module's
**State** setting itself stays ON — a normal restart restores normal
transmission.

## Internal module modes

The X18/X20/X20S/X20HD internal module (TD-ISRM) runs in one of three
modes — the X20 Pro/R/RS's TD-ISRM Pro module is similar but adds LoRa and
tandem dual-band variants. Whichever mode is selected **must match what
the receiver supports**, or binding will fail; after switching modes,
carefully re-verify every channel and especially failsafe behavior.

- **ACCESS** — 2.4GHz and 900MHz paths working in tandem under one set of
  ACCESS controls. Up to three receivers total, in any mix of 2.4GHz
  (24 channels) and 900MHz (16 channels); telemetry from both bands is
  active simultaneously, tagged by band. An **RX** telemetry source
  reports which receiver is currently the active telemetry source.
- **ACCST D16** — a single 2.4GHz path, for legacy "X"-series receivers.
- **TD mode** — low-latency, long-range tandem 2.4GHz + 900MHz for Tandem
  receivers, 24 channels on each band.

**Flex firmware** builds add a second Type column to switch between
FLEX915M (FCC-style 915MHz) and FLEX868M (LBT-style 868MHz) modulation
under any of the three modes above — matching antennas must be fitted for
whichever is selected. EU users can use 200/500mW on 868MHz; at 25mW,
telemetry rides on 868MHz, at 200/500mW it moves to 2.4GHz for
compliance.

Each mode/channel-range choice trades off update rate — e.g. under
ACCESS, 8 channels update every 7ms, 16 every 14ms, 24 every 21ms
(rotating in blocks of 8), and a 4ms **Racing mode** is available at
Ch1-8 with compatible receivers (RS-series, v2.1.7+).

## Registering and binding a receiver (ACCESS)

Binding an ACCESS receiver is two phases — **registration** only needs to
happen once per receiver/transmitter pair; **binding** can be repeated
wirelessly afterward with no bind button needed.

**Phase 1 — Register**:

1. Tap **Register** (skip this entirely if the receiver's already
   registered).
2. Hold the receiver's bind button while powering it on; wait for both
   LEDs to light. The dialog changes from "Waiting for receiver…" to
   "Receiver connected" and fills in the receiver name automatically.
3. Confirm/edit the **Registration ID** (defaults to the Owner
   Registration ID above — matching IDs across transmitters is what makes
   Smart Share work), the **Rx name**, and the **UID**. UID distinguishes
   multiple receivers used together in one model — leave at 0 for a
   single receiver; for several (e.g. one per 8-channel block), it's
   conventional to use 0/1/2. UID can't be read back from the receiver
   afterward, so label it physically.
4. Tap **Register**, confirm "Registration ok", then power the receiver
   off — it's registered but not yet bound.

**Phase 2 — Bind**:

!!! warning
    Never bind with an electric motor connected or an engine running.

1. Receiver off; confirm you're in the right module mode.
2. Tap **RX1** (or 2/3) → **Bind**. A repeating "Bind" voice alert
   confirms bind mode.
3. Power the receiver on **without** touching its bind button; select it
   from the "Select device" list that appears.
4. Confirm "Bind successful". Power-cycle both radio and receiver —
   receiver green LED on, red off, means it's linked. No need to repeat
   binding unless one side is replaced.
5. Repeat for additional receivers (RX2, RX3) if used.

## Receiver options

With the receiver powered on, tap its RX button for:

- **Options** — **Telemetry** (on/off for this receiver), **Reduced
  telemetry power 25mW** (vs. the normal 100mW — useful if nearby servos
  pick up RF interference), **High PWM Speed** (7ms servo update instead
  of 18ms — confirm your servos can keep up), **Telemetry port**
  (S.Port/F.Port/FBUS), **SBUS** (16- or 24-channel — every connected
  SBUS device must support SBUS-24 before enabling it), and **Channel
  Mapping** to remap channels to specific receiver pins.
- **Share** — hands the receiver to another ACCESS radio with a
  *different* Owner Registration ID. On the source radio, tap Share (its
  green LED turns off); on the target radio, Bind as normal — Share
  skips re-registration since the ID transfers automatically. Exit on the
  source radio to end sharing; rebinding moves it back. (Not needed at
  all if every radio already shares one Owner Registration ID — just bind
  directly on whichever radio should control it.)
- **Reset bind** — cleans up after a Share and restores your own bind;
  power-cycle the receiver afterward.
- **Factory reset** — resets the receiver and clears its UID,
  unregistering it entirely.

With the receiver **off**, the same RX button offers **Options** (waits
for the receiver to connect), **Bind** (e.g. to rebind a receiver
previously bound elsewhere), and **Clear** (equivalent to Reset bind).

## Redundant receivers

A second receiver can be bound to an unused RX slot for redundancy — 2.4G
or 900M can each back up the other. FrSky redundancy evaluates
**per-frame**, always using the best available frame (active/active
failover), so control can hop between receivers frame to frame as needed.

1. Wire the redundant receiver's SBUS Out to the main receiver's SBUS In.
2. Enable the corresponding internal RF module (e.g. 900M) and set its
   antenna/power.
3. Register the new receiver (if not already), then bind it to the free
   RX slot as above.
4. Confirm its green LED is on — it's now listed as the redundant
   receiver.

## Failsafe

Failsafe data is resent from the transmitter roughly every 10 seconds; on
TD/TW/AP/AP Plus receivers it's also saved receiver-side, so it survives
a receiver reboot. Re-check failsafe carefully after any receiver
firmware upgrade that adds this behavior.

- **Hold** — holds the last received channel positions.
- **Custom** — per-channel: **Not Set**, **Hold**, **Custom** (a fixed
  value — tap the arrow icon to capture the current value, or enter one
  directly), or **No Pulses**.
- **No Pulses** — stops pulses outright, for flight controllers with
  their own return-to-home behavior on signal loss.
- **Receiver** — (X-series or later receivers) sets failsafe on the
  receiver itself instead.

!!! warning
    Test whichever failsafe setting you choose carefully before relying
    on it.

## Range check

Run this at the field before every flying session with a new or changed
setup. Selecting **Range Check** deliberately reduces transmit power (a
repeating voice alert confirms the mode) and shows live VFR%/RSSI for
evaluating link quality. FrSky's range-check power level is roughly
−10dB relative to the normal +20dB operating level; at 1m altitude for
both radio and receiver, expect a critical alarm at around 30m — closer
than that under normal conditions may indicate a problem.

With multiple bound receivers, range check data is shown one active
receiver at a time per band — turning off the currently-active one lets
the next (in priority 0/1/2, shown via the **RX** sensor) take over so
each can be checked in turn.

## External and third-party RF modules

FrSky external modules (XJT Lite, R9M Lite, R9M Lite Pro, TWIN Lite Pro)
follow the same Register/Bind pattern as the internal module, with
protocol-specific channel counts, power levels, and antenna requirements
— refer to the specific module's manual for exact figures.

**ELRS** (ExpressLRS) is supported both via the TWIN Lite Pro module's
ELRS mode and via genuine ELRS modules (which need the ELRS Lua script
installed to `scripts/elrs` before appearing as a module option). Twelve
channels; key settings are **Packet Rate** (latency vs. range trade-off),
**Telemetry Ratio** (how often telemetry is sent, 1:1 to 1:128),
**Switch Mode** (**Hybrid** — most aux channels reduced to 2–3 positions
for lower latency — or **Wide** — full 64–128 step resolution), **Model
Match**, and **Tx Power** (10mW–1000mW, optionally **Dynamic Power** to
scale automatically with link quality — requires telemetry enabled).

**Third-party modules** (currently Ghost, Multi-protocol, Crossfire, in
addition to ELRS) each need their own user-installed Lua script — see
[Screenshot Pipeline](../contributing/screenshot-pipeline.md)'s notes on
`scripts/` and the *Third-Party External Modules* thread on rcgroups. A
module's entry only appears on the RF screen once its script is
installed. The Multi-protocol module (IRX4 Lite) can additionally be
firmware-flashed directly from [File Manager](../system-setup/file-manager.md):
copy the firmware file to `Firmware/`, then **Flash external
multimodule**.
