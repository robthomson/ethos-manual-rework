---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# X20 Pro / X20 Pro AW

![X20 Pro 硬件检查](../assets/system-hardware-check-x20pro.png)

与本手册所依据的 X20S 基准型号的差异 ——
以下内容适用于 **X20 Pro**，并且大多同样适用于 **X20 Pro AW**
以及 **X20R/RS** 系列。

- **存储** —— 默认配备 8GB 内置 eMMC，SD card 为选配 —— 参见
  [通用 → 存储位置](../system-setup/general.md#storage-location-x18-and-x20-prorrs)。
- **额外微调** —— 增加微调开关 **T5** 与 **T6** —— 参见
  [微调](../model-setup/trims.md#trim-settings)。
- **额外开关** —— 机身后肩部设有两个自锁式按钮开关 **K** 与 **L**，
  此外若已接线还可提供开关位 **M**/**N**（通常为摇杆顶端开关）—— 参见 [硬件 →
  开关](../system-setup/hardware.md#switches-settings)。
- **额外电位器** —— **Ext1**/**Ext2**，通常配合三轴摇杆使用
  —— 参见 [硬件 → 电位器/滑块](../system-setup/hardware.md#potssliders-settings)。
  这会使 [ADC 数值检视器](../system-setup/hardware.md#adc-value-inspector)
  的索引顺序发生变化：Ext1/Ext2 位于 Pot2 与滑块之间。
- **振动反馈** —— **X20 Pro AW** 与 **X20RS** 出厂即配备内置振动马达的 MC20R
  摇杆；**X20 Pro** 或 **X20R** 也可通过改装 MC20R 摇杆升级获得同样功能，
  并在 [硬件 → 启用振动摇杆升级](../system-setup/hardware.md#radio-specific-hardware-options)
  中开启。启用后，[选择振动马达](../model-setup/special-functions.md#actions)
  提供 Default、All motors、Left stick 或 Right stick 选项。
- **旋转编码器** —— X20 Pro AW 与 X20R/RS 使用灵敏度更高的
  编码器；可在 [硬件 → 编码器选项](../system-setup/hardware.md#radio-specific-hardware-options)
  中通过 **half steps**（半步）选项降低其灵敏度。
- **内置射频模块** —— X20 Pro/R/RS 采用 **TD-ISRM Pro**
  模块（支持 LoRa，除 ACCESS/ACCST D16 外还提供双向双频与 TD-Pro 模式），
  而非 X18/X20/X20S/X20HD 中的 TD-ISRM 模块 —— 参见 [射频系统](../model-setup/rf-system.md)。
