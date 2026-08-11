# Alerts

![Alerts](../assets/system-alerts.png)

Four radio-wide warnings, each independently switchable — separate from
the per-model [special functions](../model-setup/special-functions.md)
and [logical switches](../model-setup/logical-switches.md) you build
yourself.

- **Silent mode** — a spoken alert at startup when this check is on and
  [General → Audio mode](general.md) is set to Silent, as a reminder the
  radio is muted.
- **Main voltage** — "Radio battery is low" when the main radio battery
  drops below the **Low voltage** threshold set in [Battery](battery.md).
- **RTC voltage** — "RTC battery is low" when the RTC coin cell drops
  below 2.5V (the default threshold). Data logging relies on the real-time
  clock; an invalid time makes logs hard to read, especially telling
  flight sessions apart. This can be silenced temporarily while waiting to
  replace the battery, but shouldn't be left off indefinitely.
- **Sensor conflict warning** — detects conflicting telemetry sensor IDs.
  Only worth disabling if you have sensors that don't meet the S.Port
  specification.
- **Inactivity** — a spoken "Prolonged inactivity" alert (plus a haptic
  buzz, in case the volume is turned down) after the radio has gone
  unused for longer than the configured time — 10 minutes by default.
