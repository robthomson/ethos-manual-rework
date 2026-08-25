# Overview

The FrSky Suite PC application runs on a Windows PC or Mac and connects to FrSky radios that are running the ETHOS operating system or the ECOS operating system, or Aegis flight controllers. FrSky Suite connects to the radio via a USB cable. Once connected to the radio or flight controller the current release of FrSky Suite can do the following things:

## Ethos

- Determine the radio type, ID, and the versions of the firmware, the bootloader, the internal RF module, files in Flash memory, and the SD card or eMMC files.
- Change the mode of the radio from running in bootloader mode to starting and running Ethos on the radio, with the option of switching back again.
- With the current radio status information displayed, FrSky Suite provides the user with selections for updating to the most current and correct firmware and files. It then downloads and installs them automatically. The user can select to update the outdated components, to update all components regardless, or to update them individually.
- Using the Model Manager a backup of the models on the radio can be saved to disk, or a previously saved backup may be restored to the radio. Models are not backwards compatible, so the older model files have to be restored from the PC when downgrading to older firmware.
- The FrSky product page can be used to download any firmware from the FrSky download site, and to use the radio as a proxy to flash any module, sensor, servo, or receiver directly from FrSky Suite.
- Convert images to ETHOS format.
- Convert audio files to ETHOS format.

- Lua development tools allow you to view the Ethos Lua documentation, access the Lua demo scripts, as well as providing a terminal for debugging.
- There is a Repair Tool for the X18/S, TW Lite, XE, X20 Pro/R/RS radios. If your radio cannot read from NAND or the settings cannot be saved, this tool can be used to reformat the internal storage.
- Eject USB connections.

At startup there will be a notification if there is an FrSky Suite update available. Installation takes place when Suite is exited.

Note that besides the Tools, Suite offers 3 modes of operation with the radio.

- **Radio** **in** **B****ootloader mode**

- The Radio tab is available for checking and updating the radio firmware and the Flash and SD card or eMMC files to the latest versions.

- The Model Manager tab is available for making a backup of the radio, or to restore a saved backup to the radio.

- **Radio** **in** **Ethos mode**

- In this mode FrSky Suite can use the radio as a proxy to flash the internal module directly or any sensor, servo, or receiver. The FRSK Flasher tab manages these operations.

- **Radio in DFU mod****e**

- The Radio is connected in power off mode, and the DFU Flasher tab is used for flashing the bootloader. This is required if for example the radio firmware has been corrupted and the radio no longer powers up.
