# Ethos Manual

**Ethos** is the operating system that runs on FrSky's Ethos-family radios
(X20S, X20 Pro, X20 Pro AW, X18S, and others). This manual covers setting up
a model from scratch, configuring the radio's system-level settings,
building custom telemetry displays, and the Lua scripting environment that
sits on top of all of it.

!!! note "Work in progress"
    This manual is being rebuilt from scratch. Many sections are placeholders
    for now — see [Contributing](contributing/index.md) if you'd like to help
    fill them in.

## Where to start

- New to Ethos? Start with [Getting Started](getting-started/index.md) —
  the main screen layout and how navigation works before touching any
  settings.
- Setting up a new radio? See [System Setup](system-setup/index.md) for the
  one-time, radio-wide settings (hardware calibration, alerts, battery).
- Programming a model? [Model Setup](model-setup/index.md) covers mixes,
  outputs, flight modes, and everything else that lives per-model, and the
  [Tutorials](tutorials/index.md) walk through building fixed-wing, flying
  wing, and helicopter models end to end.
- Building a telemetry screen? See [Displays](displays/index.md).
- Want a specific task solved quickly? Check the [How-To
  Guides](how-to/index.md).
- Writing or installing Lua scripts/widgets? See [Lua Scripts](lua-scripts/index.md).

## Radios covered

This manual is written primarily against the **X20S**, with radio-specific
differences (X20 Pro, X20 Pro AW, X18S) called out in
[Radio Notes](radio-notes/index.md) where the UI diverges.
