---
translated_from: f134e06b5d1e428e1d1dff7dfb14c47cd1c22630
---

# 固定翼基础示例

本文完整演示一架“电机 + 2 副翼 + 2 襟翼 + 升降舵 + 方向舵”的飞机，每个舵面各用一个舵机，全程使用向导从头到尾完成配置。请先完成 [遥控器初始设置](initial-radio-setup.md)。

## 第 1 步：确认系统设置

本示例使用默认的 **AETR** 通道顺序。

## 第 2 步：确定所需的舵机/通道

[混控设置](../model-setup/mixes.md) 是遥控器的核心 —— 最多可有 100 个混控通道，通常将编号最小的分配给舵机（因为通道编号直接对应接收机通道；X20 内置 RF 模块最多支持 24 个输出通道）。较高编号的通道可自由用作虚拟通道，或通过多个 RF 模块与 SBUS 扩展出更多实际通道。本机型的配置：

| 功能 | 通道数 |
|---|---|
| 电机 | 1 |
| 副翼 | 2 |
| 襟翼 | 2 |
| 升降舵 | 1 |
| 方向舵 | 1 |

（起落架收放将在稍后添加，见 [第 10 步](#step-10-add-a-mix-for-retracts)。）

## 第 3 步：新建模型

![创建飞机模型](../assets/tut-fw-eg-wiz-create-airplane.png)

在 [模型选择](../model-setup/model-select.md) 中选择一个类别，点击 **+**，启动 **Airplane（飞机）** 向导。本示例选择 **Non stabilized receiver（非增稳接收机）**。

![发动机通道](../assets/tut-fw-eg-wiz-engine.png)
![副翼/襟翼通道](../assets/tut-fw-eg-wiz-ail-flaps.png)

接受 1 个发动机通道，然后选择 2 个副翼通道和 2 个襟翼通道。

![尾翼类型](../assets/tut-fw-eg-wiz-tail.png)
![升降舵/方向舵通道](../assets/tut-fw-eg-wiz-ele-rudd.png)

接受默认的 **Traditional Tail（常规尾翼）**，升降舵和方向舵各 1 个通道。

![模型名称](../assets/tut-fw-eg-wiz-name.png)
![接收机](../assets/tut-fw-eg-wiz-rx.png)

为模型命名（例如 “FWexample”，最多 15 个字符），完成向导，该模型即成为当前活动模型，并创建在 Airplane 类别中。

## 第 4 步：检查并配置混控

![混控总览](../assets/tut-fw-eg-mixes.png)

向导已自动建立副翼（通道 1 和 5）、升降舵、油门、方向舵以及襟翼混控（襟翼显示为 `---`，表示尚未分配信号源）。

### 副翼 {: #ailerons }

![副翼混控](../assets/tut-fw-eg-mixes-ail-mix.png)
![编辑副翼混控](../assets/tut-fw-eg-mixes-ail-edit.png)

**Weight/Rates（权重/舵量）** —— 试飞任何新模型前都应先设置好舵量：较小的行程（例如 30%）适合运动飞行，完整的 100% 适合 3D 飞行。为开关 SB 中位添加 60% 舵量、SB 下位添加 30% 舵量 —— 默认值（SB 上位）保持 100%：

![权重舵量](../assets/tut-fw-eg-mixes-ail-weight-rates.png)

**Expo（指数）** —— 线性响应在中立点附近可能显得过于灵敏；添加 Expo 舵量（例如在同样的 SB 三个位置分别为 60%/40%/20%），可在不减小最大行程的前提下柔化中立点附近的响应：

![Expo 舵量](../assets/tut-fw-eg-mixes-ail-expo-rates.png)

**Differential（差动）** —— 副翼上下行程相等时，下行副翼产生的阻力大于上行副翼，会使机头偏离转弯方向（“反向偏航”）。设置正差动（常用 50%）可减小下行行程相对上行行程的量，从而抑制这一现象：

![50% 差动](../assets/tut-fw-eg-mixes-ail-diff-50.png)

若要在飞行中调整差动，长按数值上的 `ENT`，选择 **Use a source（使用信号源）**，并选取 Pot1：

![使用信号源](../assets/tut-fw-eg-mixes-ail-diff-use-source.png)
![已选择 Pot1](../assets/tut-fw-eg-mixes-ail-diff-use-pot1.png)

对飞行中调出的数值满意后，再次长按并选择 **Convert to value（转换为数值）**，将其永久固定下来：

![转换为数值](../assets/tut-fw-eg-mixes-ail-diff-convert-to-value.png)

**Trim（微调）** —— 可以断开该混控与其关联微调的联系，而不必禁用微调本身，从而将该微调释放出来用于其他用途：

![副翼微调](../assets/tut-fw-eg-mixes-ail-trim.png)

### 升降舵与方向舵

采用同样的三段舵量 + Expo 方式，此处使用开关 SC：

![升降舵 Expo 舵量](../assets/tut-fw-eg-mixes-ele-expo-rates.png)

### 油门

![油门混控](../assets/tut-fw-eg-mixes-thr-edit.png)

输入保持为油门摇杆 —— 无需舵量/Expo —— 但安全开关是必不可少的；模型发动机或电机意外启动可能造成严重伤害。

**Low position trim（低位微调）**（甲醇/汽油发动机）—— 可独立于全油门调整怠速转速：

![低位微调](../assets/tut-fw-eg-mixes-thr-low-pos-trim.png)

启用后，摇杆处于怠速位置时油门通道位于 −75%；此时油门微调杆可在 −100% 至 −50% 之间调整怠速。

**Throttle cut（油门切断）** —— 一种安全锁定。以开关 SA 下位作为激活条件（激活时以粗体显示），当摇杆低于 −85% 后，油门输出即保持在 −100%：

![油门切断](../assets/tut-fw-eg-mixes-thr-cut.png)

若改为启用 **Sticky（粘滞）**，则只要 SA 拨到下位，油门便**立即**切断，与摇杆位置无关：

![粘滞油门切断](../assets/tut-fw-eg-mixes-thr-cut-sticky-on.png)

无论采用哪种方式，一旦激活条件解除，必须先将摇杆拉回 −85% 以下，油门才能重新增加 —— 以防切断开关一松开电机就跳到大油门位置。

**Throttle hold（油门保持）** —— 一种可从*任意*摇杆位置生效的紧急切断，条件一旦满足，输出立即降至 −100%（或设定值）：

![油门保持](../assets/tut-fw-eg-mixes-thr-hold.png)

### 襟翼

![襟翼输入](../assets/tut-fw-eg-mixes-flaps-input.png)

将襟翼分配给开关 SE，并将两个输出通道的权重均设为 100%：

![襟翼权重](../assets/tut-fw-eg-mixes-flaps-weights.png)

## 第 5 步：对频接收机

通过 [RF System](../model-setup/rf-system.md) 进行注册（若为 ACCESS）并对频。在进入输出设置之前，建议先断开舵机连杆或临时减小舵机行程，以免在设置 Min/Max 限制时过驱动任何部件。

## 第 6 步：配置输出

![输出](../assets/tut-fw-eg-outputs.png)

[输出](../model-setup/outputs.md) 用于将混控器的逻辑适配到模型的实际机械结构。

**Aileron 1（副翼 1）** —— 在优化好机械连杆后，用 **PWM center（PWM 中点）** 将舵机居中，然后设置 **Min**/**Max**。临时将一个电位器分配给 Min（随后同样处理 Max，方法与前面的差动示例相同）可以更快地调出合适数值：

![编辑副翼输出](../assets/tut-fw-eg-outputs-edit-ail.png)

**Flaps（襟翼）** —— 襟翼通常需要较大的下偏量才能有效减速；可在连杆上牺牲部分上行行程来换取下行行程，使舵机居中时襟翼处于半放下位置，再用 Min/Max 设定实际的收起与全放下位置。使用 5 点曲线是修正由此产生的襟翼/副翼动作不匹配的常见方法。最后用 **[通道平衡](../model-setup/outputs.md#balance-channels)** 使左右副翼和襟翼同步。

## 第 7 步：飞行模式简介

[飞行模式](../model-setup/flight-modes.md) 让一个模型可以携带针对不同任务的设置 —— 如同换挡。在可用的 20 个飞行模式中，本示例使用三个：**Default（默认）**、**Flaps Half（半襟翼）**（开关 SE 中位）和 **Flaps Full（全襟翼）**（SE 上位）。条件为真的第一个飞行模式即为活动模式；**Default** 模式完全没有条件，在其他模式都不适用时接管 —— 这也是它没有开关选择项的原因。设置 1 秒的淡入/淡出可使襟翼放下时的切换更平顺。

## 第 8 步：配置微调

处理升降舵微调随襟翼位置变化的两种方法：

**每个飞行模式独立微调** —— 最简单的方案：升降舵微调在各飞行模式下完全独立，随 SE 拨动自动切换。由于每个模式都要从零开始微调，[Instant trim（即时微调）](../model-setup/trims.md#instant-trim) 会很有帮助 —— 先针对常规飞行完成微调，然后降落，以此作为襟翼模式的起点。

**基础微调加偏移** —— 只在 Default 模式下微调一次，各襟翼模式的升降舵补偿以偏移量叠加其上：

1. 将微调 **Step（步进）** 设为 Medium（便于快速初步微调；之后可减小以进行精细调整），**Mode（模式）** 设为 Custom，并添加一条新行为。
2. **Active condition（激活条件）**：`FM1(Flaps Half)`，模式选 **Offset + Default** —— Flaps Half 的微调即为基础微调加上该模式激活时所调出的偏移量：

   ![添加行为](../assets/tut-fw-eg-trims-ele-add-behavior.png)
   ![Offset + Default，FM1](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm1.png)

3. 对 `FM2(Flaps Full)` 重复同样操作：

   ![选择飞行模式](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm-select.png)
   ![Offset + Default，FM2](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-fm2.png)

现在每个襟翼模式都可以独立微调，而之后调整基础 Default 微调时（例如修正舵机热漂移），两个襟翼模式的微调会自动同步偏移相同的量。

![自定义微调选择](../assets/tut-fw-eg-trims-ele-custom-default-plus-offset-select.png)

## 第 9 步：设置飞行电池计时器

在 [计时器](../model-setup/timers.md) 中编辑 Timer 1：**Down（倒计时）** 模式，起始值 5 分钟，在 **Throttle active（油门激活）** 为真时运行（且未被保持复位）。还可以选择性地指定一个比例计时信号源（例如油门摇杆），使计时器在全油门时按实际时间速度运行，油门减小时相应减慢。

## 第 10 步：为起落架收放添加混控 {: #step-10-add-a-mix-for-retracts }

![起落架混控信号源](../assets/tut-fw-eg-retracts-source.png)

点击某个混控，选择 **Add Mix（添加混控）** → **Free Mix（自由混控）**，命名为 “Retracts”，条件设为 Always，信号源设为开关 SF。默认的 Weight = 100% 动作即可 —— 这样便将例如通道 8 分配给起落架收放：

![起落架输出](../assets/tut-fw-eg-retracts-outputs.png)
