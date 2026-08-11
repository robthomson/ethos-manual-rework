---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 常规

![常规设置](../assets/system-general.png)

包含显示属性、音频、升降速度提示音（vario）、振动以及顶部工具栏的设置。

## 显示属性

- **Language（语言）** — 菜单显示语言（English、中文、Česky、Deutsch、
  Español、Français、עברית、Italiano、Nederlands、Norsk、Português
  Brasileiro、Polish、Português 等）。
- **Keyboard（键盘）** — 虚拟键盘布局：QWERTY、QWERTZ 或 AZERTY。
- **Brightness（亮度）** — 用于调节背光亮度的滑块；长按 `ENT` 可改为由某个
  信号源控制（例如下面示例中使用滑块），或将其强制为最小/最大值。

  ![亮度菜单](../assets/system-general-brightness-menu.png)
  ![亮度滑块](../assets/system-general-brightness-slider.png)

  !!! note
      如果 **Brightness（亮度）** 与 **Sleep mode brightness（休眠模式亮度）**
      相同，则即使处于“休眠”状态，触摸屏仍保持有效。

- **Wake up（唤醒）** — 选择哪些操作可将背光从休眠中唤醒（可同时启用多项）：
  **Always on（始终开启，永不休眠）**、**Sticks（摇杆）**、
  **Switches（开关）**、**Gyro（陀螺仪，即倾斜遥控器）**。无论如何设置，
  按键始终可以唤醒背光。
- **Sleep（休眠）** — 背光关闭前的无操作等待时间（若 Wake up 设为 Always on，
  该项显示为灰色不可用）。
- **Sleep mode brightness（休眠模式亮度）** — 休眠状态下的背光亮度。
- **Dark mode（深色模式）** — 选择浅色或深色显示主题。
- **Highlight Color（高亮颜色）** — 界面的强调色（默认 `#F8B038`）。

## 音频设置 {: #audio-settings }

![音频设置](../assets/system-general-audio.png)

- **Audio language（语音语言）** — 语音播报所使用的语言。
- **语音选择** — Ethos 支持同时使用多个语音包：

  - **Voice 1（主语音）** — 用于所有内置系统播报。以英语为例，默认可在美式
    （`us`）与英式（`gb`）语音包之间选择，分别读取
    `audio/en/us/system` 与 `audio/en/gb/system`。用于
    [Play Audio 特殊功能](../model-setup/special-functions.md)
    的用户音频文件应分别放在 `audio/en/us/` 或 `audio/en/gb/`。
  - **Voice 2 / Voice 3** — 附加语音包，例如自定义的 TTS 语音。每个语音包都
    需要与 Voice 1 相同的文件夹结构 — 例如名为 “Susan” 的语音需要
    `audio/en/Susan/` 存放用户音频，以及 `audio/en/Susan/system` 存放其系统
    音频（每个语音都需要 `/system` 文件夹，因为 **Play Value** 和计时器播报
    正是从该处读取；每个音频发布包中都附带一份标准系统音频文件的 `.csv`
    清单）。安装完成后，可为每个计时器和每个 Play Audio 功能分别指定语音 —
    甚至可将其设为 Voice 1，从而完全替换系统播报。
  - **Voice “default”** — 自动安装，作为安全的备用方案（同时避免从 1.4.x
    版本升级时出现转换问题）：如果在安装/升级过程中 Voice 1 尚未设置，则会
    被设为 `default`，从 `audio/en/default/system` 读取。常用的 Play Audio
    自定义音频文件位于 `audio/en/default/`。

- **Main volume（主音量）** — 用于调节整体音量的滑块（长按 `ENT` 可改为由
  电位器控制）；调节过程中会播放提示音，便于凭听觉判断音量大小。
