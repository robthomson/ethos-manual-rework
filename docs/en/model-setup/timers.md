# Timers

![Timers](../assets/model-timers.png)

Eight fully programmable timers, each counting up or down. Add one with
the **+** next to the column headings, or via **Add** below. Touching a
timer opens reset/edit/add/move/copy-paste options.

![Timer edit](../assets/model-timer1-edit.png)

## Common fields (count-down and count-up)

- **Value** — the timer's current reading.
- **Name** — editable.
- **Mode** — **Up** or **Down**.
- **Start value** (count-down only) — the value counted down from.
- **Alarm Value** (count-up only) — the value at which the timer is
  considered elapsed; it keeps counting past this, but shows red in timer
  widgets.
- **Start condition** — starts the timer. If **Stop condition** is left at
  default, the start condition alone controls start *and* stop. Otherwise,
  the timer starts the first time the start condition becomes true, and
  keeps running from there.
- **Stop condition** — if not left at default, controls the timer once
  running: stopped while true, running while false. In the example below,
  a timer starts when `ThrottleActive` becomes true and stops once
  telemetry is no longer active:

  ![Stop condition](../assets/model-timer1-edit-stop.png)

- **Proportional timing source** — `---` counts in real time. Any other
  source (e.g. the throttle stick or throttle channel) scales the timer's
  speed: at −100% the timer is stopped, at +100% it runs at real-time
  speed, and it scales proportionally in between.
- **Reset** — a switch, function switch, logical switch, or trim position
  that resets the timer; it's held at reset for as long as the condition
  is true.
- **Persistent** — keeps the timer's value across power-off or a model
  change, reloading it next time the model is used.
- **Voice** — which [voice pack](../system-setup/general.md#audio-settings)
  announces this timer.

## Audio actions

![Add audio action](../assets/model-timer1-add-action.png)
![Action type](../assets/model-timer1-action-type-select.png)
![Countdown action](../assets/model-timer1-action-countdown.png)

Fully flexible, per-timer alert configuration. Each action has a type —
**Countdown** (spoken), **Beep countdown** (beeps instead of speech),
**Play file**, or **Play value** — plus:

- **Start** — the value this action's countdown begins from.
- **Step** — announcement interval, up to 10 minutes (600s).
- **Haptic** — accompany the announcement with vibration.

A typical three-action stack:

![Actions summary](../assets/model-timer1-actions-summary.png)
![Timer 2 actions](../assets/model-timer2-actions-summary.png)

1. Spoken countdown starting at 2:00 remaining, every 30s, with haptic.
2. Beep countdown starting at 0:10 remaining, every 1s, with haptic.
3. A custom file (e.g. `timer-1-elapsed`) played on elapse, with haptic.

Add further actions with **Add**; the list runs in priority order with
the **highest priority last**.

See also the [Timer Log display widget](../displays/index.md#widget-types)
for a running log of past timer runs.

![Timer widget](../assets/model-timers-widget.png)
