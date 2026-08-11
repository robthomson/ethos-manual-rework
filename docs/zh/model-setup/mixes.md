---
translated_from: 4cf1808aa5b70d3f39900c1a7aff575ca60ee89e
---

# 混控设置

![混控图标](../assets/model-icon-mixes.png)

混控是 Ethos 中模型编程的核心——各类输入（摇杆、开关、传感器，以及任何[信号源](../getting-started/user-interface-and-navigation.md#choosing-a-source)可以获取到的量）在此被路由、整形，并合成到输出通道上。每个模型最多可定义 120 条混控。

![混控列表](../assets/model-mixes.png)

如果模型是通过 **模型选择** 向导创建的，其基础混控（副翼、升降舵、油门、方向舵，以及该机型所需的其他项）已在此自动生成。选中某条混控并按 `ENT` 会打开一个上下文菜单，可用于编辑该混控、新增混控、切换到[按通道视图](#per-channel-view)、调整顺序、复制或删除。未激活的混控显示为灰色，删除操作始终会先要求确认。

## 混控的构成 {: #anatomy-of-a-mix }

无论来自哪个类别，每条混控都具有相同的一组字段。**副翼** 混控是一个典型示例——升降舵和方向舵混控的布局与之完全相同。

![副翼混控](../assets/model-mixes-ail-edit.png)

![副翼混控编辑界面](../assets/model-mixes-ail.png)

**名称** — 默认为混控类型，可编辑。

**条件** — 默认为 *Always*（始终）。可限定为某个开关位置、功能开关、逻辑开关、飞行模式、系统事件（油门切断/油门保持）或某个微调位置，此时该混控仅在条件成立时生效。

**飞行模式** — 如果已定义飞行模式，还可将该混控限定为其中的一个或多个模式。

**曲线** — 默认提供 **Expo** 曲线（0 = 线性；正值使中位附近的响应变柔和，负值使其变灵敏）：

![Expo 曲线](../assets/model-mixes-ail-expo.png)

也可以选用先前在[曲线](curves.md)中定义的任何曲线。一条混控上最多可叠加 6 条曲线，每条曲线可有各自的条件——若同时有多个条件成立，则列表中位置靠前的曲线优先。曲线在比率**之前**被应用。

**比率** — 一行或多行权重，每行可选择由开关、功能开关、逻辑开关、微调位置或飞行模式来触发。第一行为默认行，在其他各行的条件均不满足时生效：

![副翼比率](../assets/model-mixes-ail-weight.png)

比率也可以不使用固定百分比，而是由某个[信号源](../getting-started/user-interface-and-navigation.md#choosing-a-source)驱动——例如使用电位器，以便在飞行中调整比率：

![由信号源驱动的比率](../assets/model-mixes-ail-diff.png)

**差动**（-100 至 100，默认 0）— 使一个方向的行程大于另一个方向。对副翼而言，这就是经典的上偏量大于下偏量的做法，用于减小反向偏航。只有当该混控具有多个输出通道时才会显示；差动功能特别需要 V 型尾翼或双副翼类型的输出配置才有意义。

**通道数量 / 输出** — 该混控驱动多少个输出通道，以及它们对应到哪些物理输出：

![通道数量](../assets/model-mixes-ail-ch-count.png)

在界面其他位置（例如[输出](outputs.md)中）长按某个输出通道上的 `ENT`，会直接跳回本页面。

## 油门混控

油门混控相当于副翼/升降舵/方向舵混控，再加上针对发动机的安全选项。

![油门混控](../assets/model-mixes-thr.png)

**输入** — 油门信号源，通常为油门摇杆，但也可更换为电位器、滑块、开关、微调、通道、陀螺仪轴、教练通道、计时器或任何其他信号源。

**怠速微调** — 用于内燃发动机，允许用专门的微调调整怠速转速，而不影响满油门位置。启用怠速微调后，当摇杆处于低怠速位置时，油门通道位于 -75%，此时油门微调可在 -100% 至 -50% 之间调整怠速：

![怠速微调菜单](../assets/model-mixes-thr-trim-menu.png)

![低位时的怠速微调](../assets/model-mixes-thr-trim-low-position.png)

**油门切断** — 一种强制安全联锁：只有当油门摇杆经过怠速位置后通道才会生效，因此误拨开关时无法从高油门位置直接启动电机：

![油门切断](../assets/model-mixes-thr-cut.png)

**油门保持** — 无论摇杆位置如何，将通道保持在固定数值，但不具备油门切断所提供的安全联锁：

![油门保持](../assets/model-mixes-thr-hold.png)

与其他混控一样，油门混控同样提供自己的输出通道数量设置：

![油门通道数量](../assets/model-mixes-thr-ch-count.png)

!!! note "油门联锁"
    无论油门切断/油门保持如何设置，Ethos 都要求油门混控的输入先经过 -100% 才会解锁——通过模型选择向导创建的模型已考虑到这一点，手动搭建的油门混控也应如此处理。

## 混控库 {: #mix-libraries }

**新增混控** 对话框中的预定义混控库会依据创建模型时所选的模型类别而有所不同——固定翼、滑翔机、直升机和多旋翼各自提供不同的选项集：

![固定翼混控库](../assets/model-mixes-library-airplane.png)

![滑翔机混控库](../assets/model-mixes-library-glider.png)

![直升机混控库](../assets/model-mixes-library-heli.png)

![多旋翼混控库](../assets/model-mixes-library-multirotor.png)

每个库中还都包含 **自由混控** — 一种没有预设输入/输出的通用混控类型，比专用条目更灵活，但要达到相同效果需要更多的设置工作。

## 按通道视图 {: #per-channel-view }

当同一个输出上叠加了足够多的混控时，仅从上面的平铺列表很难看出它们的合成效果。选中某条混控并选择 **按通道查看**，即可将影响同一输出的所有混控归组显示：

![切换到通道视图](../assets/model-mixes-chview-select.png)

![折叠的通道](../assets/model-mixes-chview-collapsed.png)

![展开的升降舵通道](../assets/model-mixes-chview-elevator.png)

展开某通道的汇总行后，会显示对其有贡献的每一条混控，并各自附带实时数值和图形输出——这有助于确认某条辅助混控（例如襟翼到升降舵的补偿）在主摇杆输入之上究竟叠加了多少量：

![升降舵通道视图详情](../assets/model-mixes-chview-elevator-channel.png)

![升降舵通道，突出显示某条混控](../assets/model-mixes-chview-elevator-channel-view.png)

选中某个子混控（而非汇总行）时，会打开与平铺列表相同的上下文菜单（编辑、切换回列表视图、删除）：

![从通道视图中选择列表视图](../assets/model-mixes-chview-table-view-select.png)

![返回列表视图](../assets/model-mixes-chview-back-at-mixes-view.png)
