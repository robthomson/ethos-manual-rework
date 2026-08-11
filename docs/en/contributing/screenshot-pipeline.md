# Screenshot Pipeline

Every screenshot in this manual (currently ~590 of them, under
`docs/en/assets/`) was captured by scripting the real Ethos simulator, not
by hand. The rig lives in the old
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual) repo, under
`english/manual/`, and has **not been ported into this repo yet** — this
page documents how it works so it can be, and so screenshots can be
regenerated or extended in the meantime without starting from scratch.

## How it's structured

For each menu/section of the manual there's a pair of files:

- `manual/macros/<name>.lua` — a script written against the simulator's Lua
  API (below) that navigates to a specific screen and calls
  `simulator.screenshot(path)` at each point worth capturing.
- `manual/<name>.sh` — a one-line wrapper that launches the simulator
  binary for a specific radio, pointed at that macro, e.g.:

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` runs every macro in sequence to regenerate the
entire set. Individual `.sh` files exist per-section so a single page's
screenshots can be regenerated without re-running everything (each macro
takes anywhere from a few seconds to over a minute).

Key CLI flags:

- `--read-only` — don't persist any changes made during the run.
- `--no-gui` / `--no-audio` — headless-ish; some macros still need the GUI
  because the simulator "skips" without it (see `screenshots.sh`'s comment).
- `--radio-settings <file>.bin` — which radio's saved settings to boot with
  (this is what makes screenshots language- and radio-specific — a German
  run uses a German `.bin`).
- `--sd-directory`, `--flash-directory`, `--documents-directory`,
  `--audio-directory` — point the simulator at the models/firmware/docs/audio
  it should see, so screenshots reflect deliberately staged content rather
  than whatever's on a real SD card.
- `--exec <script>.lua` — the macro to run after boot.

Each radio family (X20S, X20 Pro, X20 Pro AW, X18S) has its own simulator
binary and needs its own `--radio-settings` file per language (e.g.
`x20s-en.bin`, `x20pro-en.bin`), since the UI differs slightly between
radios and the settings file also carries the language.

## The macro API

Macros are plain Lua, driving a `simulator` global:

| Call | Purpose |
|---|---|
| `simulator.loadModel("name.bin")` | Load a specific model file before navigating — each section of the manual uses a model set up to demonstrate that section (see the model list below). |
| `simulator.pressKey(KEY_X, [holdSeconds])` | Press a hardware key — `KEY_ENTER`, `KEY_RTN`, `KEY_MDL`, `KEY_SYS`, `KEY_DISP`, `KEY_PAGE`, etc. A hold duration triggers a long-press (opens contextual menus). |
| `simulator.turnRotaryEncoder(n)` | Move the encoder `n` clicks (negative = reverse) — the primary way to move the cursor between fields. |
| `simulator.touch(x, y)` | Tap a specific screen coordinate — used where touch is the only way to reach something (e.g. switching keyboard layout). |
| `simulator.setAnalog(channel, value)` | Set a stick/pot/slider position directly (`0`-`3` are the four main sticks, `ANALOG_LAST_SLIDER` the last slider), so screenshots show a deliberate, reproducible value rather than whatever the sim defaults to. |
| `simulator.setSwitch(n, position)` | Set a physical switch position. |
| `simulator.setDateTime({...})` | Pin the simulator's clock, so timestamps in screenshots (and anything time-dependent) are reproducible across runs. |
| `simulator.screenshot(path)` | Capture the current screen to a PNG, relative to the macro's working directory (hence the `../assets/...` paths inside each macro). |
| `simulator.connectUsb()` | Simulate plugging into USB, for capturing the USB menu. |
| `simulator.sleep(seconds)` | Wait for an animation/telemetry value to settle before capturing. |

`manual/macros/common.lua` is `dofile`'d from most macros and just pins the
date/time so every macro starts from the same simulated moment.

## Models used per section

`manual/notes.txt` (carried over informally, not yet copied into this repo)
maps each macro to the `.bin` model file it depends on and why — e.g.
`model-mixes.lua` uses `rarebear.bin`, `model-fm.lua` uses `zblank.bin` (a
model with a deliberately blank flight-mode setup), `model-trims.lua` uses
`blaster.bin` (set up with offset trims to demonstrate the trim range).
Porting this file's notes into proper documentation here is part of the
phase-2 work below.

## What porting this into the new repo involves (not done yet)

- Deciding whether macros are re-run from this repo directly (requiring a
  local Ethos simulator install, as the old repo did) or via CI with the
  simulator bundled/downloaded in the workflow.
- Restructuring the flat `../assets/...` output paths to match this repo's
  per-page, per-locale asset layout (`docs/<locale>/assets/`).
- One `--radio-settings ... .bin` and one screenshot run per locale, once a
  locale beyond `en` exists — screenshots are UI-language-specific and
  cannot be shared across locales.
- Deciding how much of the ~40 existing macros to carry over as-is versus
  rewrite against the current nav structure in this repo (some macros
  produce screenshots for sections that no longer map 1:1 onto this
  manual's page layout).
