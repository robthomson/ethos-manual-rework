---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# 查找最新的引导程序或其他组件版本

Ethos 固件发布包中会附带一个 `components.json` 文件，其中列出了每款遥控器各个组件的当前版本，可用于在刷写之前确认某个引导程序/固件/音频/系统文件版本是否确实为最新版本。

!!! note "截图待补充"
    本页尚无模拟器截图 —— 参见[截图流程](../contributing/screenshot-pipeline.md)。

1. 从最新的 Ethos 发布包中下载 `components.json`。
2. 使用文本编辑器（VS Code、记事本等）打开该文件。
3. 找到对应你的遥控器的部分 —— 例如 `X20`：

   ```json
   {
     "targets": ["X20", "X20S", "X18", "X18S", "XE", "XE-S", "X20 Pro"],
     "components": [
       { "name": "bootloader", "version": "1.4.15" },
       { "name": "firmware", "version": "1.6.1" },
       { "name": "audio", "version": "1.6.1" },
       { "name": "system_files", "version": "1.6.1" }
     ]
   }
   ```

   （这只是某个版本的快照示例 —— 实际版本号请务必查阅*当前*发布包中的文件。）

4. 读取你所需组件对应的版本号 —— 在上面的示例中，X20 系列的最新引导程序版本为 `1.4.15`。

关于下载的固件文件应放置在何处，请参见[文件管理器](../system-setup/file-manager.md#top-level-folders)；关于如何让遥控器进入引导程序模式以进行刷写，请参见 [USB 连接模式](../getting-started/usb-connection-modes.md#bootloader-mode) —— 或者直接使用 [Ethos Suite](../ethos-suite/index.md)，它会自动完成版本检查与刷写。
