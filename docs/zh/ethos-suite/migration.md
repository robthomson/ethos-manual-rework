---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 迁移

首次将遥控器从旧版独立 PC 升级工具迁移到 Ethos Suite。

1. **确认 Ethos 版本 ≥ 1.1.4** —— 这是能够直接通过[文件管理器](../system-setup/file-manager.md)刷写新版 Suite 兼容引导程序（FRSK 格式）的最低版本。如有需要，请先手动升级到 1.1.4。
2. **备份 SD card/eMMC** —— 将其全部内容复制到 PC 上的一个文件夹中。
3. **下载最新的引导程序**，来源为 [ETHOS-Feedback-Community 发布页](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)，下载后解压。每个发布版本都会提供一个 `components.json` 文件，其中列出了各个组件的当前版本 —— 关于如何读取该文件，请参阅[操作指南：查找最新的引导程序](../how-to/find-latest-bootloader.md)。
4. 在该文件的 `targets` 条目中找到对应的遥控器，以确定应使用的引导程序确切版本，并在该发布版本的资源文件中找到匹配的文件。
5. 让遥控器进入[引导程序模式](../getting-started/usb-connection-modes.md#bootloader-mode)（按住 `ENT`，然后开机）并通过 USB 连接。
6. 将引导程序文件复制到 SD card/eMMC（通常放入 `Firmware/` 目录），然后弹出驱动器并断开连接。
7. 正常启动遥控器，进入 **系统 → 文件管理器**，点击刚刚复制的 `bootloader.frsk` 文件，然后选择 **Flash bootloader**（刷写引导程序）。
8. 下载并安装 Ethos Suite —— 后续关于更新固件/文件以及 Suite 其他功能的内容，请参阅[操作](operation.md)。
9. 如果 Ethos Suite 未自动完成，可能需要将 SD card/eMMC 上的 `bitmaps/user` 文件夹重命名为 `bitmaps/models`（用户模型图片存放于此）。