- **Audio mode（音频模式）**：
  - **Silent（静音）** — 不发出声音（若已启用，启动时仍会触发
    [静音模式提示](alerts.md)）。
  - **Alarms only（仅报警）** — 仅报警声可闻。
  - **Default（默认）** — 常规提示音。
  - **Often（较多）** — 在数值被推至最小/最大值之外时额外发出错误提示音。
  - **Always（总是）** — 在 Often 的基础上，为普通菜单导航也添加提示音。
  - **Bluetooth**（仅 X20S/HD/Pro/R/RS） — 将音频转发至已配对的 Bluetooth
    设备（耳机等）。选择 **Search Devices（搜索设备）**，将目标设备置于配对
    模式，找到后选中它：

    ![Bluetooth 配对](../assets/system-general-audio-bluetooth.png)
    ![Bluetooth 搜索中](../assets/system-general-audio-bluetooth-searching.png)
    ![已选择 Bluetooth 设备](../assets/system-general-audio-bluetooth-device-selected.png)
    ![Bluetooth 连接中](../assets/system-general-audio-bluetooth-connecting.png)
    ![Bluetooth 已连接](../assets/system-general-audio-bluetooth-connected-ok.png)

    随后 **Speaker mute（扬声器静音）** 用于控制内置扬声器 — 可设为始终静音、
    仅在遥测激活时静音，或由某个信号源（例如开关）控制。遥控器会记住已配对的
    设备；正常使用时请先开启遥控器，再开启 Bluetooth 设备，并在其连接后等待
    几秒钟，使扬声器静音重新生效。

## Vario（升降速度提示音）

![Vario 音频](../assets/system-general-audio-vario.png)

- **Volume（音量）** — vario 提示音的相对音量。
- **Pitch zero（零点音调）** — 爬升率为零时的音调。
- **Pitch max（最大音调）** — 达到最大爬升率时的音调。
- **Repeat（重复间隔）** — 零点音调时两次提示音之间的间隔。

有关 vario 的其他行为，另请参阅 [遥测](../model-setup/telemetry.md) 中的
VSpeed 传感器以及
[Play Vario 特殊功能](../model-setup/special-functions.md)。

## Haptic（振动）

- **Strength（强度）** — 用于调节振动强度的滑块。
- **Mode（模式）** — 选项与上面的 Audio mode 相同。

## 存储位置（X18 与 X20 Pro/R/RS） {: #storage-location-x18-and-x20-prorrs }

这些遥控器内置 8GB eMMC。Ethos 默认使用内部存储，因此 SD card 为可选配件 —
但你可以选择使用 eMMC、SD card，或两者组合。如果要将系统和模型移至 SD card，
请在切换存储位置**之前**先把相关的文件夹/文件（包括音频和图片）复制过去。

![存储位置](../assets/system-general-storage.png)

## 顶部工具栏

![顶部工具栏设置](../assets/system-general-topbar.png)

- **Digital voltage（数字电压）** — 在顶部工具栏中以数值而非条形图显示遥控器
  电池电压。
- **Digital RSSI（数字 RSSI）** — 同上，适用于 2.4GHz 与 900MHz 的 RSSI。
- **Select model at power on（开机时选择模型）** — 启动时先显示模型选择界面，
  在上一个模型的检查清单提示出现之前，让你可以直接切换模型而无需先关闭这些提示。
  默认高亮显示上次使用的模型。

  ![启动时选择模型](../assets/system-general-model-start.png)

## USB 模式预选

![USB 模式](../assets/system-general-usb.png)

遥控器通过 USB 连接到 PC 时自动执行的操作：

- **Not set（未设置）** — 连接时提示进行选择。
- **Joystick（手柄）** — 立即进入手柄模式，用于 RC 模拟器。
- **Ethos Suite** — 立即进入 Ethos 模式以配合
  [Ethos Suite](../ethos-suite/index.md) 使用。
- **Serial（串口）** — 立即进入串口模式，以 115200 bps 通过 USB-Serial 输出
  Lua 调试信息（Windows 可能需要安装虚拟 COM 端口驱动）。
