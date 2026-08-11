---
translated_from: f37a19af41cd6ab9767ee0c39f708b7f8a1966d6
---

# 截图流水线

本手册中的每一张截图（目前约 590 张，位于 `docs/en/assets/` 下）都是通过脚本驱动真实的 Ethos 模拟器自动截取的，而非手工完成。相关工具位于旧的
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual) 仓库的
`english/manual/` 目录下，并且**尚未移植到本仓库**——本页面记录其工作原理，以便日后完成移植，同时也便于在此期间无需从零开始即可重新生成或扩充截图。

## 结构说明

手册的每个菜单/章节都对应一组文件：

- `manual/macros/<name>.lua` — 基于模拟器 Lua API（见下文）编写的脚本，用于导航到特定界面，并在每个值得截图的位置调用
  `simulator.screenshot(path)`。
- `manual/<name>.sh` — 单行封装脚本，为特定遥控器启动模拟器二进制文件，并指向对应的宏脚本，例如：

```bash
ETHOS='/mnt/c/Program Files (x86)/FrSky/Ethos'
"${ETHOS}/X20S/simulator.exe" --read-only --no-gui --no-audio \
  --radio-settings ./x20s-en.bin --sd-directory ./sd --flash-directory ./flash \
  --exec ./macros/model-mixes.lua
```

`manual/screenshots.sh` 会依次运行所有宏脚本，以重新生成完整的截图集。每个章节都有独立的 `.sh` 文件，因此可以只重新生成某一个页面的截图，而无需全部重跑（每个宏脚本的耗时从几秒到一分钟以上不等）。

主要命令行参数：

- `--read-only` — 不保存运行期间所做的任何更改。
- `--no-gui` / `--no-audio` — 近似无头运行；部分宏脚本仍然需要 GUI，因为没有 GUI 时模拟器会“跳过”（参见 `screenshots.sh` 中的注释）。
- `--radio-settings <file>.bin` — 启动时使用哪台遥控器的已保存设置（这正是使截图与语言、遥控器型号相关的原因——德语版本的运行会使用德语的 `.bin` 文件）。
- `--sd-directory`、`--flash-directory`、`--documents-directory`、
  `--audio-directory` — 指定模拟器所使用的模型/固件/文档/音频内容，使截图呈现有意布置的内容，而不是真实 SD card 上的任意内容。
- `--exec <script>.lua` — 启动后要运行的宏脚本。

每个遥控器系列（X20S、X20 Pro、X20 Pro AW、X18S）都有各自的模拟器二进制文件，并且每种语言都需要各自的 `--radio-settings` 文件（例如
`x20s-en.bin`、`x20pro-en.bin`），因为不同遥控器的界面略有差异，而设置文件同时也携带语言信息。

## 宏 API

宏脚本是纯 Lua 代码，通过全局对象 `simulator` 进行操作：

| 调用 | 用途 |
|---|---|
| `simulator.loadModel("name.bin")` | 在导航之前加载指定的模型文件——手册的每个章节都使用一个专门配置好的模型来演示该章节内容（参见下方的模型列表）。 |
| `simulator.pressKey(KEY_X, [holdSeconds])` | 按下硬件按键——`KEY_ENTER`、`KEY_RTN`、`KEY_MDL`、`KEY_SYS`、`KEY_DISP`、`KEY_PAGE` 等。指定按住时长即为长按（用于打开上下文菜单）。 |
| `simulator.turnRotaryEncoder(n)` | 转动编码器 `n` 格（负值为反向）——在各字段之间移动光标的主要方式。 |
| `simulator.touch(x, y)` | 点击指定的屏幕坐标——用于只能通过触摸才能到达的位置（例如切换键盘布局）。 |
| `simulator.setAnalog(channel, value)` | 直接设置摇杆/电位器/滑块的位置（`0`-`3` 为四个主摇杆，`ANALOG_LAST_SLIDER` 为最后一个滑块），使截图显示有意设定且可复现的数值，而不是模拟器的默认值。 |
| `simulator.setSwitch(n, position)` | 设置物理开关的位置。 |
| `simulator.setDateTime({...})` | 固定模拟器的时钟，使截图中的时间戳（以及任何与时间相关的内容）在多次运行之间保持一致。 |
| `simulator.screenshot(path)` | 将当前屏幕截取为 PNG 文件，路径相对于宏脚本的工作目录（因此各宏脚本内使用 `../assets/...` 形式的路径）。 |
| `simulator.connectUsb()` | 模拟接入 USB，用于截取 USB 菜单。 |
| `simulator.sleep(seconds)` | 在截图之前等待动画或遥测数值稳定。 |

`manual/macros/common.lua` 会被大多数宏脚本用 `dofile` 加载，其作用仅是固定日期与时间，使每个宏脚本都从相同的模拟时刻开始运行。

## 各章节所用的模型

`manual/notes.txt`（非正式沿用，尚未复制到本仓库）记录了每个宏脚本所依赖的 `.bin` 模型文件及其原因——例如
`model-mixes.lua` 使用 `rarebear.bin`，`model-fm.lua` 使用 `zblank.bin`（一个刻意留空飞行模式配置的模型），`model-trims.lua` 使用
`blaster.bin`（配置了偏置微调，用于演示微调范围）。将该文件中的说明整理为正式文档也属于下述第二阶段工作的一部分。

## 移植到新仓库需要做的工作（尚未完成）

- 决定宏脚本是直接从本仓库运行（需要本地安装 Ethos 模拟器，与旧仓库一样），还是通过 CI 运行并在工作流中打包/下载模拟器。
- 将扁平的 `../assets/...` 输出路径重构为符合本仓库按页面、按语言的资源布局（`docs/<locale>/assets/`）。
- 一旦出现 `en` 之外的语言，每种语言都需要一个 `--radio-settings ... .bin` 文件并单独运行一次截图流程——截图与界面语言相关，无法在不同语言之间共用。
- 决定现有约 40 个宏脚本中有多少可以原样沿用，有多少需要针对本仓库当前的导航结构重写（部分宏脚本生成的截图所对应的章节，已无法与本手册的页面结构一一对应）。
