---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 显示屏

![显示屏主页](../assets/display-home.png)

主页屏幕由一个或多个**显示屏幕**组成，每个屏幕都由您自行放置并配置的**小组件**构建而成。按下 `DISP` 可打开当前屏幕的显示编辑器。

最多可使用**八个**屏幕，每个屏幕从**十三种**布局中选择一种作为起点（最多可容纳**九个**小组件单元格）。小组件可以显示遥测数据，也可以显示其他十七个信息类别中的任意内容——模型/遥控器状态、计时器、通道等等。已配置的屏幕可通过触摸滑动或 `PAGE` 上/下键切换；除全屏布局外，顶部和底部状态栏在每个屏幕上都保持可见。

## 添加小组件

![小组件类型](../assets/display-widget-types.png)

每个屏幕都是一个网格；点击空白单元格即可打开小组件选择器。小组件的范围涵盖从简单的文本和数值读数到仪表、图表以及完整的遥测日志。放置完成后，再次点击小组件将打开同一个选项菜单，可用于调整大小、移动或删除该小组件：

![小组件配置选项](../assets/display-widget-config-options.png)

选择小组件自身的设置项会打开该小组件专用的配置表单。**信号源**字段——即小组件所显示的数值——使用与 Ethos 中其他位置相同的[信号源选择器](../getting-started/user-interface-and-navigation.md#choosing-a-source)：

![更改小组件信号源](../assets/display-change-source.png)

## 小组件类型 {: #widget-types }

**Value（数值）**——以文本形式显示单个数值或遥测读数：

![数值小组件配置](../assets/display-widget-value-config.png)

大多数信号源还支持缩减为实时**最小值**或**最大值**——选择信号源后，长按该信号源并选择 Min 或 Max——这对于查看整个飞行过程中最差的 RSSI 之类的数据非常有用：

![数值小组件最小值](../assets/display-widget-value-min.png)
![数值小组件最小 RSSI](../assets/display-widget-value-min-rssi.png)

放置完成后，它会在屏幕上呈现为一个普通读数：

![遥测数值小组件](../assets/display-widget-value-telemetry.png)

**Bitmap（位图）**——显示一张静态图片（例如模型照片），或根据某个信号源的数值切换显示一组图片（例如随电压变化的电池图标）：

![位图小组件配置](../assets/display-widget-bitmap-config.png)
![位图小组件类型](../assets/display-widget-bitmap-type.png)

**LiPo（锂电池）**——专用的电池电量表，从 FLVSS 之类的传感器读取数据：电池组总电压、电芯数量以及每个电芯的单独电压。低于所配置的**低电压**阈值时，显示将变为红色——在下面的示例中，3.3V 阈值由最低电芯电压触发：

![LiPo 小组件配置](../assets/display-widget-lipo-config.png)
![LiPo 小组件](../assets/display-widget-lipo.png)

**Channels（通道）**——以条形图形式显示最多 8 个输出通道，可横向或纵向排列：

![通道小组件配置](../assets/display-widget-channels-config.png)
![通道小组件](../assets/display-widget-channels.png)

**Line Chart（折线图）**——绘制某个信号源随时间变化的数值，在执行飞行复位时清零：

![折线图小组件配置](../assets/display-widget-line-chart-config.png)
![折线图小组件](../assets/display-widget-line-chart.png)

- **Source（信号源）**——要绘制的对象。
- **Pause condition（暂停条件）**——用于暂停/恢复记录的信号源（若没有空闲信号源可用于此功能，也可直接点击正在运行的小组件）。
- **Log period（记录周期）**——采样间隔；500ms 大约可覆盖 6 分钟后开始滚动，1s 约为 12 分钟。
- **Inverted（反向）**——将图表垂直翻转。
- **Auto range（自动量程）**——自动缩放垂直轴以适配数据；关闭后则使用固定的**Min**/**Max** 数值（例如固定的 −100%…+100% 范围）。

点击正在运行的图表会弹出 **Pause/resume（暂停/恢复）**、**Reset（复位）**（清空并重新开始）、**Configure widget（配置小组件）**，或跳转到 **Configure screens（配置显示屏）**：

![折线图选项](../assets/display-widget-line-chart-options.png)

**Text（文本）**——呈现某个 Markdown 文本文件的内容（从 `documents/user/` 读取——参见[文件管理器](../system-setup/file-manager.md#top-level-folders)）：

![文本小组件配置](../assets/display-widget-text-config.png)
![文本小组件](../assets/display-widget-text.png)

**Timer Log（计时器日志）**——可滚动查看所选计时器的历史数值日志，每次该计时器被复位时写入一条记录（便于跟踪一次活动中飞行电池的使用情况）；**Reverse（反序）**会将最新记录置于顶部：

![计时器日志小组件配置](../assets/display-widget-timer-logs-config.png)
![计时器日志小组件](../assets/display-widget-timer-log.png)

长按某条记录（或该小组件）可执行 **Clear logs（清除日志）**、编辑/复位对应的计时器，或跳转到小组件/屏幕配置：

![计时器日志记录菜单](../assets/display-widget-timer-log-menu.png)

**GPS Map（GPS 地图）**——为配备 GPS 传感器的模型绘制实时 GPS 位置轨迹（有关此小组件的更多细节，可参阅 rcgroups 上的 *FrSky - ETHOS Lua Script Programming* 主题第 #8854 楼）：

![GPS 地图小组件配置](../assets/display-widget-gps-map-config.png)

## 屏幕级选项

除了各个独立的小组件之外，每个屏幕还有自己的设置项——布局网格尺寸、背景，以及哪些屏幕纳入 `PAGE` 循环切换：

![屏幕配置选项](../assets/display-screen-config-options.png)

一个配置完善的主页屏幕会将多个小组件组合成一个可一目了然的布局：

![主视图](../assets/display-main-view.png)

如需在默认屏幕之外添加更多屏幕，请参见[附加显示屏](additional-displays.md)；如需超出内置范围的 Lua 脚本小组件，请参见[自定义小组件](custom-widgets.md)。
