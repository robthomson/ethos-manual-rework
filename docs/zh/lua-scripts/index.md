---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua 脚本

Lua 脚本可让你构建自定义的[显示小组件](../displays/custom-widgets.md)，
以显示 Ethos 原生不支持的信息；也可（按模型）创建自定义
[信号源与任务](../model-setup/lua-scripts.md)——这是一项计划持续扩展的基础功能，
未来将支持专门的自定义功能以及飞控集成。

Lua 本身是一种轻量级、可嵌入的通用脚本语言（应用范围从游戏到 Web 应用）；
Ethos 嵌入 Lua 正是为了实现这类遥控器端的自定义。

!!! warning
    Lua 脚本会增加遥控器的启动时间。编写良好的脚本所带来的延迟应当难以察觉，
    而编写不佳的脚本几乎可能让启动无限期延迟。

- [Lua 解释器](lua-interpreter.md) —— Ethos 内嵌的 Lua 版本及库。
- [Ethos Lua 文档](ethos-lua-documentation.md) —— 完整 API 参考的所在位置。
- [示例脚本位置](example-script-locations.md) —— 在何处查找并下载可用的示例。
- [配置限制](configuration-limits.md) —— 位图与脚本的内存预算。
- [基本小组件布局](basic-widget-layout.md) —— 自定义小组件脚本所需的代码结构。
