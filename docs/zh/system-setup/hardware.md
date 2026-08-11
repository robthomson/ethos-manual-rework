---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 硬件

![硬件检测](../assets/system-hardware-check-x20s.png)

用于测试和校准遥控器的物理控制部件、定义开关类型，以及设置主页按键映射。

## 硬件检测 {: #hardware-check }

逐一操作每个物理输入，以确认每个输入都能正确识别。

![X20 Pro 硬件检测](../assets/system-hardware-check-x20pro.png)
![X18S 硬件检测](../assets/system-hardware-check-x18s.png)

- **X20 Pro/R/RS** — 还会检测机身背面肩部的两个自锁按键开关 **K** 和 **L**，以及附加微调 **T5**/**T6**。
- **X18** — 还会检测附加微调 **T5**/**T6**。

## 模拟量校准 {: #analogs-calibration }

![模拟量校准](../assets/system-hardware-analogs-calibration.png)

让遥控器准确识别各摇杆、电位器和滑块的中位与行程极限位置。首次开机时会自动运行；更换摇杆、电位器或滑块后应重新执行。

## 陀螺仪校准

![陀螺仪校准](../assets/system-hardware-gyro-calibration.png)

校准内置陀螺仪，使基于倾斜的输入能正确响应遥控器的倾斜动作 —— "水平"位置即为你平时握持遥控器的姿态。同样会在首次开机时自动运行。

## 模拟量滤波

针对摇杆的 ADC 滤波开关，默认开启 —— 可减少摇杆中位附近的抖动。此处为**全局**设置；在 [模型编辑](../model-setup/model-edit.md) 中还有**按模型**的模拟量滤波覆盖设置。

## 电位器/滑块设置 {: #potssliders-settings }

可重命名电位器和滑块。**X20 Pro/R/RS** 还额外支持两个扩展电位器 **Ext1**/**Ext2**，通常用于三轴摇杆。

![ADC 值，电位器](../assets/system-hardware-pots-x20s.png)
![ADC 值，电位器（X20 Pro）](../assets/system-hardware-pots-x20pro.png)

## 开关设置 {: #switches-settings }

![开关](../assets/system-hardware-switches.png)

- **开关中位检测延时** — 防止三位开关快速由上→下（或下→上）拨动时瞬间被识别为中位；只有开关确实停在中位时才应识别为中位。默认值为 0ms，该值适配 FrSky 增稳接收机在 CH12 上的"自检"检测。
- **开关类型** — SA–SJ 均可定义为 **None**、**Momentary**、**2 POS** 或 **3 POS**，从而可在物理开关之间互换功能（例如让弹回开关 SH 承担通常由二位开关 SF 承担的角色）—— 但受遥控器实际接线的限制（三位角色一般无法分配给未按三位方式接线的硬件）。

  ![开关选项](../assets/system-hardware-switches-options.png)
  ![附加开关](../assets/system-hardware-switches-2.png)

- **重命名** — 开关可从 SA–SJ 重命名为自定义名称；名称对所有模型全局生效。
- **X20 Pro** — 在机身背面肩部增加按键开关 **K**/**L**，若已接线还包括 **M**/**N** 位（通常用于摇杆端部开关）。

## 主页按键映射

重新指定 `SYS`、`MDL` 和 `DISP`（旧款遥控器上为 `TELE`）主页按键的跳转目标。

- **`DISP`** — 短按和长按均可重新指定为任意模型页面、系统页面、配置显示屏、主页或飞行数据记录。为与 X10 系列保持一致，`DISP` 长按通常设置为配置显示屏。
- **`SYS`/`MDL`** — 仅长按可重新指定（可选目标与上述相同）；短按始终分别打开系统或模型部分。

## 特定机型的硬件选项 {: #radio-specific-hardware-options }

- **启用震动摇杆升级件**（X20 Pro、X20R）— X20 Pro AW 和 X20RS 出厂搭载带震动马达（stick-shaker）的 MC20R 摇杆；如果为 X20 Pro 或 X20R 加装了 MC20R 摇杆，需在此处启用（震动模式本身的配置见 [特殊功能](../model-setup/special-functions.md)）。

  ![震动（X20 Pro）](../assets/system-hardware-haptic-x20pro.png)
  ![震动（X20 Pro AW）](../assets/system-hardware-haptic-x20proaw.png)

- **编码器选项**（X20 Pro AW、X20R/RS）— 这些遥控器配备灵敏度更高的旋转编码器；启用**半步进**可降低其灵敏度。

  ![编码器选项（X20 Pro AW）](../assets/system-hardware-x20proaw-encoder-option.png)

## ADC 数值查看 {: #adc-value-inspector }

显示 CPU 为每个模拟输入读取的原始模数转换值：

![ADC 检测（X20S）](../assets/system-hardware-adc-check-x20s.png)
![ADC 检测（X20 Pro）](../assets/system-hardware-adc-check-x20pro.png)

**X20S**：1 左摇杆水平，2 左摇杆垂直，3 右摇杆垂直，4 右摇杆水平，5 Pot 1，6 Pot 2，7 中间滑块，8 左滑块，9 右滑块。

**X20 Pro**：同上，但在滑块之前插入了两个额外的外部电位器通道（7 Ext1，8 Ext2 —— 例如安装在摇杆上的电位器），因此滑块顺延为 9 中间滑块，10 左滑块，11 右滑块。
