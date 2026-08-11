---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 基本小组件结构

自定义 Lua 小组件（安装方法参见[自定义小组件](../displays/custom-widgets.md)）由一小组具名字段/处理函数构成：

- **`key`** *(字符串)* — 小组件的唯一标识符。
- **`name`** *(字符串或函数)* — 小组件的显示名称。可以是普通字符串，也可以是一个不接受参数并返回名称的函数 —— 后者适用于需要随语言环境变化的名称。
- **`create`** *(函数)* — 在小组件创建时调用一次，不接受参数。返回一个**小组件表**，该表随后会传递给下面所有其他处理函数 —— 请在此处初始化你的状态数据并将其存入该表。
- **`configure`** *(函数)* — 当用户打开小组件的配置界面时调用，其唯一参数是 `create()` 返回的小组件表，无返回值。请在此处构建配置表单，并用它来更新小组件表中的数值。
- **`wakeup`** *(函数)* — 每个循环周期调用一次（大约每 50ms 一次），参数为小组件表，无返回值。在此处检查是否有内容发生变化；若有，则调用 `invalidateWindow()` 以通过 `paint()` 触发重绘。此处理函数必须保持高效 —— 理想情况下在绝大多数调用中什么都不做。
- **`event`** *(函数)* — 当小组件收到事件时调用；Ethos 通过该处理函数将各类事件路由给小组件。
- **`paint`** *(函数)* — 绘制小组件，参数为小组件表，无返回值。每当 `lcd.invalidate()` 被触发时自动调用。它可以相对较慢，但仍应仅在内容发生变化时才真正执行重绘。
- **`read`** *(函数，可选)* — 读取小组件的持久化存储数据。
- **`write`** *(函数，可选)* — 写入小组件的持久化存储数据。
- **`init`** *(函数)* — 向 Ethos 注册小组件及其回调函数。通常是脚本中的最后一项内容：

```lua
local function init()
  system.registerWidget({
    key = "unique",
    name = name,
    create = create,
    configure = configure,
    wakeup = wakeup,
    paint = paint,
    read = read,
    write = write,
  })
end

return { init = init }
```

`key` 在所有已安装的小组件中必须唯一；其他字段则按上述说明与小组件的生命周期相关联。

脚本存放在 SD card/eMMC 的 `scripts/` 目录下，最好按每个小组件分别建立文件夹进行组织（参见[文件管理器](../system-setup/file-manager.md#top-level-folders)和[脚本存放位置示例](example-script-locations.md)）。更多实例可参阅 rcgroups 论坛上的 *FrSky ETHOS Lua Script Programming* 主题帖。
