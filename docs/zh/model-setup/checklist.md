---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 检查清单

![检查清单](../assets/model-checklist.png)

一组飞行前安全检查，在遥控器开机和/或加载模型时运行。内置检查项包括静音模式、未设置失控保护、开关/电位器位置、遥控器电池与 RTC 电池——开关检查会显示每个开关需要拨动的方向，在警告界面上以红点标示：

![启动时的检查清单](../assets/model-checklist-at_start.png)

!!! note
    无论屏幕上的警告提示如何，按 `OK` 或 `RTN` 都会完全跳过飞行前检查。

## 油门检查

![检查功能](../assets/model-checklist-check_function.png)

启用后选择一个运算符——`<`（小于）、`~`（约等于）或 `>`（大于）——与设定值进行比较；如果油门摇杆超出该比较所允许的范围，则会发出警告。

## 失控保护检查

如果当前模型尚未设置[失控保护](rf-system.md#failsafe)，则发出警告。

!!! tip
    强烈建议保持此项启用。

## 开关检查

![开关](../assets/model-checklist-switches.png)
![开关检查选项](../assets/model-checklist-switches-options.png)

可为每个开关指定启动时所需的位置（在[系统设置 → 硬件](../system-setup/hardware.md#switches-settings)中自定义了名称的开关会显示这些名称）。**加载所有开关位置**会将*当前*的实际物理位置作为所有未标记为**不检查**的开关的目标位置。

## 功能开关检查

![功能开关](../assets/model-checklist-function-switches.png)
![功能开关检查选项](../assets/model-checklist-function-switches-options.png)

与上述原理相同，适用于六个[功能开关](model-edit.md#function-switches)。**加载所有功能开关位置**的工作方式与上文相同。

## 电位器 / 滑块检查

![电位器](../assets/model-checklist-pots.png)
![电位器检查选项](../assets/model-checklist-pots-options.png)

要求启动时电位器/滑块处于特定位置，可对每个控件单独设置（`~`/`<`/`>`，与油门检查相同）。**加载所有电位器位置**会自动采集当前位置——之后请仔细核对自动选定的运算符，因为 `~` 与 `<`/`>` 可能与您的实际意图不符。

## 用户自定义文本

![用户检查清单文本](../assets/model-checklist-user-checklist.png)

为模型安装相应文件后，可将纯文本或增强文本文件作为启动检查清单的一部分显示。完整设置方法请参阅[操作指南：用户自定义文本检查清单](../how-to/user-defined-checklist.md)。
