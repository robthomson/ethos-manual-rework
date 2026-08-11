---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 设备

![设备](../assets/system-devices.png)

在菜单中称为 **Device config（设备配置）** —— 用于配置通过 S.Port/FBUS 连接的外围设备：传感器、接收机、“油动套件”、舵机、VTX 和电调。一旦检测到 DIY 传感器，**DIY sensors** 项会自动出现。各设备的完整细节请参阅其自身的说明书；本页仅介绍它们的共通之处。

!!! note
    这与选择某个*模型*使用哪个射频模块（内置或外置）发射无关 —— 那是逐模型设置，详见
    [射频系统](../model-setup/rf-system.md)。

设备配置是可扩展的：用户和 FrSky 都可以通过 Lua 在此添加页面。

## 重新分配传感器 ID

Ethos 的设备配置界面可直接修改设备的 S.Port **Physical ID（物理 ID）** 和 **Application ID（应用 ID）**。如果你有多个功能相同的设备，请**逐个**连接：先在
[遥测 → 搜索新传感器](../model-setup/telemetry.md) 中发现某个设备，在此处的设备配置中修改其 Physical ID 和 Application ID，然后返回并以新的 ID 重新搜索该传感器。

## 接收机示例

![模块选择](../assets/system-devices-module-choice.png)

FrSky 增稳接收机在安装了对应的配置 Lua 脚本后（从 Ethos Suite 的 Lua 库一键安装）即可在此进行配置。根据接收机的代次，有两种配置途径：

- **Stabilizer config** —— 适用于具备“高级增稳”功能（增益控制位于通道 13）的较新接收机。可使用两个相互独立的增稳组：第 1 组对应通道 1–6，第 2 组对应通道 7–11 —— 如果不使用 7–11 号引脚进行增稳，请关闭第 2 组。内置六轴校准，新接收机必须执行一次，且在任何 v3.0.x 固件升级之后（进行恢复出厂设置后）需再次执行。在每个组的校准中，旧的“自检”步骤已被机身水平、通道中位与通道行程端点的独立校准所取代，且每个通道均可单独启用/禁用。配置（不包括校准数据）可保存到 PC 并从 PC 恢复。
- **SxR** —— 适用于较旧的接收机，包括早期型号以及 Archer/Archer Pro，还包括诸如 SR10 Pro 这类（尽管名称中带有“SRx”）增益位于通道 9 而非通道 13 的接收机。

  ![当前设备](../assets/system-devices-current.png)

!!! warning "升级到接收机固件 v3.0.x 之后"
    请先执行恢复出厂设置（位于射频设置中的接收机 Options 下），然后重新对频并完整重新配置 —— 尤其是增稳（Stab）功能与六轴校准。这是 v3.0.x 新增的失控保护数据保存功能所要求的；之后请仔细检查失控保护功能。

FrSky 北美发布了详细的增稳接收机设置指南，FrSky 队员飞手 Juan Sanchez Garcia 也制作了内容相同的演示视频。

## 通过发射机的 S.Port 接口进行配置

S.Port 与 FBUS 设备也可以直接通过发射机顶部的 S.Port 接口进行配置，无需经由已对频的接收机。

1. 将设备插入发射机的 S.Port 接口（白/黄线朝向有缺口的一侧）。
2. 进入 **System → Device config**，滚动到该设备（例如 FAS40 ADV 电流传感器），按 `ENT`。
3. 在配置页面中，将 **Module** 设为 **S.Port connector**。
4. 进行所需修改 —— Physical ID 与 Application ID 必须各自唯一 —— 然后向下滚动并点击 **Save to flash**。

这既适用于 FBUS 设备（另见 [操作指南：配置 FBUS 系统](../how-to/fbus-setup.md)），也适用于普通 S.Port 设备（如空速/升降速度计）。
