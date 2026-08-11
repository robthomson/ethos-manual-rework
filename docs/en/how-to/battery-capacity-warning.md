# Battery Capacity Warning

Warning on **consumed capacity** (mAh) rather than voltage — a more
direct measure of how much of the pack is actually used up. Two ways to
get there, depending on what hardware is fitted.

## Option A: a Neuron-series ESC

FrSky's Neuron ESCs report consumption directly — no calculated sensor
needed. Set [Receiver Options → Telemetry
Port](../system-setup/devices.md) to S.Port, connect the Neuron's
telemetry lead, and [discover
sensors](../model-setup/telemetry.md#discovering-sensors) — the sensor of
interest is **ESC Consumption**.

1. Add a [logical switch](../model-setup/logical-switches.md) on `ESC
   Consumption`, true above (say) 900mAh — roughly 60% of a pack sized to
   land with ~30% still in reserve.
2. Add a [Play audio special
   function](../model-setup/special-functions.md), active condition the
   new switch, with a **Play value** step for `ESC Consumption`.

As a second line of defense, Neuron ESCs also report **ESC Voltage** —
set up a second logical switch the same way as [Low Battery
Voltage Warning](low-battery-warning.md) (below 3.4V/cell for 4s — e.g.
13.6V for a 4S pack), with its own Play audio function repeating every 5
seconds.

## Option B: a current sensor + calculated sensor

If the ESC doesn't report consumption, a current sensor (e.g. FrSky
FASxxx) combined with a [calculated **Consumption**
sensor](../model-setup/telemetry.md#calculated-sensors) does the same
job.

### 1. Connect and discover

![Current sensor](../assets/how-to-consumption-telemetry-current-sensor.png)

Connect the current sensor's S.Port lead and discover it — it appears as
**Current**. Set its **Range** to match the sensor (e.g. 0–100A for a
FAS100):

![Current sensor edit](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. Create the calculated Consumption sensor

![Create calculated sensor](../assets/how-to-consumption-create-calc-select.png)
![Consumption sensor](../assets/how-to-consumption-create-calc-sensor.png)

In Telemetry, **Create Calculated Sensor** → **Consumption**. Set units
to `mAh` and **Range** to the pack's capacity (e.g. 2800mAh); **Source**
to `Current`.

![Sensor edit](../assets/how-to-consumption-sensor-edit.png)
![Sensor edit 2](../assets/how-to-consumption-sensor-edit2.png)

Set **Reset** to system event `!Telemetry Active` — select **Telemetry
Active**, long-press `ENT`, and choose **Invert** — so the running total
resets automatically once telemetry drops out (i.e. the model is powered
off).

### 3. Milestone callouts

![Delta 200mAh logical switch](../assets/how-to-consumption-lsw-delta200mAh.png)

Add a logical switch using the **Δ > X** function on `Consumption`,
firing every time it climbs by a fixed step — e.g. every 200mAh, a
convenient fraction of a 2800mAh pack.

!!! tip
    Set **Check interval** to `---` (infinite) so it keeps accumulating
    toward the next threshold indefinitely rather than resetting after a
    fixed window. Give **Min Duration** a small non-zero value while
    debugging — at 0.0 the trigger is too brief to see on screen.

Add a Play Audio function, active condition this switch, with a Play
value step for `Consumption`:

![Play delta callout](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value: consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. Low-capacity warning

![Second logical switch](../assets/how-to-consumption-lsw2-play-battlow.png)

A second logical switch fires once, past a hard low-capacity threshold —
e.g. 2000mAh out of a 2800mAh pack — paired with a Play Audio function
repeating every 10 seconds until the model is reset:

![Play value on low battery](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value: consumption on low battery](../assets/how-to-consumption-sf2-play-value-consumption.png)
