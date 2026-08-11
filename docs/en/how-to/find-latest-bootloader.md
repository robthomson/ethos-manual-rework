# Find the Latest Bootloader or Other Component

Ethos firmware releases publish a `components.json` file listing the
current version of every component per radio, useful for confirming
whether a given bootloader/firmware/audio/system-files version is
actually current before flashing it.

!!! note "Screenshots pending"
    This page doesn't have simulator screenshots yet — see [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

1. Download `components.json` from the latest Ethos release.
2. Open it in a text editor (VS Code, Notepad, etc.).
3. Find the section for your radio — e.g. `X20`:

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   (A snapshot example — always check the *current* release's file for
   real version numbers.)

4. Read off the version for whichever component you need — in the
   example above, the latest bootloader for the X20 family is `1.4.15`.

See [File Manager](../system-setup/file-manager.md#top-level-folders) for
where to place the downloaded firmware file, and [USB Connection
Modes](../getting-started/usb-connection-modes.md#bootloader-mode) for
putting the radio into bootloader mode to flash it — or use [Ethos
Suite](../ethos-suite/index.md), which handles version-checking and
flashing automatically.
