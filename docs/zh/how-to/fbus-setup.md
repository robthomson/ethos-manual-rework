---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 配置 FBUS 系统

[FBUS](../model-setup/telemetry.md#how-frsky-telemetry-works)（原名
F.Port2）将控制信号与遥测数据合并到一条线上，使多个 FBUS
设备可以共用一条菊花链连接，并支持完整的无线配置。本教程将两个 Xact 舵机接到[基础固定翼示例](../tutorials/basic-fixed-wing.md)的副翼通道（通道 1 和 5）上。

!!! note "截图待补充"
    本页尚无模拟器截图 — 参见[截图流程](../contributing/screenshot-pipeline.md)。

## 1. 下载最新固件

FBUS 要求接收机与设备均运行较新的固件 — 例如 Xact
舵机需要 v2.0.1 以上版本。请从
[FrSky 下载页面](https://www.frsky-rc.com/download/)获取相应的更新文件。

## 2. 刷写固件

将固件文件复制到 SD card/eMMC 的 `Firmware/` 目录下。在[文件管理器](../system-setup/file-manager.md)中，将舵机插入遥控器的 S.Port
接口（白/黄线朝向卡口一侧），选中固件文件，然后执行 **Flash External Device**（刷写外部设备）。

## 3 / 5. 配置 Physical ID

两个舵机的默认 Physical ID 均为十六进制 `0C`、Application ID 为十六进制 `6800` —
若不修改其中一个，它们会在共用总线上产生冲突。根据接收机类型有两种配置方式：

**通过发射机的 S.Port 接口**（适用于任何接收机）：

1. 插入舵机 1，进入 **Device Config → XAct**，将 **Module** 设为
   **S.Port connector**。保持 Physical ID `0C`/Application ID `6800` 及通道
   `CH1` 为默认值，然后执行 **Save to flash**。
2. 换插舵机 2，进入同一菜单。将 **Physical ID** 改为十六进制 `0D`，
   **Application ID** 改为十六进制 `6801`（可用槽位请参见 [Physical ID
   对照表](../model-setup/telemetry.md#how-frsky-telemetry-works)），将
   **Channel** 设为 `CH5`，然后 **Save to flash**。

**通过接收机直接配置**（例如 TD-R18 Tandem，两个舵机可同时接线 —
参见[第 4 步](#4-configure-the-receiver-for-fbus)）：

1. 仅连接舵机 1（例如接收机 Pin1），进入 **Device Config →
   XAct**，将 **Module** 设为 **Internal module**。确认默认值（`0C`/
   `6800`/`CH1`），执行 **Save to flash**。
2. 仅连接舵机 2（Pin5），进入同一菜单（Device Config 一次只能与一个舵机通信）—
   改为 `0D`/`6801`/`CH5`，执行 **Save to flash**。
   之后重新进入 Device Config，确认修改已生效。

## 4. 将接收机配置为 FBUS {: #4-configure-the-receiver-for-fbus }

**SR10 Pro**：[RF 系统](../model-setup/rf-system.md) → 接收机对应的按钮 →
**Options** → 将 **Telemetry Port** 设为 **FBUS**。Xact 舵机随后以菊花链方式接在该端口上；由于每个舵机只有一个接口，需要使用 F.Port2 多通道扩展器（FP2CH4/6/8）将其分出多路。

**TD-R18 Tandem**：RF 系统 → 接收机对应的按钮 → **Options** →
将各个引脚（例如 **Pin1**、**Pin5**）单独设为 **FBUS** —
可按需重新分配任意数量的引脚，从而完全无需扩展器；所有被指定为 FBUS 的引脚都输出完全相同的 FBUS 信号。

## 5. 检查 FBUS 对舵机的控制

将舵机 1 插入 Pin1，舵机 2 插入 Pin5（即固定翼示例中的副翼通道），上电后确认通道 1 和 5 分别驱动正确的舵机。

## 6. 检查 FBUS 遥测

在两个舵机均连接的情况下，删除[遥测](../model-setup/telemetry.md)中已有的
`SRV` 传感器并重新发现。每个舵机会上报 4 个传感器：电流、电压、温度和状态（正常时显示 `OK`）。

## 7. 后续修改配置

模型完全装配布线后，为通过 Device Config 重新配置而单独隔离某个舵机并不现实。替代做法是：进入遥测页面，找到目标舵机的某个传感器（例如
`SRV1 curr`），选择
**Configure** — 这会直接打开该舵机的配置界面。
任何修改后都要执行 **Save to flash**。

!!! warning
    切勿在该界面上误改 Physical ID 或 Application ID —
    正是它们保证了每个舵机在共用总线上可被独立寻址。
