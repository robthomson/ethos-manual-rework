---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 电池容量告警

针对**已消耗容量**（mAh）而非电压发出告警——这是衡量电池组实际用掉多少电量的更直接方式。根据所装硬件的不同，有两种实现途径。

## 方案 A：Neuron 系列电调

FrSky 的 Neuron 电调可直接上报消耗量——无需计算传感器。将[接收机选项 → 回传端口](../system-setup/devices.md)设为 S.Port，接好 Neuron 的回传线，然后[发现传感器](../model-setup/telemetry.md#discovering-sensors)——需要关注的传感器是 **ESC Consumption**。

1. 基于 `ESC Consumption` 添加一个[逻辑开关](../model-setup/logical-switches.md)，当数值高于（例如）900mAh 时为真——对于计划降落时仍保留约 30% 余量的电池组来说，这大约相当于其容量的 60%。
2. 添加一个[播放音频特殊功能](../model-setup/special-functions.md)，激活条件设为这个新建的开关，并加入针对 `ESC Consumption` 的 **Play value** 步骤。

作为第二重保障，Neuron 电调同时还会上报 **ESC Voltage**——按照[低电压告警](low-battery-warning.md)中的方法再设置一个逻辑开关（低于 3.4V/片，例如 4S 电池组为 13.6V），并配上各自的播放音频功能，每 5 秒重复一次。

## 方案 B：电流传感器 + 计算传感器

如果电调不上报消耗量，可以用电流传感器（例如 FrSky FASxxx）配合[计算得出的 **Consumption** 传感器](../model-setup/telemetry.md#calculated-sensors)来完成同样的工作。

### 1. 连接并发现

![电流传感器](../assets/how-to-consumption-telemetry-current-sensor.png)

接好电流传感器的 S.Port 线并进行发现——它会显示为 **Current**。将其 **Range** 设为与传感器相符（例如 FAS100 设为 0–100A）：

![电流传感器编辑](../assets/how-to-consumption-telemetry-current-sensor-edit.png)

### 2. 创建计算得出的 Consumption 传感器

![创建计算传感器](../assets/how-to-consumption-create-calc-select.png)
![Consumption 传感器](../assets/how-to-consumption-create-calc-sensor.png)

在回传（Telemetry）中选择 **Create Calculated Sensor** → **Consumption**。将单位设为 `mAh`，**Range** 设为电池组容量（例如 2800mAh）；**Source** 设为 `Current`。

![传感器编辑](../assets/how-to-consumption-sensor-edit.png)
![传感器编辑 2](../assets/how-to-consumption-sensor-edit2.png)

将 **Reset** 设为系统事件 `!Telemetry Active`——选择 **Telemetry Active**，长按 `ENT`，然后选择 **Invert**——这样一旦回传中断（即模型断电），累计总量便会自动清零。

### 3. 里程碑播报

![200mAh 增量逻辑开关](../assets/how-to-consumption-lsw-delta200mAh.png)

基于 `Consumption` 添加一个使用 **Δ > X** 功能的逻辑开关，使其每增加固定步长就触发一次——例如每 200mAh，这正好是 2800mAh 电池组容量的一个便于计算的分数。

!!! tip
    将 **Check interval** 设为 `---`（无限），使其持续向下一个阈值累加，而不是在固定时间窗结束后清零。调试期间可给 **Min Duration** 一个较小的非零值——设为 0.0 时触发过于短暂，屏幕上根本看不到。

添加一个播放音频功能，激活条件设为该开关，并加入针对 `Consumption` 的 Play value 步骤：

![播放增量播报](../assets/how-to-consumption-sf-play-delta200mAh.png)
![Play value：consumption](../assets/how-to-consumption-sf-play-value-consumption.png)

### 4. 低容量告警

![第二个逻辑开关](../assets/how-to-consumption-lsw2-play-battlow.png)

第二个逻辑开关在超过一个固定的低容量阈值时触发一次——例如 2800mAh 电池组用掉 2000mAh——并配以每 10 秒重复一次的播放音频功能，直到模型被复位：

![低电量时播放数值](../assets/how-to-consumption-sf2-play-battlow.png)
![Play value：低电量时播报 consumption](../assets/how-to-consumption-sf2-play-value-consumption.png)
