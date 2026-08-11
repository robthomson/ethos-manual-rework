---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 信息

![系统信息](../assets/system-info.png)

系统固件详情、摇杆类型、内部/外部射频模块信息、已对频接收机信息、遥控器运行时间、错误日志以及恢复出厂设置。

## 遥控器信息

- **Serial number** —— 遥控器序列号。
- **Firmware** —— Ethos 版本与遥控器型号（例如 X20）。
- **Firmware Version** —— 固件版本类型，例如 FCC、LBT 或 Flex。
- **Date** —— 固件编译日期/时间。
- **RAM available** —— 系统可用内存，可用于发现异常的 Lua 脚本；该项同时作为系统[信号源](../getting-started/user-interface-and-navigation.md#choosing-a-source)提供，因此可在小组件中显示。
- **Sticks** —— 已安装摇杆的霍尔传感器版本（模拟摇杆则显示 "ADC"）。
- **Internal Module** —— 内部射频模块的硬件与固件版本。
- **Receiver** —— 当前已对频接收机的详细信息，显示在内部模块之后。若冗余接收机与主接收机共用同一插槽，两者会在显示中交替出现（例如 Archer SR10 Pro 与其冗余的 R9MM-OTA 一同显示在 "Receiver1" 下）。
- **External Module** —— 已安装且使用 ACCESS 协议的 FrSky 外部射频模块的硬件/固件信息。Multi-protocol 模块不会在此显示。

![X20 Pro 信息](../assets/system-info-x20pro.png)

## 遥控器运行时间

![遥控器运行时间](../assets/system-info-radio-runtime.png)

记录遥控器的累计使用时间；**Reset** 可将其归零。

## 错误

![错误](../assets/system-info-errors.png)

主视图顶栏出现红色三角形，表示 Ethos 已记录错误，详情可在此页面查看。可能的原因包括：

- **Lua 脚本错误** —— 正在运行的 Lua 脚本出现问题。
- **RAM 备份错误** —— 模型过大，超出模型备份 RAM 的容量。Ethos 已将其从 4K 扩展至 32K，因此现在很少会触发；但一旦发生，则属于严重错误：当触发[紧急模式](../getting-started/emergency-mode.md)时，模型将从 SD card 而非备份 RAM 载入，速度较慢。
- **运行 nightly 固件版本** —— 提醒您 nightly 版本并不适合用于飞行。

**Reset** 可清除已记录的错误 —— 在 Lua 调试过程中非常实用。

## 恢复出厂设置

![恢复出厂设置](../assets/system-info-factory-reset.png)

完全在设备上将遥控器恢复至出厂设置 —— 无需连接电脑。

![恢复出厂设置确认](../assets/system-info-factory-reset-confirm.png)

!!! danger
    确认后将擦除**所有**模型、日志、截图、文档、脚本、位图以及遥控器设置。擦除过程中会显示进度条，完成后所有驱动器将被卸载，遥控器随即重启。

X20 Pro/R/RS 的 Info 页面显示的是该系列遥控器对应的相关信息。
