---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 基础飞翼（升降副翼）示例

以双舵机升降副翼飞翼为例，采用 Dreamflight Weasel 推荐的行程量/Expo/混控比例作为具体的实操范例。请先完成[遥控器初始设置](initial-radio-setup.md)。

## 步骤 1. 确认系统设置 {: #step-1-confirm-system-settings }

保持默认的 **AETR** 通道顺序，并将 **[前四通道固定](../system-setup/controls.md#first-four-channels-fixed)** 设为 **关闭**。继续之前，请通过 [RF System](../model-setup/rf-system.md) 注册（若使用 ACCESS）并对频接收机。

## 步骤 2. 确定所需的舵机/通道

对于升降副翼机型，[混控设置](../model-setup/mixes.md)会将副翼与升降舵的输入合并到两个物理舵面上——总共只需 2 个通道，每个通道都是两种输入的混合结果。

## 步骤 3. 新建模型

![创建固定翼模型](../assets/tut-wing-eg-wiz-create-airplane.png)

在[模型选择](../model-setup/model-select.md)中启动 **Airplane（固定翼）**向导，选择 **Non stabilized receiver（非增稳接收机）**。

![无动力](../assets/tut-wing-eg-wiz-no-engine.png)

选择 **No engine（无动力）**，接受默认的 2 个副翼通道，并选择 **No flaps（无襟翼）**。

![无尾翼](../assets/tut-wing-eg-wiz-no-tail.png)

尾翼类型选择 **None（无）**——正是这一选择让 Ethos 自动构建升降副翼混控（副翼 + 升降舵输入，同时作用于相同的两个通道）。为模型命名（例如 "Weasel"），选择一个图片，然后完成——它将成为 Airplane 类别中的当前模型。

## 步骤 4. 检查并配置混控

![混控概览](../assets/tut-wing-eg-mixes.png)

向导会在通道 1+2 上创建一个副翼混控，随后*同样*在通道 1+2 上创建一个升降舵混控——两种输入都作用于两个升降副翼通道，这正是升降副翼混控的全部要点。

### 副翼

![副翼混控](../assets/tut-wing-eg-mixes-ail-mix.png)

**Weight/Rates（权重/行程量）**——根据 Weasel 说明书，副翼舵面偏转量应约为升降舵的 3 倍，且两者之和应为 100%：副翼 **75%**，升降舵 **25%**。小行程约为大行程的一半：副翼小行程 **36%**，升降舵小行程 **12%**。

![副翼混控权重](../assets/tut-wing-eg-mixes-ail-mix-weight.png)

**Expo**——Weasel 推荐大行程 35% / 小行程 20%，由开关 SB 向下位置激活，使摇杆中位附近的响应更平缓。

**Differential（差动）**——该机型差动量较小，约 **4%**：

![副翼差动](../assets/tut-wing-eg-mixes-ail-diff-04.png)

（关于差动的作用，参见[基础固定翼示例](basic-fixed-wing.md#ailerons)——此处适用同样的反向偏航原理。）

### 升降舵

![升降舵混控](../assets/tut-wing-eg-mixes-ele-mix.png)

采用相同的模式：大/小行程为 **25%**/**12%**，Expo 值与副翼相同。

### 方向舵

![方向舵混控](../assets/tut-wing-eg-mixes-rud-mix.png)

Weasel 没有方向舵——飞翼通常不需要方向舵。若升降副翼模型*确实*需要方向舵，可在通道 3 上添加一个[自由混控](../model-setup/mixes.md#mix-libraries)。

## 步骤 5. 对频接收机

与[步骤 1](#step-1-confirm-system-settings)相同——在继续之前完成注册/对频；在设定 Min/Max 限制之前，可考虑断开舵机连杆或减小行程，以避免过度驱动任何部件。

## 步骤 6. 检查混控

输出通道 1/2 可重命名为 **Elevon1**/**Elevon2**。当副翼打到最右时，通道 1（右侧，上偏）显示 75%，而通道 2（左侧，下偏）显示 72%——这 3% 的差异*正是*差动在起作用。在此基础上再叠加升降舵满下舵，通道 1 变为 75+25 = 100%，通道 2 变为 72−25 = 47%。

## 步骤 7. 配置舵机最大行程

![副翼满舵](../assets/tut-wing-eg-outputs-full-ail.png)
![副翼满舵 + 升降舵满舵](../assets/tut-wing-eg-outputs-full-ail-full-ele.png)

首先用 **PWM center** 将每个舵机居中。Weasel 推荐的最大行程为副翼 25mm + 升降舵 10mm = 合计 35mm——请分别施加同向*和*反向的副翼/升降舵满量输入，确认两者均未超出机械或舵机极限，然后再设定最终的偏转量。

- **Min/Max** ——硬性限制，永不被覆盖；减小它们会减少行程而非削顶。默认为 ±100%，必要时可扩展至 ±150%。
- **Curve（曲线）**——通常比直接反复调整 Min/Max/Subtrim 更快、更灵活，还有实时图形可参考。3 点曲线适用于大多数输出；在第二个升降副翼上使用 5 点曲线，可以方便地在 5 个点上与第一个舵面同步行程。使用曲线来实现这一点时，请将 Min/Max/Subtrim 保持在直通值（−100/100/0，或在扩展限制下为 −150/150/0），改由曲线来完成整形。
