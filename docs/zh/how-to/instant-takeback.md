---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 教练功能的即时接管

这是对[教练](../model-setup/trainer.md)功能的一项实用增强：教官不再只能依靠开关来接管，只需拨动副翼或升降舵摇杆即可立即收回控制权——出现意外时无需先去寻找教练开关。

教练开关仍用于开始教学；教练功能本身由一个[锁存型逻辑开关](../model-setup/logical-switches.md#sticky)驱动，该逻辑开关可由开关关闭**或**检测到教官摇杆动作而取消。

![教练功能激活](../assets/trainer-take-back-trainer-active.png)

## 1. 副翼检测逻辑开关

![副翼输入检测](../assets/trainer-take-back-ailinput.png)

该逻辑开关对副翼摇杆使用 **|A| > X**，当摇杆向任一方向偏离中位超过 10% 时为真。长按副翼信号源并选择 **Ignore trainer input**（忽略教练输入），这样*学员*的副翼动作（通过教练链路传入）就不会同时触发它：

![忽略教练输入](../assets/trainer-take-back-ailinput-ignore.png)

## 2. 升降舵检测逻辑开关

![升降舵输入检测](../assets/trainer-take-back-eleinput.png)

采用相同的方式，只是作用于升降舵摇杆。

## 3. 取消逻辑开关

一个 **OR** 逻辑开关，当副翼检测开关或升降舵检测开关为真时为真，**或者**教练开关（例如 SD）未处于下位时为真——也就是说，“教官拨动了摇杆”或“教练开关被关闭”这两种情况中的任意一种都会结束本次教学。

## 4. 教练启用锁存型逻辑开关

![停用教练功能](../assets/trainer-take-back-disable-trainer.png)

一个 **Sticky**（锁存型）逻辑开关：**Trigger ON** 为教练开关（SD 拨到下位），**Trigger OFF** 为第 3 步中的取消开关。将该锁存开关——将其命名为 `TrainerActive`——用作教练功能自身的激活条件，替代原始开关。

## 5. 语音提示

添加[播放音频特殊功能](../model-setup/special-functions.md)，在 `TrainerActive` 变为真以及解除时进行播报，这样两位飞手都能通过清晰的语音提示准确知晓控制权何时交接。
