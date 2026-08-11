---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# USB 连接模式

![USB 菜单](../assets/usbmenu.png)

通过 USB 将遥控器连接到电脑后所进入的模式，取决于插入 USB 时遥控器的供电状态。

## 关机模式

**在遥控器关机状态下**通过 USB 将其连接到电脑，遥控器会进入 DFU 模式，用于刷写 bootloader 本身。

## Bootloader 模式 {: #bootloader-mode }

**按住 `ENT` 键**开机，即可进入 bootloader 模式（屏幕显示 "Bootloader"）。此时接入 USB，状态会变为 "USB Plugged"，电脑会挂载**两个**磁盘：遥控器的内部闪存，以及 SD card/eMMC 的内容。该模式用于直接读写这两个存储区域中的文件，同时也是 [Ethos Suite](../ethos-suite/index.md) 更新遥控器固件所使用的模式 —— 详见 Ethos Suite 中的 Bootloader 模式章节。

## 开机模式

在遥控器**正常开机状态下**接入 USB，会弹出模式选择菜单：

- **Joystick** —— 将遥控器识别为 USB HID 摇杆设备，用于操作电脑上的飞行模拟器。
- **FrSky Suite** —— 使遥控器进入 "Ethos mode"，以便与 [Ethos Suite](../ethos-suite/index.md) 通信。
- **Serial** —— 通过 USB 串口（115200 bps）输出 Lua 调试信息。Ethos Suite 的 Lua Development Tools 选项卡内置了终端用于显示这些信息；在 Windows 下可能需要安装虚拟 COM 端口驱动。
