---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 计时器

![计时器](../assets/model-timers.png)

八个完全可编程的计时器，每个都可正计时或倒计时。可通过列标题旁的 **+** 添加，也可通过下方的 **Add** 添加。触摸某个计时器会打开复位/编辑/添加/移动/复制粘贴等选项。

![计时器编辑](../assets/model-timer1-edit.png)

## 通用字段（倒计时与正计时）

- **Value** —— 计时器的当前读数。
- **Name** —— 可编辑。
- **Mode** —— **Up**（正计时）或 **Down**（倒计时）。
- **Start value**（仅倒计时）—— 倒计时的起始值。
- **Alarm Value**（仅正计时）—— 达到该值即视为计时结束；计时器会继续往上计数，但在计时器小组件中显示为红色。
- **Start condition** —— 启动计时器。若 **Stop condition** 保持默认值，则仅由启动条件同时控制启动*和*停止。否则，计时器在启动条件首次成立时启动，并从此持续运行。
- **Stop condition** —— 若未保持默认值，则在计时器运行后由其控制：条件成立时停止，条件不成立时运行。在下面的示例中，计时器在 `ThrottleActive` 成立时启动，并在遥测不再有效时停止：

  ![停止条件](../assets/model-timer1-edit-stop.png)

- **Proportional timing source** —— `---` 表示按实际时间计时。选择其他任何信号源（例如油门摇杆或油门通道）都会按比例缩放计时器的速度：在 −100% 时计时器停止，在 +100% 时以实际时间速度运行，介于两者之间则按比例缩放。
- **Reset** —— 用于复位计时器的开关、功能开关、逻辑开关或微调位置；只要条件成立，计时器就保持在复位状态。
- **Persistent** —— 在断电或切换模型后保留计时器的数值，下次使用该模型时重新载入。
- **Voice** —— 播报该计时器所使用的[语音包](../system-setup/general.md#audio-settings)。

## 音频动作

![添加音频动作](../assets/model-timer1-add-action.png)
![动作类型](../assets/model-timer1-action-type-select.png)
![倒计时动作](../assets/model-timer1-action-countdown.png)

完全灵活的、针对每个计时器的提示配置。每个动作都有一个类型 —— **Countdown**（语音播报）、**Beep countdown**（以提示音代替语音）、**Play file** 或 **Play value** —— 以及：

- **Start** —— 该动作倒计时的起始值。
- **Step** —— 播报间隔，最长 10 分钟（600 秒）。
- **Haptic** —— 播报时伴随振动。

一个典型的三动作组合：

![动作汇总](../assets/model-timer1-actions-summary.png)
![计时器 2 动作](../assets/model-timer2-actions-summary.png)

1. 从剩余 2:00 开始的语音倒计时，每 30 秒播报一次，并伴随振动。
2. 从剩余 0:10 开始的提示音倒计时，每 1 秒一次，并伴随振动。
3. 计时结束时播放自定义文件（例如 `timer-1-elapsed`），并伴随振动。

可通过 **Add** 添加更多动作；列表按优先级顺序执行，**最后一项优先级最高**。

另请参阅[计时器日志显示小组件](../displays/index.md#widget-types)，可查看过往计时记录的运行日志。

![计时器小组件](../assets/model-timers-widget.png)
