---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 附加显示屏

![屏幕配置选项](../assets/display-screen-config-options.png)

默认模型仅包含一个屏幕（一张模型图片加三个计时器小组件），但最多支持 **八** 个屏幕。点击 "Screen1" 旁边的 **+** 即可添加新屏幕：

- 可从 **15** 种布局中选择，其中包括两种专用的主页屏幕布局和一种全屏布局，单个屏幕最多可容纳 9 个小组件 —— 配置方式与第一个屏幕完全相同。
- 屏幕可在其各自的编辑对话框中重新排序或删除（点击 Screen1、Screen2 等）。

## 实例演示

![主视图](../assets/display-main-view.png)

一种典型布局：左侧为模型图片（在 [模型编辑 → 图片](../model-setup/model-edit.md) 中配置），右侧自上而下依次排列接收机电池电压、RSSI 以及一个 "Throttle ACTIVE" 状态小组件（该小组件是由社区开发的 Lua 小组件，来自 rcgroups 论坛的 *FrSky - ETHOS Lua Script Programming* 主题帖）。点击任一小组件即可打开其配置界面，或跳转至主"配置显示屏"功能。

## 屏幕级选项

除各个小组件之外，每个屏幕还有自身的设置项 —— 布局网格尺寸、背景，以及哪些屏幕包含在 `PAGE` 循环切换中。

有关小组件本身，请参阅 [显示屏](index.md)；有关在内置小组件之外添加 Lua 脚本小组件，请参阅 [自定义小组件](custom-widgets.md)。
