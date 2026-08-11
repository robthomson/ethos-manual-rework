---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# 特殊功能

![特殊功能菜单](../assets/model-sf-menu.png)

当某个条件成立时，特殊功能会触发一个动作——播放音频、截屏、写入日志、震动反馈等等。最多支持 100 条；默认没有任何条目。用 **+** 添加一条；点击已有条目可进行 **编辑**/**移动**/**复制粘贴**/**克隆**/**删除**。

![添加特殊功能](../assets/model-sf-add.png)
![移动](../assets/model-sf-move.png)

## 所有动作共有的字段

- **状态** — 在不删除的情况下启用/禁用该功能。
- **激活条件** — **始终开启**，或由开关/功能开关/逻辑开关/微调位置或飞行模式控制。在某个开关上长按 `ENT` 并勾选 **取反**，即可反转其逻辑（例如 `SG-up` 变为 `!SG-up`，即在 SG *不* 处于上位时激活）。
- **全局** — 将该功能添加到**所有**模型，包括现有模型和以后新建的模型。如果某个模型已存在配置完全相同的本地功能，全局功能会作为一条额外条目添加；再次关闭"全局"时，除当前选中的模型外，其余所有模型中的该功能都会被移除。全局功能保存在 `radio.bin` 中；本地功能保存在模型文件中。

## 动作 {: #actions }

**复位** — 复位 **飞行数据**（遥测 + 计时器）、**所有计时器** 或 **全部遥测**。

![复位](../assets/model-sf-reset.png)

**截屏** — 将截图保存到 SD card/eMMC 上的 `screenshots/` 目录。

![截屏](../assets/model-sf-screenshot.png)

**设置失控保护** — 通过内置或外置射频**模块**，将当前各通道位置记录为失控保护值。

![设置失控保护](../assets/model-sf-set-failsafe.png)

**播放音频** — 功能最丰富的动作，支持完整的播放序列：

![播放音频](../assets/model-sf-play-audio.png)

- **语音** — 选择最多 3 种已配置语音中的一种（参见 [通用设置](../system-setup/general.md#audio-settings)）。
- **重复** — 播放一次，或按可设定的间隔重复（最长 10 分钟）。
- **启动时跳过** — 抑制该功能在开机启动过程中触发。
- **序列** — 最多 100 个步骤，每一步可以是：

  - **播放文件** — 播放所选的音频文件。

    ![播放文件](../assets/model-sf-play-audio-add-play-file.png)

  - **播报数值** — 语音播报某个信号源的值：模拟量、开关、逻辑开关、微调、通道、陀螺仪、系统时钟、教练、计时器或遥测。

    ![播报数值](../assets/model-sf-play-audio-add-play-value.png)

  - **等待时长** — 固定的暂停时间，最长 10 分钟。
  - **等待条件** — 暂停序列，直到条件成立。

  ![添加序列行](../assets/model-sf-play-audio-add-line.png)
  ![序列行类型](../assets/model-sf-play-audio-add-line-type.png)

  例如：当逻辑开关 `VFRlow` 变为激活时播放 `vfrlow.wav`，然后播报记录到的 VFR 最小值——

  ![文件之后播报数值](../assets/model-sf-play-audio-add-play-value-add-line.png)

  ——或者让序列暂停，直到开关 SH 拨到下位后再继续：

  ![带等待条件的序列](../assets/model-sf-play-audio-add-sequence.png)

  点击任一序列行即可编辑、添加、重新排序或删除：

  ![序列管理](../assets/model-sf-play-audio-add-sequence-management.png)

**震动** — 震动反馈：

![震动](../assets/model-sf-haptic.png)

- **模式** — 单次、两次、三次、五次或极短促。

  ![震动模式](../assets/model-sf-haptic-pattern.png)

- **强度** — 1–10（默认 5）。
- **重复** — 一次，或按设定间隔重复。
- **选择震动马达** — 在带有摇杆震动马达的遥控器上（X20 Pro AW、X20RS，或升级了 MC20R 摇杆的 X20 Pro/X20R——参见 [硬件](../system-setup/hardware.md#radio-specific-hardware-options)）：**默认**（内置震动）、**全部马达**、**左摇杆** 或 **右摇杆**。

  ![X20 Pro AW 上的震动](../assets/model-sf-haptic-x20proaw.png)

**写入日志** — 将 `.csv` 日志写入 SD card/eMMC 上的 `Logs/` 目录，时间戳取自 RTC（这对事后区分各次飞行记录至关重要）：

![写入日志](../assets/model-sf-write-logs.png)

- **写入间隔** — 100–500ms。
- **摇杆/电位器/滑块**、**开关**、**逻辑开关**、**通道** — 可独立开关的日志记录类别。

  **查看日志**：在文件管理器中打开 `/Logs` 下的日志文件。选择要绘制的通道（默认选中 RSSI）；用旋转编码器或滑动手势平移，按住 `PAGE` 同时旋转编码器可缩放。按 `DISP` 将焦点跳转到右侧第一个列按钮。

**播放文本**（仅 X20 Pro）— 使用机内文字转语音，而不是预录音频文件：

![播放文本](../assets/model-sf-x20pro-play-text.png)

- **文本** — 要朗读的字符串。全部大写会逐字母拼读（例如 "OFF" → "O-F-F"）；小写则作为单词朗读（"off"）。
- **重复**、**启动时跳过** — 同上。

**跳转到屏幕** — 将显示切换到指定屏幕，例如按下按钮时跳转到某接收机的飞行数据记录：

![跳转到屏幕](../assets/model-sf-go-to-screen.png)
![屏幕选项](../assets/model-sf-go-to-screen-options.png)

**锁定触摸屏** — 锁定触摸屏以防误操作（也可在主页界面同时按住 `ENT` + `PAGE` 1 秒直接锁定）：

![锁定触摸屏](../assets/model-sf-lock-touchscreen.png)

**载入模型** — 触发时载入指定的**模型**，并可选择在实际切换前显示**确认**提示：

![载入模型](../assets/model-sf-load-model.png)

**播放升降音** — 由所选信号源驱动升降音（通常是 FrSky 升降速度计的 VSpeed 传感器，但任何以 m/s 为单位的传感器均可）：

![播放升降音](../assets/model-sf-play-vario.png)
![升降音信号源：VSpeed](../assets/model-sf-play-vario-vspeed.png)

- **范围** — 映射为音调高低的爬升/下降速率，默认 ±10m/s（最大 ±100m/s）。高于 **中心** 区间时，音调随爬升率线性升高，直至范围最大值（最大速率对应的音调在 [通用设置 → 升降音](../system-setup/general.md#vario) 中设定）；下降时发出连续音，音调朝范围最小值逐渐降低。
- **中心** — "零爬升"区间，默认 ±0.3m/s（最大 ±2m/s）；在此区间内音调保持恒定（零速率对应的音调同样在通用设置 → 升降音中设定）。将 **蜂鸣**→**静音** 可完全关闭提示音。

  ![升降音范围/中心选项](../assets/model-sf-play-vario-options.png)
