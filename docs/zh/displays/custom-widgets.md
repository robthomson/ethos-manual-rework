---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 自定义小组件

除了[内置小组件类型](index.md)之外，Lua 脚本还可以实现完全自定义的小组件——通常是一个 `main.lua` 文件，放在以其功能命名的子文件夹中。

## 安装小组件

将小组件的子文件夹复制到 SD card/eMMC 上的 `scripts/` 目录中（参见[文件管理器](../system-setup/file-manager.md#top-level-folders)）。它会在下次开机时自动注册，此后便会与内置类型一同出现在[配置显示屏](additional-displays.md)的 **Change widget** 类别选择器中——配置方式完全相同。

## 编写小组件

有关小组件脚本需要实现的代码结构，请参见 [Lua 脚本 → 小组件基本结构](../lua-scripts/basic-widget-layout.md)。
