---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 低电压警告

在**负载状态下**监测动力电池电压并在低于阈值时发出警报，比依赖固定计时器更为可靠——使用诸如 FrSky FLVSS 之类的传感器即可轻松实现。

## 1. 连接并搜索传感器

![LiPo 遥测传感器](../assets/how-to-low-batt-telemetry-lipo-sensor.png)

将[接收机选项 → 遥测端口](../system-setup/devices.md)设置为 **S.Port**，通过 S.Port 线将 FLVSS 连接至接收机，然后在[遥测](../model-setup/telemetry.md)中启用**搜索新传感器**——LiPo 传感器便会与其他已搜索到的传感器一同出现。

## 2. 添加逻辑开关

![电池低电压逻辑开关](../assets/how-to-low-batt-lsw-battlow-lipo.png)

新增一个[逻辑开关](../model-setup/logical-switches.md)，以 Lipo 传感器作为其信号源。在高亮的传感器上长按 `ENT`，即可选择要使用该传感器的哪一项数值：

![选择最低单节电压](../assets/how-to-low-batt-lsw-battlow-lipo-select-lowest.png)

- 电池组最低电压 / 电池组最高电压
- **最低单节电压** / 最高单节电压
- 电芯数量
- 各单节电压（仅当传感器实际连接至已对频的接收机且已接入 LiPo 电池时才可选择）

选择 **Lowest**（最低单节电压）——这正是 LVC 式保护所关注的数值。

![已选择最低单节电压](../assets/how-to-low-batt-lsw-battlow-lipo-lowest.png)

将比较值设为约 **3.4V**，并将**激活延时**设为 **4 秒**——当最低单节电压连续 4 秒或更长时间读数低于 3.4V/节时，该开关变为真。（在**负载状态下**为 3.4V 的电压，在卸除负载后通常会回升至约 3.7V，因此该阈值反映的是真实的电压下垂，而非瞬时噪声。）

![完成的逻辑开关](../assets/how-to-low-batt-lsw-summary.png)

## 3. 添加特殊功能

![特殊功能：BattLow](../assets/how-to-low-batt-sf-battlow.png)

添加一个[播放音频特殊功能](../model-setup/special-functions.md)，将**激活条件**设为 `BattLow` 逻辑开关，选择一种语音，并在**序列**中为 LiPo 总电压添加一个**播放数值**步骤：

![播放数值：LiPo](../assets/how-to-low-batt-sf-play-value-lipo.png)
![序列汇总](../assets/how-to-low-batt-sf-play-value-lipo-summary.png)

将**重复**设为 10 秒后，只要最低单节电压持续低于 3.4V/4 秒的阈值，遥控器便会每 10 秒播报一次 LiPo 电压。
