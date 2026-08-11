---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 遥控器初始设置

在开始编程任何模型之前需要完成的一次性设置。后续的[教程](index.md)均假定已先完成本页内容。

!!! note
    这些教程并非严格的操作手册——它们假定读者已掌握基本的 RC 术语，并能熟练地在 Ethos 菜单中操作。如果本文中有任何不清楚之处，请先回顾[用户界面与导航](../getting-started/user-interface-and-navigation.md)。

## 第 1 步：为遥控器电池和动力电池充电

按照遥控器附带的说明为遥控器电池充电，并使用与动力电池化学类型相匹配的充电器为其充电——对锂电池组尤其要小心。

## 第 2 步：校准硬件

确认已完成[硬件校准](../system-setup/hardware.md#analogs-calibration)（首次启动时会自动执行），这样遥控器才能知道每个摇杆、电位器和滑块的精确中点与行程极限。每次更换摇杆、电位器或滑块后，都应在 **系统 → 硬件** 中重新校准。

## 第 3 步：进行遥控器系统设置

[系统设置](../system-setup/index.md)涵盖所有模型共用的各项设置，与[模型设置](../model-setup/index.md)中针对单个模型的设置不同。多数默认值可直接使用，但请检查以下项目：

- **[日期与时间](../system-setup/date-and-time.md)** —— 正确设置。
- **[音频 → 语音选择](../system-setup/general.md#audio-settings)** —— 设置语音播报，包括任何自定义音频文件。
- **[控制（摇杆）](../system-setup/controls.md)**：
  - **摇杆模式** —— 模式 1（油门/副翼在右，升降舵/方向舵在左）或模式 2（油门/方向舵在左，副翼/升降舵在右——Ethos 的默认设置）。

    !!! warning
        如果模型按某一种摇杆模式配置，而发射机设置为另一种模式，则接收机上电瞬间电动机可能立即启转。

  - **通道顺序** —— Ethos 默认为 **AETR**（副翼、升降舵、油门、方向舵）；Spektrum/JR 的惯例是 **TAER**，Futaba/Hitec 为 **AETR**。该设置决定新建模型时摇杆输入的分配顺序——之后仍可对各个模型单独调整。

    !!! note "FrSky 增稳接收机"
        此类接收机专门要求使用 **AETR**。当某一功能对应多个舵面时（例如 2 个副翼），向导通常会将它们分组（形成 **AAETR**）——但 SRx 接收机期望的是 **AETRA**/**AETRAE**，因此请在摇杆设置中启用 **[前四通道固定](../system-setup/controls.md#first-four-channels-fixed)**，以确保前四个通道始终严格按 AETR 顺序排列。

- **[电池](../system-setup/battery.md)** —— 设置 **主电压**、**低电压** 和 **显示电压范围**，使其与遥控器实际使用的电池相匹配。
- **[所有者注册 ID](../model-setup/rf-system.md#owner-registration-id)** —— 供 ACCESS 接收机使用，并在多台发射机之间共享以实现 Smart Share。该项虽在模型设置下配置，但实际上等同于系统级设置，因为每个新建模型都会使用它（如有需要，仍可在注册时针对每个接收机单独更改）。

!!! note "单位"
    Ethos 没有全局的公制/英制切换开关——[遥测传感器单位](../model-setup/telemetry.md#editing-a-sensor)需按每个传感器单独设置。
