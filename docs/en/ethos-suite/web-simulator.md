# Ethos Web Simulator

New in Ethos 26.1: a browser-based simulator, built as WebAssembly — no
install, runs entirely in-browser (Chrome recommended). It's for
exploring radio capabilities, testing model changes, or trying a new
Ethos release before actually upgrading a real radio.

!!! note "Screenshots pending"
    This page doesn't have screenshots yet — see [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

Available at [ethos-simulator.frsky-rc.com](https://ethos-simulator.frsky-rc.com/).
Default selections are the latest Ethos release, an X20 Pro, and the FCC
protocol — pick a display language to start. With no model data loaded
yet, it opens straight into the new-model wizard; complete it (or [upload
a radio backup](#recommended-setup) instead) to get a working test model.

## Panel layout

Use the **Panels** icon in the top menu to open additional panels (e.g.
**Console** — useful for watching the startup sequence and catching
errors/events — and **Telemetry**), then drag their title bars to
position them (e.g. Console bottom-left, Telemetry bottom-right). The
simulator remembers panel layout between sessions.

In the **Telemetry** panel, **Add a new sensor** repeatedly for whichever
sensors your simulated session needs. Save that set with the panel's menu
→ **Save telemetry settings** (downloads `telemetry.json`); reload it in
a future session via the **Upload** icon → **Upload a JSON telemetry
file**.

## Recommended setup {: #recommended-setup }

Replicating your actual radio's setup in the simulator gives you the same
functionality to test against, without touching your real flying/model
environment:

1. Back up your radio via [Ethos Suite's Model
   Manager](operation.md#model-manager) function.
2. **Upload** menu → **Upload a radio backup**, and browse to that backup
   file. The simulator starts on whatever model was current on the radio
   at backup time.
3. Build or modify models from there — clone an existing model or start
   from a template to maximize reuse rather than programming from
   scratch. **Download** menu → **Download a model file** saves the
   finished `.bin`, ready to copy onto the real radio.

## Simulator task bar

- **Screenshot** — saves to the downloads folder.
- **Start record** — records a macro (its own topic, beyond this
  overview).
- **Panels** — lists panels not currently open.
- **Upload…** — model file (`.bin`), radio backup (`.bin`), audio pack
  (`.zip`), Lua plugin (`.zip`), CSV translations file (`.csv`), JSON
  telemetry file (`.json`), or start a macro (`.zip`).
- **Download…** — save the current model (`.bin`), edit the current
  model, edit the current model file (JSON), save all screenshots (to a
  chosen folder), save a radio backup (`.zip`), or save telemetry
  settings (`.json`).
- **Audio On/Off**, **Restart simulator**, **Documentation** (links the
  latest manual), **Light/Dark mode**.

## Controls panel

Mimics the chosen radio's physical controls.

- **Gimbals** — drag with the mouse to move a stick. While debugging,
  constrain a stick to auto-center, vertical-only, or horizontal-only
  movement.
- **Momentary switches/buttons** — can be latched, toggling between on
  and off and staying there, instead of springing back — useful for
  debugging without having to hold a button down.
