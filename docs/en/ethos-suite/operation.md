# Operation

## Welcome section

**Update News** — release notes and backup recommendations before
updating. Ethos 1.6.0+ requires the internal RF module and TD/TW/AP/AP
Plus receivers to be on v3.0.1+ to use its improvements. Enabling
**Pre-releases** (with the server set to GitHub — see [Suite
Settings](#suite-settings)) also lists pre-release builds here, alongside
full release history.

**Ethos web page** — an embedded view of ethos.frsky-rc.com: resources,
model template links, and the list of supported radios.

## Radio section

Manages the connected radio. Power it into [bootloader
mode](../getting-started/usb-connection-modes.md#bootloader-mode) and
connect via USB — Suite shows the radio type (e.g. "X20") once detected.

### Radio Information

- **Ethos** — installed firmware/bootloader versions; **Manage Ethos**
  jumps to updating them if out of date.
- **RF Module** — installed internal RF module firmware; **Manage
  internal module** jumps to updating it if out of date.
- **Model manager** / **Lua library** / **Download center** — shortcuts
  into those tools.

### Updating Ethos {: #updating-ethos }

The **Ethos** tab shows Firmware, Bootloader, SD card/eMMC (audio files),
and flash memory (system bitmaps) versions side by side — system files in
flash are now updated together with firmware, no longer managed
separately.

- **Write outdated components** — updates only what's behind.
- **Write all components** — updates everything regardless of version.
- Individual **Write firmware**, **Write bootloader**, **Write audio
  files** options, each run by clicking the dark grey button next to the
  chosen option.
- **Flash from a local file** — bypasses the download, using a firmware
  file already on disk.

Selecting a release first means picking a **branch** (Stable/Testing)
then a version. Updating prompts for a backup first (**Go to backup
page**) — take it. If the internal RF module isn't on v3.0.1+, Ethos
1.6.0+ requires upgrading it before continuing (**Go to Module
manager** flashes it automatically, then the Ethos update resumes) — and
TD/TW/AP/AP Plus receivers need their telemetry deleted and rediscovered
afterward to pick up updated sensor names.

Update progress is shown step by step (switching to bootloader,
downloading, copying, unmounting, writing, refreshing, "Update
successful!") — the radio's own screen mirrors the write progress too.

!!! note "Pre-release updates"
    A pre-release's files can change without its version number
    changing, which Suite can't detect — always reflash a pre-release
    version you're already on once it becomes a full release. Check the
    firmware date on [System → Info](../system-setup/information.md) if
    unsure.

!!! note "Updating from Ethos 1.2.8 or earlier"
    Suite may not be able to flash firmware/bootloader fully
    automatically from such an old version — a guided manual-flash dialog
    appears instead. Eject the drives manually before unplugging USB
    either way.

System bitmap files update automatically alongside firmware now (no
separate management needed); audio files update via **Write all
components** or **Write audio files** (downloads the selected language
pack, e.g. "English audio pack").

### RF Module Manager

Select a version (normally the latest) and **Flash module** to update the
internal RF module's firmware directly — confirms
"...has been flashed successfully" on completion. This is also triggered
automatically by the mandatory v3.0.1 upgrade path above.

### Ethos Mode

**Switch to Ethos** reboots the radio out of bootloader mode into
running Ethos (shown by a green USB icon on the radio, and the Suite
header dropping "(Bootloader Mode)"). This is required for the
**Download center** to use the radio as a proxy for flashing modules,
receivers, sensors, and servos. The button then becomes **Switch to
Bootloader** to reverse it. **Eject Drives** disconnects the radio
cleanly.

### Model Manager

Backs up model files and settings to disk, or restores a previous backup.

!!! warning
    Restoring does **not** restore firmware — after restoring
    models/settings, separately reflash the firmware version that
    actually matches that backup (see [Updating
    Ethos](#updating-ethos)), since model files aren't backwards
    compatible.

- **Backup Location** — browse to a folder (remembered per radio type);
  the last backup's date/time is shown beneath it.
- **Backup** — saves model files, recording the current Ethos version
  alongside them.
- **Restore** — select which components to bring back: Audio (off by
  default), Scripts, Screenshots, System Bitmaps (off by default —
  managed with firmware now), Models (including any [user-defined
  checklist](../how-to/user-defined-checklist.md) text files stored
  alongside them), Language, User Bitmaps, Logs, System Settings.

### Lua library

Browse and one-click install Lua scripts/tools from FrSky's remote
library (or install from a local zip), with installed scripts shown
alongside the remote catalog once any exist.

## Tools section

- **Download center** — download any firmware from the FrSky site, and
  (while the radio is in Ethos mode) use it as a proxy to flash a module,
  sensor, servo, or receiver connected via an S.Port upgrade connection.
  Pick the product from the list (e.g. a TW SR8 receiver), browse
  available **assets**, **Download** to save locally or **Flash** to
  write directly to the connected device — a progress bar tracks the
  flash, ending in "...has been flashed successfully!"

- **Image manager** — converts images to Ethos's native format (32-bit
  BMP, RGB, alpha channel added only if needed) at a chosen size,
  preserving aspect ratio. Reference sizes: model images 300×280 (X20) /
  180×168 (X18); full-screen images 800×480 (X20) / 480×320 (X18) — see
  [File Manager](../system-setup/file-manager.md#top-level-folders) for
  bitmap naming rules. Also browses the radio's `bitmaps/gps`,
  `bitmaps/models`, and `bitmaps/user` folders directly, with upload
  support. Add images to the transcode list with **+** (TIFF isn't
  supported), pick an output path (a local folder; directly to the radio
  under model/user/GPS images; or the currently open radio folder), and
  optionally auto-open the output folder or force an alpha channel.

- **Audio manager** — converts audio to Ethos's format (PCM linear,
  32kHz, mono, 16-bit little-endian). Add files with **+**, choose a
  local folder or send straight to the radio's `audio` folder (moving it
  into the right voice subfolder afterward), optionally auto-opening the
  destination.

- **Lua development tools** — **Lua Docs** links the Ethos Lua reference
  guide (see also the *FrSky - ETHOS Lua Script Programming* rcgroups
  thread); **Lua Demo Scripts** links example scripts on the
  Ethos-Feedback-Community GitHub; **Debug** opens a live log window for
  Lua `print()` traces sent over USB-Serial while the radio is in Serial
  mode:

  1. Connect the radio to Suite normally and switch to Ethos mode.
  2. Edit Lua scripts directly on the radio's mounted drive, in any code
     editor.
  3. Open **Lua Development Tools** → **START DEBUG** — this reboots the
     radio into Serial/debug mode and re-initializes scripts.
  4. Every active script's `print()` output streams into Suite's
     terminal.
  5. **STOP DEBUG** switches back to normal Ethos mode to edit further.

- **DFU Flasher** — flashes the bootloader via a power-off USB (DFU)
  connection, working even with fully corrupted firmware, since the
  underlying ST bootloader lives in ROM. **Select Bootloader** to pick a
  downloaded file (Suite reports its version/suitability), connect the
  **powered-off** radio, then **Flash**.

  !!! note "\"Radio connection is not detected!\""
      Usually a missing/incorrect DFU driver. Most Windows 10+ PCs handle
      Tandem systems with the default USB DFU driver, but Windows Update
      sometimes replaces it with a generic one that doesn't work — check
      Device Manager, and consider a tool like Impulse Driver Fixer.
      Horus X10 users specifically may need to install the STM32
      bootloader USB driver by hand (Impulse Driver Fixer or Zadig),
      since Windows 10 doesn't install it by default.

- **Repair Tool** — for X18/S, TW Lite, XE, and X20 Pro/R/RS: reformats
  internal storage when the radio can't read NAND or save settings.

## Others section

- **Documentation** — links to the Ethos-Feedback-Community GitHub, the
  official Ethos manuals (downloadable), and an Ethos Suite FAQ.
- **Ethos Github** — releases and issue tracker (search existing issues
  before filing a new one).

### Suite Settings {: #suite-settings }

- **Language** — Czech, German, English, Spanish, French, Hebrew,
  Italian, Dutch, Norwegian, Portuguese, Slovenian, Chinese.
- **Server location** — **FrSky server** or **GitHub** (needed for
  pre-release access above).
- **Debug options** — toggle the fatal-error popup; enable full Suite
  debug logging (not just crashes); open the logs folder.
- **Version** / **Update Suite** — current version, and a manual update
  check.
- **About** — acknowledgments for reused components.

## Command line operation

Ethos Suite can run from a terminal:

| Flag | Effect |
|---|---|
| `--help` | Show command-line help. |
| `--version` | Show the installed Suite version. |
| `--list-radios` | List all supported FrSky radios. |
| `--radio-components --radio {RADIO}` (or `--radio auto`) | List a connected radio's components and their paths. `auto` detects automatically; specify `{RADIO}` if more than one is connected. |
| `--get-path {COMPONENT}` | Get the path for a component — `BITMAPS`, `SCRIPTS`, `SCREENSHOTS`, `AUDIO`, or `I18N`. |
| `--serial start` \| `--serial stop` | Enable/disable serial debug mode. |

!!! note
    Suite won't start at all unless it recognizes a valid command.
