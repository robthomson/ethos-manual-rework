---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 文件管理器

![文件管理器 - 遥控器](../assets/system-filemanager-radio.png)

文件管理器用于浏览遥控器的存储空间，并为内部射频模块、通过 S.Port 连接的设备、OTA（无线空中升级）设备以及外部模块刷写固件。

## 存储结构

点按 **Flash**（或按 `PAGE` 切换驱动器）可浏览遥控器内部的虚拟 USB 闪存盘，其中存放系统位图与字体：

![Flash 存储](../assets/system-filemanager-flash.png)

- `bitmaps/system` — 用于屏幕显示与图标的位图
- `fonts/` — 各语言选项所使用的字体

引导程序（bootloader）与系统固件本身都位于该内部闪存中，从最初的 X9D 起的每一款 FrSky 遥控器均是如此。

**X20/X20S/X20HD** 系列使用 FAT32 格式化的 SD card，容量不超过 32GB（SanDisk Ultra Micro SDHC Class 10 16GB 卡是可靠的选择）。**X18** 与 **X20 Pro/R/RS** 默认使用内置 eMMC（也可另外加装一张外部 SD card）——点按 **Radio** 即可浏览。若缺少 `Logs/`、`models/` 和 `screenshots/` 目录，Ethos 会自动创建；`Firmware/` 则是人为约定的目录，用于存放接收机等设备的固件文件。

## 顶层文件夹 {: #top-level-folders }

- **`audio/`** — 用户与系统声音文件，按语音种类分开存放
  （`audio/en/gb`、`audio/en/us`、`audio/en/default`）。用户文件由
  [播放音频特殊功能](../model-setup/special-functions.md)播放；
  系统文件包括 `hello.wav`（“Welcome to Ethos” 开机问候语——也可自行添加
  `bye.wav`，但固件并未提供）。格式要求：16kHz 或 32kHz PCM、
  线性 16 位，或 A-law（EU）/µ-law（US）8 位；文件名最长 31 个字符
  （不含扩展名）。无论实际选择哪一种语音，Ethos Suite 都会保持三个语音
  文件夹内容同步。

  ![audio 文件夹](../assets/system-filemanager-audio.png)

- **`bitmaps/`** — `bitmaps/models/` 存放用户模型图片（在
  [模型编辑](../model-setup/model-edit.md)或新建模型向导中设定）；
  `bitmaps/user/` 存放其他所有图片。推荐格式：32 位 BMP，每色通道 8 位，
  带 alpha 通道，300×280 像素——这样可将遥控器的解码开销降至最低。
  Ethos 可即时缩放 BMP，但不能缩放 PNG/JPEG。文件名只能使用
  `A-Z a-z 0-9 ()!-_@#;[]+=` 以及空格，且必须不超过 11 个字符
  （另加 4 个字符的扩展名），否则不会出现在模型图片选择器中——
  更长的文件名仍会显示在文件管理器中，但无法在选择器里被选中。
  Ethos Suite 的图片转换工具可代为完成格式转换。

  ![bitmaps 文件夹](../assets/system-filemanager-bitmaps.png)

- **`documents/user/`** — 用户文本文档，可由 **Text** 显示小组件调用。

- **`Firmware/`** — 用于内部射频模块、外部模块以及其他设备（接收机等）的
  固件文件，可从此处通过 S.Port 或 OTA 刷写。将遥控器置于
  [引导程序模式](../getting-started/usb-connection-modes.md)并通过 USB
  连接后，把新固件复制到此处；点按固件文件并选择 **Flash** 即开始更新：

  ![刷写内部射频模块](../assets/system-filemanager-flash.png)
  ![通过 S.Port 刷写 S8R 接收机](../assets/system-filemanager-flash-S8R.png)
  ![通过 OTA 刷写 TD-R18 接收机](../assets/system-filemanager-flash-TD-ISRM.png)
  ![刷写引导程序](../assets/system-filemanager-flash-bootloader.png)

- **`I18n/`** — 语言翻译文件。

- **`Logs/`** — 数据日志。

- **`models/`** — 模型文件本身。这些文件无法在此直接编辑，只能备份或分享。
  自 Ethos v1.2.11 起，模型文件以模型名称命名，而不再是 `model01.bin`
  这样的顺序编号（例如名为 “Extra” 的模型会保存为 `Extra.bin`；第二个
  “Extra” 则为 `Extra01.bin`）。在[模型编辑](../model-setup/model-edit.md)中
  重命名模型时，其文件也会一并重命名——文件名一律为小写（大小写混合的
  显示名称保存在文件内部），并且模型名称中的字符并非全部都能保留到文件名中。
  自 v1.1.0 Alpha 17 起，每个用户创建的模型分类都会拥有各自的子文件夹。

- **`screenshots/`** — [截屏特殊功能](../model-setup/special-functions.md)的输出目录。

- **`scripts/`** — Lua 脚本，可根据需要连同支持文件整理到各自的子文件夹中。
  脚本类型包括 **widgets**（参见[显示屏](../displays/index.md)）、
  **tasks 与 sources**（自定义传感器或飞行后动作——安装于此后，会出现在
  模型的 [Lua](../model-setup/lua-scripts.md) 菜单中），以及 **tools**
  （例如系统菜单下的增稳接收机配置工具）。第三方外部模块各自拥有专属脚本
  与文件夹，例如 `scripts/multi`、`scripts/elrs`、`scripts/ghost`、
  `scripts/crossfire`。

  !!! warning
      Lua 脚本会增加遥控器的启动时间。编写良好的脚本所带来的延迟难以察觉——
      而编写糟糕的脚本几乎可以让启动过程无限延迟。

- **`radio.bin`**（根目录）— 系统设置文件，由遥控器在初始化时自行写入。
  升级固件前请将其与 `models/` 一同备份，以便在需要时降级回退。

- **`firmware.bin`**（根目录）— 将新的遥控器固件文件放到此处，遥控器下次
  与电脑断开连接时便会自动刷写。同一次操作中，SD card/eMMC 与内部闪存盘的
  内容可能也需要更新。

- **`sdcard.version`**（根目录）— SD card 内容版本号，由 Ethos Suite 维护。

## 通过 Bluetooth 分享文件

Ethos 可通过 Bluetooth 在遥控器之间传输文件。在**接收方**遥控器上，于文件管理器中进入目标文件夹，长按 `ENT`，然后选择 **Receive file here**：

![Bluetooth 接收](../assets/system-filemanager-bluetooth-receive.png)

在**发送方**遥控器上，点按文件，选择 **Send file**，然后按两台遥控器上的提示操作：

![Bluetooth 发送](../assets/system-filemanager-bluetooth-send.png)

如果任一遥控器已存在活动的 Bluetooth 连接（遥测、教练连接，或在 X20S/Pro 上的音频连接），系统会询问是否先断开该设备。
