---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 蝴蝶(乌鸦)混控

蝴蝶(又称 crow)刹车用于控制下降率,主要用于滑翔机:副翼小幅上抬,同时襟翼大幅下放,产生显著阻力——非常适合控制着陆进场。本教程假设滑翔机的襟翼通道已经存在(由 [Model Select](../model-setup/model-select.md) 向导创建),并以油门摇杆作为刹车输入:摇杆推到顶时无蝴蝶动作,随着摇杆下移逐渐加大,同时加入升降舵补偿,使滑翔机在施加 crow 时不会向上抬头。

## 1. 关闭默认的襟翼混控

![关闭襟翼混控](../assets/how-to-butterfly-flaps-disable.png)

将向导创建的襟翼混控的 **Active condition** 设为 `---`——该混控将不再使用。

## 2. 创建蝴蝶混控

![已添加蝴蝶混控](../assets/how-to-butterfly-mix-added.png)

点按任意混控,选择 **Add Mix** → 从[混控库](../model-setup/mixes.md#mix-libraries)中选择 **Butterfly**,将其放在(现已禁用的)襟翼混控之后。

## 3. 配置输入

![油门输入](../assets/how-to-butterfly-mix-source-thr.png)

将 **Input** 设为 **Throttle**。由于油门在摇杆推到顶时通常读数为最大值,而蝴蝶动作需要在摇杆推到顶时为 0,因此在 Throttle 上长按 `ENT` 并选择 **Invert**:

![反转油门](../assets/how-to-butterfly-mix-source-thr-neg-select.png)
![已反转的油门](../assets/how-to-butterfly-mix-source-thr-neg.png)

现在摇杆完全推到顶时输入读数为 0,该字段显示为 `-Throttle`,以确认已反转。如果蝴蝶功能不应始终可用,可将 **Active condition** 设为着陆飞行模式(或其他开关)。

## 4. 添加死区曲线

![选择曲线](../assets/how-to-butterfly-mix-curve-select.png)

在摇杆零位端设置少量死区,可避免摇杆在接近限位处的微小抖动导致意外展开。添加一条自定义 3 点曲线(例如命名为 "Crowdb"),并关闭 **Easy mode**,以便可以移动 X 坐标点:

![3 点曲线](../assets/how-to-butterfly-mix-curve-3pt.png)
![曲线点](../assets/how-to-butterfly-mix-curve-3pt-points.png)

!!! note
    为蝴蝶混控添加自定义曲线后,其内部的 0–100 偏移(通常会自动应用)将被移除——此时需要由曲线本身来实现该 0–100 变换。在本例中,输出在油门摇杆到达 −90% 之前保持 0%,随后线性上升至 100%:

    ![已添加曲线](../assets/how-to-butterfly-mix-curve-added.png)

## 5. 配置副翼与襟翼

![副翼输出](../assets/how-to-butterfly-mix-ailerons.png)

通常的分配方式是副翼小幅上抬(例如 20%)配合襟翼大幅下放。襟翼一般需要的下行行程远大于上行行程——常见做法是在连杆机构中将襟翼舵机摇臂相对中立位偏置 20–30°,这样舵机处于中立位时襟翼大致处于半下放状态:

![襟翼上抬](../assets/how-to-butterfly-mix-flaps-up.png)
![襟翼下放](../assets/how-to-butterfly-mix-flaps-down.png)

将襟翼混控权重设得较高(例如 −180%)以获得最大行程;实际的物理行程则由 [Outputs](../model-setup/outputs.md) 中的 Min/Max 控制。

!!! tip
    为避免过度驱动舵机,一开始将 Outputs 的 Min/Max 设得保守一些(例如 ±30%),在最终调试时再谨慎放宽,并注意是否出现机构卡滞。

## 6. 添加"襟翼中立位"偏移混控

![80% 偏移混控](../assets/how-to-butterfly-offset-mix-80.png)

由于舵机摇臂偏置后,舵机中立位时襟翼已有约 20–30% 的偏转,因此需要用一个 **Offset Mix** 将其恢复到真正的机翼中立位以进行常规飞行。先设置 80% 的偏移量(后续再调整),并将 2 个输出通道映射到两个襟翼通道:

![带偏移的襟翼上抬](../assets/how-to-butterfly-offset-mix-flaps-up.png)
![带偏移的襟翼下放](../assets/how-to-butterfly-offset-mix-flaps-down.png)

将油门摇杆完全推到顶(蝴蝶混控关闭),确认襟翼混控数值处于偏移量位置(80%);将襟翼摇杆推到完全展开位置时,混控输出应变化整个权重值(例如从 80% 降到 −100%,共 180% 的变化幅度)。实际行程限制可在 Outputs 中通过 Min/Max 或曲线进行微调。

## 7. 添加升降舵补偿曲线与混控 {: #7-add-the-elevator-compensation-curve-and-mix }

![补偿曲线](../assets/how-to-butterfly-comp-curve.png)
![补偿曲线点](../assets/how-to-butterfly-comp-curve-points.png)

由于所需的补偿量是非线性的,应使用曲线而非固定权重。定义一条自定义 5 点曲线(例如 "EleComp")——本例各点起始值为 12%/10%/8%/5%/0%;如果没有适用于你的机体的已知起始值,这些数值需要通过实际试飞确定。

接下来,将该曲线转换为可用作混控 **Weight** 的数值:添加一个[自由混控](../model-setup/mixes.md#mix-libraries)("EleCompx"),以 Throttle 为信号源并附加 EleComp 曲线,输出到一个较高的未使用通道(例如 CH20):

![CH20 上的补偿混控](../assets/how-to-butterfly-comp-mix-ch20.png)

回到蝴蝶混控,在升降舵输出的 **Weight** 上长按 `ENT`,选择 **Use a source**,然后从 Channels 类别中选取 CH20(EleCompx):

![升降舵以 CH20 作为信号源](../assets/how-to-butterfly-mix-ele-use-ch20.png)
![选择信号源](../assets/how-to-butterfly-mix-ele-use-source.png)

至此蝴蝶混控已完全配置完成:

![升降舵补偿配置完成](../assets/how-to-butterfly-mix-ele-comp.png)

## 8. 使用按通道视图进行验证

![按通道视图](../assets/how-to-butterfly-mix-ele-comp-view-per-ch.png)

在升降舵上切换到[按通道视图](../model-setup/mixes.md#per-channel-view),可以在移动油门/刹车摇杆时同时观察所有参与混控的项目(摇杆输入 + 蝴蝶补偿)的变化——这比平铺的表格视图更便于排查问题。

!!! tip
    在确定补偿曲线的初始数值之前,最好先获取升降舵行程与襟翼偏转量之间的对应数据(来自机体制造商或社区资料)。若无此类数据,可从襟翼完全展开时对应几毫米的升降舵行程开始,再逐步优化。
