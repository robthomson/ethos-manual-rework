---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua 脚本（模型）

![Lua 配置](../assets/model-lua-config.png)

只有在 SD card/eMMC 的 `scripts/` 目录下安装了 Lua **source**（信号源）或 **task**（任务）脚本后，此菜单才会出现（参见[文件管理器](../system-setup/file-manager.md#top-level-folders)）——该菜单用于**按模型**激活和配置这些脚本，而不是用于安装它们。安装完成后，source 或 task 对所有模型全局可用；本页面则是每个模型选择启用并设置各自配置的地方。示例 source 与 task 脚本发布在 Ethos-Feedback-Community 网站上（`/lua/examples/task`、`/lua/examples/source`）。

## Lua 任务

每个已安装的 task 都会列出，并带有针对当前模型的启用开关。启用后会显示其配置表单（如果有）——task 脚本自行提供读/写函数，因此每个模型都可以保存自己的设置。例如，某个 task 可能提供一个可配置的数值范围，该范围可按模型独立设定。

## Lua 信号源

source 采用相同的模式：按模型启用，然后通过 source 脚本提供的表单进行配置。以这种方式注册的 source 可在 Ethos 中的任何其他位置作为普通[信号源](../getting-started/user-interface-and-navigation.md#choosing-a-source)使用，与内置信号源完全相同。

## 给脚本作者的说明

source 与 task 通过 Lua 的 `system.registerSource()` 和 `system.registerTask()` 注册——请参阅《Ethos Lua Reference Guide》，以及本手册中的 [Lua 脚本](../lua-scripts/index.md)一章了解通用脚本运行环境（小组件是一种独立但相关的机制——参见[自定义小组件](../displays/custom-widgets.md)）。
