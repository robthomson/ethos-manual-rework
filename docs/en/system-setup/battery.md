# Battery

![Radio battery settings](../assets/system-battery.png)

Calibrates the radio's internal battery reading and sets alarm
thresholds — separate from a model's flight-pack settings (see [How-To:
Low Battery Voltage Warning](../how-to/low-battery-warning.md)).

- **Main voltage** — shows the current reading, and doubles as the
  calibration adjustment: enter the actual voltage as measured with a
  multimeter. Default is 8.4V (a fully charged 2S Li-ion pack).
- **Low voltage** — the alarm threshold, default 7.2V (7.4V gives extra
  margin). When the [Main voltage
  alert](alerts.md) is on, dropping below this triggers a warning dialog
  and a spoken "Radio battery is low" alert every minute, dialog open or
  not.

  !!! warning
      Land and charge the radio battery as soon as this alert sounds — it
      repeats every minute regardless. At 6.0V the radio shuts down
      unconditionally to protect the 2×3.0V Li-ion cells.

- **Display voltage range** — the min/max for the graphical battery
  display in the top-right corner: MIN is where the first bar segment
  goes dark, MAX is where the fourth lights up. Defaults are 6.4–8.4V for
  the built-in Li-ion pack; many pilots raise the low end to get an
  earlier low-voltage warning and avoid over-discharging. Set these to
  match whatever battery type is actually fitted.
- **RTC voltage** — the real-time-clock coin cell's voltage. 3.0V when
  new; replace it below 2.7V to keep the clock accurate, and expect the
  [RTC voltage alert](alerts.md) below 2.5V.
