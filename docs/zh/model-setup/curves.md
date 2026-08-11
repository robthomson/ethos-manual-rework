---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 曲线

![曲线类型](../assets/model-curves-type.png)

可供[混控设置](mixes.md#anatomy-of-a-mix)或[输出](outputs.md#editing-a-channel)重复使用的响应曲线——两者都内置了 Expo 功能，但更复杂的曲线需要在此处定义（或通过 **Add curve** 定义，该项可从上述任一编辑界面直接进入）。最多可使用 50 条曲线；默认情况下不存在任何曲线（无论如何，Expo 始终为内置功能）。用 **+** 添加曲线；点击已有曲线可进行 **Edit**/**Move**/**Copy-paste**/**Clone**/**Delete**。

![添加曲线](../assets/model-curves-add.png)

## 曲线类型

- **Expo** —— 默认值为 40；正值使中位附近的响应变柔和，负值则使其更灵敏。柔化中位附近的响应有助于避免操作过量，对经验较少的飞手尤其有用。

  ![Expo](../assets/model-curves-expo.png)

- **Function** —— 一小组固定的数学曲线形状：

  ![函数类型](../assets/model-curves-fn-types.png)

  - **x > 0** —— 信号源为正值时原样输出；为负值时输出 0。

    ![x > 0](../assets/model-curves-fn-xgt0.png)

  - **x < 0** —— 与上者镜像：为负值时原样输出，为正值时输出 0。

    ![x < 0](../assets/model-curves-fn-xlt0.png)

  - **|x|** —— 以绝对值形式输出信号源（始终为正）。

    ![|x|](../assets/model-curves-fn-barx.png)

  - **f > 0** —— 信号源为正值时输出 100%，为负值时输出 0（这是一个硬开关，而非原样输出）。

    ![f > 0](../assets/model-curves-fn-fgt0.png)

  - **f < 0** —— 为负值时输出 −100%，为正值时输出 0。

    ![f < 0](../assets/model-curves-fn-flt0.png)

  - **|f|** —— 为负值时输出 −100%，为正值时输出 +100%。

    ![|f|](../assets/model-curves-fn-barf.png)

  每种曲线类型——包括 Function——都还有一个 **Offset**（偏移），可将曲线在 Y 轴上上移或下移（精度为一位小数，与一般的 Y 值相同）：

  ![函数偏移](../assets/model-curves-fn-xgt0-offset.png)

- **Custom** —— 基于点的曲线，默认 5 个点，最多 21 个。

  ![5 点自定义曲线](../assets/model-curves-custom5.png)

  - **Smooth** —— 让曲线平滑地穿过所有点，而不是在各点之间使用直线段。

    ![平滑曲线](../assets/model-curves-custom5-2-smooth.png)

  - **Easy mode** —— 设为 **On** 时，仅允许编辑均匀分布的 Y 坐标（X 固定）；设为 **Off** 时，可编辑每个点的 X 和 Y，但 −100%/+100% 两个端点除外，它们被锁定，因为曲线必须始终覆盖完整的信号范围。

    ![Easy mode 关闭](../assets/model-curves-custom-easy-off.png)

  **编辑器控制项**（与[输出平衡曲线编辑器](outputs.md#balance-channels)的模式相同）：

  - **Source** —— 默认为该曲线自身的混控信号源，或选择 **Auto analog input** 以自动捕捉第一个被拨动的摇杆/滑块/电位器。
  - 滚轮编码器具有就近点吸附功能，并有 **Lock** 开关，可在观察舵面实际动作时冻结输入。
  - 实时游标显示当前驱动曲线的输入值，便于在调整前将其对准某个点。

## 通过 Var 驱动曲线

Function 曲线的 **Offset** 以及 **Custom** 曲线的单个点，都可以由 [Var](variables.md) 驱动，而不使用固定值——并且该 Var 又可通过重新指派用途的微调在飞行中进行调整：

![由 Var 驱动的函数偏移](../assets/model-curves-fn-offset-var.png)
![由 Var 驱动的自定义曲线点](../assets/model-curves-custom-with-var.png)

有关此用法的完整实例，请参阅[变量](variables.md)以及[操作指南：飞行中可调补偿曲线](../how-to/in-flight-compensation-curve.md)。
