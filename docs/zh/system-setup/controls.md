---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 控制

![摇杆](../assets/system-sticks.png)

在菜单中称为 **Sticks（摇杆）** —— 用于设置摇杆模式以及默认的通道分配顺序。

## 摇杆模式

- **Mode 1** —— 油门与副翼位于右摇杆，升降舵与方向舵位于左摇杆。
- **Mode 2** —— 油门与方向舵位于左摇杆，副翼与升降舵位于右摇杆。

摇杆默认按行业标准模式命名，也可以自行重命名。

## 通道顺序

定义当通过 [模型选择](../model-setup/model-select.md) 向导创建新模型时，四个摇杆输入分配到通道的顺序。默认为 **AETR**。当机型中同一舵面有多个时，它们会归组在一起，除非启用了 [前四通道固定](#first-four-channels-fixed) —— 例如 2 个副翼会变为 **AAETR**。

![接收机通道顺序](../assets/system-sticks-rx-order.png)

## 前四通道固定 {: #first-four-channels-fixed }

启用此项后，前四个通道永远不会被归组。若顺序为 **AETR**，机型有 2 个副翼、1 个升降舵、1 个电机、1 个方向舵和 2 个襟翼，向导将生成 **AETRAFF**（通道 1–4 严格保持 A-E-T-R，第二个副翼与两个襟翼追加在其后），而不是 **AAETRFF**。正是此设置使向导创建的模型适配 SRx 增稳接收机，因为这类接收机要求上述固定的通道布局。

![4 通道固定顺序](../assets/system-sticks-4ch-fixed.png)
