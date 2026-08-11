# Migration

Moving a radio from the older, separate PC update tools to Ethos Suite,
for the first time.

1. **Confirm Ethos ≥ 1.1.4** — the minimum version that can flash the new
   Suite-compatible bootloader (FRSK format) directly from [File
   Manager](../system-setup/file-manager.md). Update manually to 1.1.4
   first if needed.
2. **Back up the SD card/eMMC** — copy the whole thing to a folder on a
   PC.
3. **Download the latest bootloader** from
   [ETHOS-Feedback-Community releases](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   and unzip it. Each release publishes a `components.json` listing every
   component's current version — see [How-To: Find the Latest
   Bootloader](../how-to/find-latest-bootloader.md) for reading it.
4. Find the radio under its `targets` entry in that file for the exact
   bootloader version to use, and locate the matching file in that
   release's assets.
5. Power the radio into [bootloader mode](../getting-started/usb-connection-modes.md#bootloader-mode)
   (hold `ENT`, then power on) and connect via USB.
6. Copy the bootloader file to the SD card/eMMC (normally into
   `Firmware/`), then eject the drives and disconnect.
7. Start the radio normally, go to **System → File Manager**, tap the
   `bootloader.frsk` file just copied, and **Flash bootloader**.
8. Download and install Ethos Suite — [Operation](operation.md) covers
   updating firmware/files and the rest of Suite's features from here.
9. If Ethos Suite doesn't do it automatically, the `bitmaps/user` folder
   on the SD card/eMMC may need renaming to `bitmaps/models` (this is
   where user model bitmaps live).
