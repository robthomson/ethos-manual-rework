# Procedure for migrating to Ethos Suite

- Ensure that you are on at least Ethos version 1.1.4, the minimum version needed to flash the new Ethos Suite compatible bootloader (FRSK format) from the File Manager on the radio. If not, you will need to manually update to 1.1.4 to be able to migrate to Ethos Suite for automated updates.
- Make a backup your SD card or eMMC (it’s advisable to copy all of it to a folder on your computer).
- Download the zip file for the latest bootloader from [https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases) for your radio, and unzip it. The current bootloader versions are listed in a file called components.json which lists all components used in a release. The file is published with each new firmware release, and can be opened with a text editor such as note pad.
- Simply look for your radio under the “targets” headings, then the relevant Bootloader version number will be listed underneath. You will find the Bootloader listed in the assets of the Ethos release with that number.
- Power the radio on in bootloader mode (hold the enter key down, keep it down and then press power ON) and connect the system to the PC with a data USB cable.
- Copy the bootloader to a folder on your SD card or eMMC (normally the Firmware folder), then eject the drives and disconnect the radio from the PC.
- Start the radio, go to System / File Manager, tap the bootloader.frsk file you have just copied and select the ‘Flash bootloader’ option.
- Download and install the Ethos Suite. You should now be able to follow the sections below to update your radio firmware and the Flash and SD card or eMMC files to the latest versions, and make use of the other Ethos Suite features.
- Please note that you may need to rename the bitmaps/user folder on the SD card or eMMC to bitmaps/models if ETHOS Suite does not do it for you. This is the folder where user bitmaps are stored.
