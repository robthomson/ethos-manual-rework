# Low Battery Voltage Warning

Monitoring flight-pack voltage **under load** and alerting below a
threshold is a more reliable approach than relying on a fixed timer — a
sensor such as a FrSky FLVSS makes this straightforward.

## 1. Connect and discover the sensor

![LiPo telemetry sensor](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

Set [Receiver Options → Telemetry
Port](../system-setup/devices.md) to **S.Port**, connect the FLVSS to the
receiver via an S.Port cable, then enable **Discover new sensors** under
[Telemetry](../model-setup/telemetry.md) — the LiPo sensor appears
alongside the others already discovered.

## 2. Add a logical switch

![Battery low logical switch](../assets/how-to-low-batt-lsw-battlow-lipo.png)

Add a new [logical switch](../model-setup/logical-switches.md) with the
Lipo sensor as its source. Long-press `ENT` on the highlighted sensor to
choose which of its values to use:

![Select lowest cell](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- Min pack voltage / Max pack voltage
- **Lowest cell voltage** / Highest cell voltage
- Cell count
- Individual cell voltages (only selectable while the sensor is actually
  connected to a bound receiver with a LiPo attached)

Select **Lowest** (cell voltage) — the value that matters for LVC-style
protection.

![Lowest cell selected](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

Set the comparison value to around **3.4V** and **Delay before active**
to **4 seconds** — the switch goes true once the lowest cell has read
below 3.4V per cell continuously for 4s or more. (3.4V *under load*
typically recovers to around 3.7V once load is removed, so this threshold
reflects a real sag, not just momentary noise.)

![Completed logical switch](../assets/how-to-low-batt-lsw-summary.png)

## 3. Add a special function

![Special function: BattLow](../assets/how-to-low-batt-sf-battlow.png)

Add a [Play audio special function](../model-setup/special-functions.md),
**Active condition** set to the `BattLow` logical switch, choose a voice,
and under **Sequence** add a **Play value** step for the LiPo total
voltage:

![Play value: LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![Sequence summary](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

With **Repeat** set to 10 seconds, the LiPo voltage is spoken every 10s
for as long as the lowest cell stays below the 3.4V/4s threshold.
