---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 变量

![变量](../assets/model-vars.png)

变量（"Vars"）是用于存放模型自身设置值的命名容器，可在编程的任何其他位置引用——包括[混控设置](mixes.md)。将它们集中在专门的页面中，可把模型的*配置数据*与*编程逻辑*分离开来：无需在数十条混控中翻找并调整某个数值，所有内容都以有意义的名称集中在一处。共有 64 个变量可用，默认情况下一个都不存在。使用 **+** 添加变量；点击已有变量可进行**编辑**/**移动**/**复制**/**克隆**/**删除**。

![添加变量](../assets/model-vars-add.png)

变量可以保存一个固定常量，也可以在用户定义的限值范围内可调（以防止错误数值导致坠机），并且可以针对每个激活条件（例如每个飞行模式）保存*不同*的数值。数值在关机后仍会保留。在任何可使用[选项功能](../getting-started/user-interface-and-navigation.md#the-options-feature)（带汉堡图标的字段）的位置，变量都可以替代普通数值。

!!! example
    一架带分离式副翼的滑翔机（内侧翼面同时兼作着陆襟翼）希望在四个翼面全部作为副翼工作时，各处共用同一个副翼差动设置——用一个变量保存该数值，并在每条相关混控中引用它，即可保持一致，并且只需在一处调整。

## 添加变量

![新建变量](../assets/model-vars-new_var.png)

- **Value** — 当前值（只读显示）。
- **Name** — 可编辑。
- **Comment** — 说明其用途的自由文本。
- **Range** — 变量数值永不可超出的下限/上限（一位小数，范围在 ±500% 之内）。

### 数值

![变量数值](../assets/model-vars-values.png)

- **Fixed** — 单一常量，保留一位小数。
- **Multiple/variable** — **Add new value** 可为每个激活条件附加一个数值。例如，当飞行模式 Thermal（FM4）激活时 `Var12` 读数为 9%，而当 Speed（FM5）激活时为 −3%，其 Range 限制为 −10%…+15%，因此两者都不会超出合理限值：

  ![随飞行模式变化的数值](../assets/model-vars-fm-dependent.png)
  ![添加数值](../assets/model-vars-add-value.png)

### 动作

![变量动作](../assets/model-vars-actions.png)
![添加动作](../assets/model-vars-add-action.png)

动作由某个输入驱动，使变量的数值随时间发生变化。

**Repurposed trim** — 将某个物理微调从其常规功能转为调整该变量，通常限定在某一个激活条件下生效：

![重定义微调用途](../assets/model-vars-functions-repurpose.png)
![选择要重定义用途的微调](../assets/model-vars-functions-repurpose-select.png)

!!! example
    将油门微调重定义为调整弯度补偿变量，但仅在飞行模式 Landing（FM3）激活时有效，Range 为 0–25%，每次点动步长为 1.0%。在该激活条件之外，该微调会自动恢复其常规功能。

**算术动作** — 可由任意输入驱动：

- **Assign** — 将变量设为指定数值。
- **Add** / **Subtract** / **Multiply** / **Divide** — 对当前值进行算术运算。
- **Percentage** — 取驱动输入的一个百分比。
- **Min** / **Max** — 以驱动输入对变量进行限幅。

  ![功能动作](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` 直接将变量赋值为 40%；`FS1(edge)` 每按一次加 2（以 Range 上限为限）；`FS2(edge)` 每按一次减 2（以 Range 下限为限）。此处 **Edge** 选项（长按功能开关）很重要——若不使用它，只要开关保持在该位置，动作就会持续反复触发，而不是每按一次触发一次。

  ![实例演示](../assets/model-vars-calc-example.png)
