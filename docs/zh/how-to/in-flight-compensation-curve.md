---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# 飞行中可调补偿曲线

## 目的

放下襟翼会改变机翼弯度——上单翼机往往会"抬头上飘"，下单翼机往往会下沉——所需的升降舵修正量与襟翼行程并非线性关系，因此需要使用曲线而非固定偏移量。本教程使用 [Vars](../model-setup/variables.md) 将补偿曲线的各点变为**飞行中可调**，通过一个改用的油门微调进行调整，并根据襟翼摇杆当前靠近哪个曲线点来切换调节对象——本教程在[操作指南：蝴蝶混控](butterfly-mixer.md)中的升降舵补偿步骤基础上展开。

## 1. 选择曲线类型

一条 5 点[自定义曲线](../model-setup/curves.md)足以实现平滑补偿，又不会过于复杂。第 5 点（最右侧，襟翼摇杆完全推上／无襟翼）始终固定为零——未放下襟翼时无需补偿。其余 4 个点通过 Vars 变为可调。由于襟翼摇杆经常停在两个已定义点之间，因此在重叠区域内，摇杆两侧的两个点需要能够同时调节。

## 2. 计算重叠区间

各点对应的区间（经许可改编自 Mike Shellim 在 rc-soar.com 发布的 OpenTX "Crow-aware adaptive elevator trim"——略作扩展，使 Pt2 的区间一直延伸到 +100%，原因见[第 6 步](#6-apply-the-curve)）：

| 襟翼摇杆区间 | 生效的点 |
|---|---|
| +100% 至 +45% | 仅 Pt2 |
| +45% 至 +20% | Pt2 与 Pt3 |
| +20% 至 −20% | 仅 Pt3 |
| −20% 至 −45% | Pt3 与 Pt4 |
| −45% 至 −90% | 仅 Pt4 |
| −90% 至 −100% | 仅 Pt5 |

## 3. 配置逻辑开关

![自适应点逻辑开关](../assets/how-in-flight-comp-lsws.png)

建立四个[逻辑开关](../model-setup/logical-switches.md)，每个都对襟翼（油门）摇杆使用 **Range**（范围）判断，当摇杆处于该点的区域内时激活：

- `AdaptivePt2` —— 范围 20% 至 100%（特意扩展到 100%，以便在完全未放襟翼时也能调节 Pt2——参见第 6 步）。

  ![AdaptivePt2](../assets/how-in-flight-comp-lsw-adaptivept2.png)

- `AdaptivePt3` —— 范围 −45% 至 45%。

  ![AdaptivePt3](../assets/how-in-flight-comp-lsw-adaptivept3.png)

- `AdaptivePt4` —— 范围 −90% 至 −20%。

  ![AdaptivePt4](../assets/how-in-flight-comp-lsw-adaptivept4.png)

- `AdaptivePt5` —— 范围 −100% 至 −90%。

  ![AdaptivePt5](../assets/how-in-flight-comp-lsw-adaptivept5.png)

## 4. 定义调节用 Vars

![Vars 总览](../assets/how-in-flight-comp-vars.png)

建立四个 [Vars](../model-setup/variables.md)：`VAdjPt2`–`VAdjPt5`，范围均为 0–50%（如有需要可加大），并各自设置一个**改用的油门微调**动作——步进值 1.0%，激活条件为对应的逻辑开关：

![VAdjPt2](../assets/how-in-flight-comp-var-vadjpt2.png)
![VAdjPt2 动作](../assets/how-in-flight-comp-var-vadjpt2-2.png)
![VAdjPt3](../assets/how-in-flight-comp-var-vadjpt3.png)
![VAdjPt3 动作](../assets/how-in-flight-comp-var-vadjpt3-2.png)
![VAdjPt4](../assets/how-in-flight-comp-var-vadjpt4.png)
![VAdjPt4 动作](../assets/how-in-flight-comp-var-vadjpt4-2.png)
![VAdjPt5](../assets/how-in-flight-comp-var-vadjpt5.png)
![VAdjPt5 动作](../assets/how-in-flight-comp-var-vadjpt5-2.png)

由于同一时刻只有一个逻辑开关（在重叠区域内最多两个）处于激活状态，因此同一个物理微调可以根据襟翼位置安全地调节不同的 Vars。

## 5. 定义补偿曲线

![补偿曲线](../assets/how-in-flight-comp-var-comp-curve.png)
![补偿曲线各点](../assets/how-in-flight-comp-var-comp-curve-pts.png)

新建一条 5 点自定义曲线（例如命名为 "EleComp"），并启用 **Smooth**（平滑）。在第 1–4 点上长按 `ENT`，选择 **Use a source**（使用信号源），分别指定为 `VAdjPt5`…`VAdjPt2`（第 5 点按第 1 步所述固定为 0）。

## 6. 应用曲线 {: #6-apply-the-curve }

将这条曲线用在[操作指南：蝴蝶混控](butterfly-mixer.md#7-add-the-elevator-compensation-curve-and-mix)中把 EleComp 曲线接入升降舵补偿混控的相同位置。

条件允许时，应从真实数据出发（厂商说明、社区帖子），了解特定襟翼行程需要多少升降舵行程；否则，以全襟翼时几毫米的补偿量作为起点是比较合理的。

!!! tip "调试方法"
    从小襟翼行程和小幅微调开始。`AdaptivePt2` 可以在**完全未放襟翼**的情况下调试——放一点襟翼，再收回，每次只加入少量补偿，而不是在模型上飘或下沉时手忙脚乱地边挣扎边微调。再放一点襟翼进行检查，必要时继续调整。一旦 Pt2 感觉合适，就移到摇杆中位附近的下一个点——如果 Pt2 需要较大的微调量，值得先降落，把其余各点依次设置为略大于前一个点的值，而不是盲目猜测。
