---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 模型选择

![模型向导 - 固定翼](../assets/model-modelselect-model-wizard-airplane.png)

用于创建、选择、克隆和删除模型，并管理用于归类模型的用户自定义分类文件夹。

## 管理模型文件夹

![模型文件夹](../assets/model-modelselect-folders.png)

Ethos 允许你将模型归入自定义的文件夹中——通常是诸如固定翼、滑翔机、直升机、多轴、老式战机、船、车、模板或存档之类的分类。在你创建任何文件夹之前，模型都存放在自动生成的 **Uncategorized**（未分类）文件夹中（该文件夹在升级到 Ethos 1.1.0 alpha 17+ 时创建，或当模型文件从别处复制到 `\Models` 中时创建）；一旦该文件夹为空，Ethos 会将其再次删除。

要创建文件夹，请点按 "Uncategorized" 旁的 **+**（或长按 `PAGE` 上/下键），为其命名（最多 15 个字符）并确认。文件夹按字母顺序排列，**Uncategorized** 始终排在最后，并且与 SD card/eMMC 上 `\Models` 下的子文件夹直接对应。点按文件夹名称可打开重命名/删除操作——删除文件夹会将其中的所有模型移回 Uncategorized。

![更改文件夹](../assets/model-modelselect-folder-change-select.png)

要移动模型，点按其图标，选择 **Change folder**，然后点按目标文件夹：

![选择文件夹](../assets/model-modelselect-folder-airplane-select.png)

## 添加新模型

![创建模型](../assets/model-modelselect-model-create.png)

选择要在其中创建模型的分类，点按 **+**，然后点按 **Create model** 启动向导（若分类尚不存在，请先创建分类）。向导支持 **Airplane**（固定翼）、**Glider**（滑翔机）、**Helicopter**（直升机）、**Multirotor**（多轴）和 **Other**（其他）；每种向导都会引导你完成该机型的基本设置，包括针对 FrSky 增稳接收机的可选预设混控（增益、增稳模式）。模型名称最多 15 个字符。

### 增稳接收机与通道顺序

![向导：固定翼](../assets/model-modelselect-model-wizard-airplane.png)

FrSky 增稳接收机要求通道顺序必须为 **AETR**——请将 [摇杆 → 通道顺序](../system-setup/controls.md) 保持为默认的 AETR，并开启 **First four channels fixed**（前四通道固定），使向导的输出与接收机的预期一致。

向导按从右到左的顺序分配通道。对于 2 副翼 + 1 升降舵 + 1 方向舵 + 1 电机，分配如下：

| 通道 | 功能 |
|---|---|
| 1 | 副翼 1（右副翼） |
| 2 | 升降舵 |
| 3 | 油门 |
| 4 | 方向舵 |
| 5 | 副翼 2（左副翼） |

采用此分配方式时，常规情况下（上偏行程大于下偏行程）副翼差动为**正值**。FrSky 官方的接收机说明书目前记载的是*相反*的约定（从左到右，即 Ch1 = 左副翼，Ch5 = 右副翼）——在这种情况下，要获得相同的物理效果，差动就需要设为**负值**。

!!! tip
    建议始终统一使用 Ethos 的约定——无论采用哪种方式，所有增稳功能都能正常工作，因为补偿方向是在增稳设置过程中设定的。如果确实需要与接收机说明书的约定保持一致，最简单的方法是先按常规用向导建立模型，然后在 [输出](outputs.md) 中使用 **Swap channels**（交换通道）将两个副翼通道对调——这样可以使副翼混控的差动符号保持为正值。

### 向导步骤

![向导：尾翼类型](../assets/model-modelselect-model-wizard-tail.png)
![向导：副翼/襟翼数量](../assets/model-modelselect-model-wizard-ail-and-flaps.png)
![向导：升降舵/方向舵数量](../assets/model-modelselect-model-wizard-ele-and-rudder.png)
![向导：动力](../assets/model-modelselect-model-wizard-engine.png)
![向导：通道重新分配](../assets/model-modelselect-model-wizard-ch-reassignment.png)
![向导：名称](../assets/model-modelselect-model-wizard-name.png)
![向导：接收机](../assets/model-modelselect-model-wizard-rx.png)

对于 **Airplane**（固定翼），在设置尾翼类型/舵面数量之后，向导会依次涉及动力通道数量，然后是副翼/襟翼通道数量。

**尾翼配置**可在传统十字尾、V 尾或无尾（三角翼/飞翼）之间选择：

- **三角翼/飞翼**——创建带 2 个副翼且无尾翼舵面的固定翼模型时，会自动建立升降副翼（elevon）混控，默认权重为 50%，因此副翼 + 升降舵同时满打时总量仍为 100%。
- **由增稳接收机完成混控的三角翼**——此时应改选 1 个副翼和 1 个升降舵；升降副翼混控在接收机内完成，具体参见其自身说明书。
- **带独立副翼和升降舵舵面的三角翼**——让向导按有尾翼的模型运行；它会配置所需的副翼和升降舵通道（可带或不带方向舵），且不会创建升降副翼混控。

**通道重新分配**步骤允许你覆盖向导的默认映射，但请注意增稳接收机需要按特定顺序排列通道（请查阅接收机自身的说明）。最后一步设置模型名称并关联图片。

完成的模型会存放在启动向导时所处的分类文件夹中，并在其中按字母顺序排列。完整的实操演示参见 [固定翼基础示例](../tutorials/basic-fixed-wing.md)。

## 从另一台 Ethos 遥控器接收模型

![接收模型](../assets/model-modelselect-model-receive.png)

选择目标分类，点按 **+**，然后点按 **Receive model**——遥控器会进入等待状态并显示其 Bluetooth 地址，以便发送方找到它。在发送方遥控器上，点按模型并选择 **Send model**；接收方遥控器会在接受前确认传入的文件名。

## 选择模型

点按 **Model select** 打开模型列表。

!!! note "Ethos 升级后的模型转换"
    Ethos 会在版本升级后首次*选中*某个模型时对其单独进行转换，而不是在升级时一次性全部转换——转换过程没有明显延迟，且在之后的任何时候进行都是安全的，即使是在更新的 Ethos 版本下也一样。当发生转换时（或当你编辑模型时），选择界面底部的 **Last Modification**（最后修改）日期会更新——否则保持不变。

**快速选择**——在模型图标上长触摸或长按 `ENT` 可立即切换到该模型。

**模型管理菜单**——点按模型将其高亮，再次点按可打开菜单：

- **Set current model**（设为当前模型）
- **Clone**（克隆）——复制该模型。克隆出的模型会自动获得新的接收机编号；如果你改为重新指定原模型的接收机编号，则无需重新对频即可使用。
- **Change folder**（更改文件夹）
- **Send**/**Receive**（发送/接收）——如上文所述，与另一台遥控器之间收发。
- **Delete**（删除）——仅对非当前模型提供该选项。
