---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 教练功能

![教练功能](../assets/model-trainer.png)

默认关闭。可将本遥控器设置为 **Master**（教练机，即教练员的遥控器，可接收学员端最多 16 路控制量）或 **Slave**（学员机，即学员的遥控器，向教练员发送可配置数量的通道）。

## Master 模式

![Master 模式](../assets/model-trainer-master.png)
![教练功能选项](../assets/model-trainer-options.png)

### 连接方式

![连接方式选项](../assets/model-trainer-link-mode-options.png)

- **教练线** — 使用一根 3.5mm 单声道音频线连接两台遥控器。
- **Bluetooth** —

  ![Bluetooth 连接](../assets/model-trainer-link-mode-bt.png)

  - **模式** — 普通速率或高速率；若两台遥控器均支持，使用高速率可获得更低延迟。

    ![Bluetooth 模式](../assets/model-trainer-link-mode-bt-mode.png)

  - **本机名称** — 向其他设备显示的 BT 名称（默认为 `FrSkyBT`，可编辑）。
  - **本机地址** — 本遥控器的 Bluetooth 地址。
  - **对端地址** — 连接建立后，配对遥控器的地址。
  - **搜索设备**（仅 Master 模式）— 扫描附近的设备：

    ![正在搜索](../assets/model-trainer-link-mode-bt-search.png)
    ![等待中](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![选择设备](../assets/model-trainer-link-mode-bt-select-device.png)
    ![已连接](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **连接上一个设备** / **复位模块** — 重新连接上一次配对的设备，或彻底清除 Bluetooth 模块的配置。

- **SBUS 外置模块** — 在外置模块仓的 PXX-IN 引脚上接入 SBUS 信号，可安装一台带 SBUS 输出的 FrSky 接收机（例如 Archer RS）作为无线链路的接收端 —— 这样**任意** FrSky 遥控器都可以作为学员端（buddy box），只需与该接收机对频即可。
- **CPPM 外置模块** — 原理相同，但通过 CPPM 输入接入，适用于仅有 CPPM 输出的旧款接收机。

### 激活条件

![激活条件](../assets/model-trainer-active-condition.png)

可选择开关/按键、功能开关、逻辑开关、微调位置或飞行模式，当其处于激活状态时将控制权交给学员。

### 教练通道

![激活条件编辑](../assets/model-trainer-active-condition-edit.png)

在激活条件成立时，最多可有 16 个通道从学员机传输至教练机。点击某个通道即可单独配置：

- **激活条件** — 针对单个通道的覆盖设置，例如在一段飞行中仅禁用学员的升降舵输入。
- **模式** — **OFF**（该通道不参与教练功能）、**Add**（教练与学员的信号相加，两人可同时操作该控制量）或 **Replace**（常规模式 —— 激活时学员完全控制该通道）。
- **百分比** — 缩放学员的输入量，通常为 100%。
- **目标** — 学员的该通道映射到哪个功能。

关于教练员通过开关瞬间收回控制权的完整示例，请参阅 [操作指南：瞬时收回控制权](../how-to/instant-takeback.md)；若需将学员的摇杆动作从监视教练员自身摇杆的逻辑开关中排除，请参阅 [忽略教练输入](../getting-started/user-interface-and-navigation.md#choosing-a-source)。

## Slave 模式

![Slave 模式](../assets/model-trainer-slave-mode.png)

- **连接方式** — 与 Master 模式相同，可选择教练线、Bluetooth 或 SBUS/CPPM 外置模块（Bluetooth 的 **模式**/**本机名称**/**本机地址**/**对端地址** 字段也相同）。

  ![Slave 连接方式](../assets/model-trainer-slave-link-mode.png)

- **通道范围** — 本遥控器的哪一段通道范围将发送给教练机。

  ![Slave 通道](../assets/model-trainer-slave-channels.png)
  ![Slave 通道编辑](../assets/model-trainer-slave-channel-edit.png)
