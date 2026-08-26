# USB Connection To PC modes

## Power Off mode

- Connecting the radio while powered off to a PC via a USB cable is the DFU mode for flashing the bootloader.

## Bootloader mode

- The radio is placed in bootloader mode by switching on the radio with the enter key held down. The status message ‘Bootloader’ will be displayed on the screen. 
- The radio can then be connected to a PC via a USB data cable. The status message will change to ‘USB Plugged’, and the PC should display two external drives connected. The first is for the radio flash memory, and the second is the content of the SD card or eMMC.
- This mode is used for reading and writing files to SD card or eMMC and/or the radio flash memory.
- This mode can also be used to connect to Ethos Suite for updating the radio. Please refer to [Bootloader Mode](../ethos-suite/operation.md) in the Ethos Suite section.

## Power On mode

- If the radio is connected to a PC via a USB data cable while powered on, the following option dialog is displayed:

![](../assets/usbmenu.png)

- In joystick mode the radio can be configured for controlling RC simulators.
- In Frsky Suite mode the radio will enter ‘Ethos mode’ for communication with Ethos Suite. Please refer to [Ethos Mode](../ethos-suite/operation.md) in the Ethos Suite section.

- In Serial mode Lua debug traces are sent to USB-Serial if present. The Lua Development Tools tab in Ethos Suite has an integrated terminal window to display the traces. The baud rate is 115200bps. A suitable Windows Virtual COM Port driver may be found [here](https://www.st.com/en/development-tools/stsw-stm32102.html).
