---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 用户自定义文本检查清单

![用户检查清单文本](../assets/model-checklist-user-checklist.png)

[检查清单](../model-setup/checklist.md)功能可在启动时显示自定义文本——纯文本或 Markdown 格式文本——每次加载该模型时都会自动显示。

## 1. 创建检查清单文本

**纯文本** —— 使用任意文本编辑器编写（Notepad++，甚至可用 MS Word 另存为纯文本），并保存为 `<model name>.txt`。

**增强文本（Markdown）** —— Ethos 支持 Markdown 格式，例如用 `##` 表示标题，用 `**bold**` 表示粗体文本。可使用任意文本编辑器（手动输入 Markdown 语法），或使用专用的 Markdown 编辑器（Nextpad、MarkText 等），并保存为 `<model name>.md`。

```markdown
## Emphasis
**this is bold text**
*this is italic text*
```

## 2. 将文件复制到遥控器

将该文件复制到与模型自身 `.bin` 文件相同的 `models/` 文件夹中（参见[文件管理器](../system-setup/file-manager.md#top-level-folders)），然后在断开连接前安全弹出遥控器的磁盘驱动器。

## 3. 查看检查清单

加载该模型——检查清单文本现在会作为启动检查的一部分自动显示；若内容超过一屏，可滚动查看。
