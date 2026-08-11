---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 操作

## 欢迎区

**更新新闻** — 更新前的发布说明与备份建议。Ethos 1.6.0+ 要求内置 RF 模块与 TD/TW/AP/AP Plus 接收机升级至 v3.0.1+，才能使用其改进功能。启用 **Pre-releases**（并将服务器设为 GitHub — 参见 [Suite 设置](#suite-settings)）后，此处还会列出预发布版本，以及完整的发布历史。

**Ethos 网页** — 内嵌显示 ethos.frsky-rc.com：资源、模型模板链接以及支持的遥控器列表。

## 遥控器区

管理已连接的遥控器。将遥控器以 [bootloader 模式](../getting-started/usb-connection-modes.md#bootloader-mode)开机并通过 USB 连接 — 检测成功后，Suite 会显示遥控器型号（例如 "X20"）。

### 遥控器信息

- **Ethos** — 已安装的固件/bootloader 版本；若版本过旧，**Manage Ethos** 会跳转至更新页面。
- **RF Module** — 已安装的内置 RF 模块固件；若版本过旧，**Manage internal module** 会跳转至更新页面。
- **Model manager** / **Lua library** / **Download center** — 通往这些工具的快捷入口。

### 更新 Ethos {: #updating-ethos }

**Ethos** 选项卡并列显示固件、bootloader、SD card/eMMC（音频文件）以及闪存（系统位图）的版本 — 闪存中的系统文件现在随固件一并更新，不再单独管理。

- **Write outdated components** — 仅更新版本落后的组件。
- **Write all components** — 无论版本如何，更新全部组件。
- 单独的 **Write firmware**、**Write bootloader**、**Write audio files** 选项，各自通过点击所选项旁的深灰色按钮执行。
- **Flash from a local file** — 跳过下载，使用磁盘上已有的固件文件。

先选择发布版本意味着先选择**分支**（Stable/Testing），再选择版本。更新前会提示先进行备份（**Go to backup page**）— 请务必备份。如果内置 RF 模块版本低于 v3.0.1，Ethos 1.6.0+ 要求先升级模块才能继续（**Go to Module manager** 会自动刷写，随后 Ethos 更新继续）— 并且 TD/TW/AP/AP Plus 接收机在之后需要删除并重新发现遥测，才能获取更新后的传感器名称。

更新进度会逐步显示（切换至 bootloader、下载、复制、卸载、写入、刷新、"Update successful!"）— 遥控器自身的屏幕也会同步显示写入进度。

!!! note "预发布版本更新"
    预发布版本的文件可能在版本号不变的情况下发生变化，Suite 无法检测到这一点 — 当你正在使用的预发布版本转为正式发布版本后，务必重新刷写一次。如不确定，可在 [System → Info](../system-setup/information.md) 查看固件日期。

!!! note "从 Ethos 1.2.8 或更早版本更新"
    从如此旧的版本升级时，Suite 可能无法完全自动刷写固件/bootloader — 此时会出现引导式手动刷写对话框。无论采用哪种方式，拔出 USB 前都要手动弹出驱动器。

系统位图文件现在会随固件自动更新（无需单独管理）；音频文件通过 **Write all components** 或 **Write audio files** 更新（下载所选语言包，例如 "English audio pack"）。

### RF 模块管理器

选择一个版本（通常是最新版）并点击 **Flash module**，即可直接更新内置 RF 模块的固件 — 完成后会确认 "...has been flashed successfully"。上文提到的强制 v3.0.1 升级流程也会自动触发此操作。

### Ethos 模式

**Switch to Ethos** 使遥控器退出 bootloader 模式并重启进入 Ethos 运行状态（遥控器上显示绿色 USB 图标，Suite 标题栏不再显示 "(Bootloader Mode)"）。要使用 **Download center** 将遥控器作为代理来刷写模块、接收机、传感器和舵机，必须进入此模式。此后该按钮会变为 **Switch to Bootloader** 以便切回。**Eject Drives** 用于安全断开遥控器连接。

### 模型管理器

将模型文件与设置备份到磁盘，或恢复之前的备份。

!!! warning
    恢复操作**不会**恢复固件 — 恢复模型/设置后，需另外刷写与该备份实际匹配的固件版本（参见[更新 Ethos](#updating-ethos)），因为模型文件不向后兼容。

- **Backup Location** — 浏览选择文件夹（按遥控器型号分别记忆）；下方会显示最近一次备份的日期/时间。
- **Backup** — 保存模型文件，并同时记录当前的 Ethos 版本。
- **Restore** — 选择要恢复的组件：Audio（默认关闭）、Scripts、Screenshots、System Bitmaps（默认关闭 — 现在随固件一并管理）、Models（包括与其一同存放的任何[用户自定义检查清单](../how-to/user-defined-checklist.md)文本文件）、Language、User Bitmaps、Logs、System Settings。

### Lua 库

浏览并一键安装 FrSky 远程库中的 Lua 脚本/工具（或从本地 zip 安装）；一旦存在已安装的脚本，它们会与远程目录一同显示。

## 工具区

- **Download center** — 从 FrSky 网站下载任意固件，并（在遥控器处于 Ethos 模式时）将其作为代理，刷写通过 S.Port 升级接口连接的模块、传感器、舵机或接收机。从列表中选择产品（例如 TW SR8 接收机），浏览可用的 **assets**，点击 **Download** 保存到本地，或点击 **Flash** 直接写入已连接的设备 — 进度条会跟踪刷写过程，最后显示 "...has been flashed successfully!"

- **Image manager** — 按所选尺寸将图像转换为 Ethos 的原生格式（32 位 BMP、RGB，仅在需要时添加 alpha 通道），并保持宽高比。参考尺寸：模型图像 300×280（X20）/ 180×168（X18）；全屏图像 800×480（X20）/ 480×320（X18）— 位图命名规则参见[文件管理器](../system-setup/file-manager.md#top-level-folders)。它还可直接浏览遥控器的 `bitmaps/gps`、`bitmaps/models` 和 `bitmaps/user` 文件夹，并支持上传。用 **+** 将图像加入转换列表（不支持 TIFF），选择输出路径（本地文件夹；直接写入遥控器的模型/用户/GPS 图像目录；或当前打开的遥控器文件夹），并可选择自动打开输出文件夹或强制添加 alpha 通道。

- **Audio manager** — 将音频转换为 Ethos 的格式（PCM 线性、32kHz、单声道、16 位小端）。用 **+** 添加文件，选择本地文件夹或直接发送到遥控器的 `audio` 文件夹（之后需将文件移入正确的语音子文件夹），并可选择自动打开目标位置。

- **Lua development tools** — **Lua Docs** 链接到 Ethos Lua 参考指南（另可参阅 rcgroups 上的 *FrSky - ETHOS Lua Script Programming* 主题帖）；**Lua Demo Scripts** 链接到 Ethos-Feedback-Community GitHub 上的示例脚本；**Debug** 打开实时日志窗口，显示遥控器处于 Serial 模式时通过 USB-Serial 发送的 Lua `print()` 跟踪输出：

  1. 按常规方式将遥控器连接到 Suite，并切换到 Ethos 模式。
  2. 在任意代码编辑器中直接编辑遥控器已挂载驱动器上的 Lua 脚本。
  3. 打开 **Lua Development Tools** → **START DEBUG** — 这会将遥控器重启进入 Serial/调试模式并重新初始化脚本。
  4. 所有运行中脚本的 `print()` 输出都会实时传送到 Suite 的终端窗口。
  5. **STOP DEBUG** 切回正常的 Ethos 模式以便继续编辑。

- **DFU Flasher** — 通过关机状态下的 USB（DFU）连接刷写 bootloader，即使固件完全损坏也能工作，因为底层的 ST bootloader 位于 ROM 中。点击 **Select Bootloader** 选择已下载的文件（Suite 会报告其版本/适用性），连接**已关机**的遥控器，然后点击 **Flash**。

  !!! note "\"Radio connection is not detected!\""
      通常是 DFU 驱动缺失或不正确所致。大多数 Windows 10+ 电脑可用默认 USB DFU 驱动处理 Tandem 系统，但 Windows Update 有时会将其替换为无法工作的通用驱动 — 请检查设备管理器，并考虑使用 Impulse Driver Fixer 之类的工具。Horus X10 用户尤其可能需要手动安装 STM32 bootloader USB 驱动（使用 Impulse Driver Fixer 或 Zadig），因为 Windows 10 默认不会安装该驱动。

- **Repair Tool** — 适用于 X18/S、TW Lite、XE 以及 X20 Pro/R/RS：当遥控器无法读取 NAND 或无法保存设置时，重新格式化内部存储。

## 其他区

- **Documentation** — 链接到 Ethos-Feedback-Community GitHub、官方 Ethos 手册（可下载）以及 Ethos Suite 常见问题解答。
- **Ethos Github** — 发布版本与问题跟踪（提交新问题前请先搜索已有问题）。

### Suite 设置 {: #suite-settings }

- **Language** — 捷克语、德语、英语、西班牙语、法语、希伯来语、意大利语、荷兰语、挪威语、葡萄牙语、斯洛文尼亚语、中文。
- **Server location** — **FrSky server** 或 **GitHub**（上文所述的预发布版本访问需要选择后者）。
- **Debug options** — 开关致命错误弹窗；启用完整的 Suite 调试日志（不仅记录崩溃）；打开日志文件夹。
- **Version** / **Update Suite** — 当前版本，以及手动检查更新。
- **About** — 对所使用的第三方组件的致谢。

## 命令行操作

Ethos Suite 可从终端运行：

| 参数 | 作用 |
|---|---|
| `--help` | 显示命令行帮助。 |
| `--version` | 显示已安装的 Suite 版本。 |
| `--list-radios` | 列出所有受支持的 FrSky 遥控器。 |
| `--radio-components --radio {RADIO}`（或 `--radio auto`） | 列出已连接遥控器的组件及其路径。`auto` 表示自动检测；若连接了多台遥控器，则需指定 `{RADIO}`。 |
| `--get-path {COMPONENT}` | 获取某个组件的路径 — `BITMAPS`、`SCRIPTS`、`SCREENSHOTS`、`AUDIO` 或 `I18N`。 |
| `--serial start` \| `--serial stop` | 启用/禁用串口调试模式。 |

!!! note
    除非识别到有效命令，Suite 根本不会启动。
