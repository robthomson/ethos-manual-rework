---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Ethos Suite

Ethos Suite 是配套的 Windows/Mac 应用程序，用于通过 USB 连接管理运行 Ethos 的遥控器。

!!! note "截图待补充"
    Ethos Suite 是独立的 PC 应用程序，而非遥控器本身，因此本节不使用手册其余部分所采用的模拟器截图 —— 参见 [截图流程](../contributing/screenshot-pipeline.md)。

连接完成后，Ethos Suite 可以：

1. 读取遥控器的型号、ID 以及已安装的各项版本 —— 固件、引导程序、内置 RF 模块、闪存文件以及 SD card/eMMC 文件。
2. 在引导程序模式与运行 Ethos 之间切换遥控器状态，并可切换回来。
3. 将已安装版本与最新版本进行比较并自动更新 —— 仅更新过期组件、无论状态全部更新，或逐个单独更新组件。
4. 通过 **Model Manager** 将模型备份到磁盘，或恢复此前的备份（由于模型文件在不同固件版本之间不向后兼容，此功能十分必要）。
5. 通过 **Download center** 从 FrSky 下载站点获取任意固件，并将遥控器作为中转设备直接刷写模块、传感器、舵机或接收机。
6. 将图像和音频文件转换为 Ethos 的原生格式。
7. 提供 **Lua 开发工具** —— API 文档、演示脚本以及调试终端。
8. 在 DFU 模式下（断电连接）刷写遥控器的引导程序，无论遥控器自身固件是否仍能运行。
9. 当 NAND 无法读取或设置无法保存时，通过 **Repair Tool** 修复 X18/S、TW Lite、XE 以及 X20 Pro/R/RS 遥控器的内部存储。
10. 安全弹出遥控器的 USB 驱动器。
11. 在启动时提示 Suite 自身有可用更新（在退出时安装）。

## 连接模式

除了各项工具之外，Suite 在三种不同的遥控器连接状态下工作：

- **遥控器处于引导程序模式** —— **Radio** 选项卡用于检查/更新固件以及闪存/SD card/eMMC 文件；**Model Manager** 用于备份或恢复遥控器。
- **遥控器处于 Ethos 模式** —— Suite 将遥控器作为中转设备（通过 **FRSK Flasher**/Download center 工具）直接刷写内置模块，或任何已连接的传感器/舵机/接收机。
- **遥控器处于 DFU 模式** —— 断电连接，由 **DFU Flasher** 用于刷写引导程序本身，例如当固件损坏导致遥控器无法正常开机时。

首次将现有遥控器迁移至 Ethos Suite，请参见 [迁移](migration.md)；关于 Suite 界面本身，请参见 [操作](operation.md)。
