---
translated_from: 727b0ba85be63990bda647e617a27dce6b255458
---

# 贡献指南

## 本手册为何存在

此前的手册（[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual)）按语言分裂为两个互不相连的部分。英文部分实际上只是一套**截图生成装置**——用 shell 脚本通过 Lua 宏 API 驱动真实的 Ethos 模拟器来抓取界面截图——手册正文本身并没有任何 Markdown（或其他纯文本）源文件；英文文本仅以一堆 PDF/ODT 导出件的形式存在。相比之下，法文部分是一份完整撰写的 GitBook 导出内容，有真实的正文，但其构建与维护完全独立，并拥有自己单独的一套手工粘贴的截图。其他语言则两者皆无。既没有可供翻译的单一权威来源，也无法判断某个已翻译页面何时与（并不存在的）英文原文脱节。

本仓库重新开始，为每种语言的每一个页面采用统一格式：纯 Markdown，使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建（与 [wingflight-docs](https://doc.wingflight.org) 所用技术栈相同），并在每次推送到 `main` 时部署至 GitHub Pages。

## 工作流程

内容前端没有 CMS 或网页编辑器——撰写者与译者直接在 git 中工作，与对本仓库的任何其他改动一样：

1. 从 `main` 创建分支（直接在本仓库中——参见下文关于 fork 的说明）。
2. 编辑 `docs/en/` 下的相关 `.md` 文件。
3. 使用 `mkdocs serve` 在本地预览（参见根目录的 [README](https://github.com/robthomson/ethos-manual-rework)），或直接提交拉取请求并使用下文所述的自动 PR 预览。
4. 提交拉取请求。

页面引用的截图与页面一同存放在 `docs/en/assets/` 中，只是普通的 Markdown 图片链接——没有特殊语法。截图的生成方式请参见[截图流水线](screenshot-pipeline.md)。

### PR 预览 {: #pr-previews }

针对 `main` 的每个拉取请求都会获得独立的实时预览，由 `.github/workflows/pr-preview.yml` 自动构建并部署：地址为 `manual.rt-rc.com/pr-preview/<PR number>/`，会通过机器人评论链接在 PR 中，并在每次推送时更新。PR 关闭时预览会自动移除。主站本身（`manual.rt-rc.com`）不受影响——预览与其并存于 `gh-pages` 分支上的 `pr-preview/` 文件夹中，该文件夹在每次生产部署后依然保留。

此机制仅对直接推送到本仓库的分支生效，不适用于 fork——来自 fork 的 PR 不会获得实时预览（GitHub 有意不向 fork 触发的 `pull_request` 工作流授予 `GITHUB_TOKEN` 的写权限，以防 fork 利用 CI 向 `gh-pages` 推送任意内容）。来自 fork 的贡献者仍可使用 `mkdocs serve` 在本地预览。

## 版本管理

多个固件版本的手册（例如 1.6 与未来的 Ethos26 并存）以独立分支的形式位于同一仓库中，各自部署到自己的 `manual.rt-rc.com/<version>/` 路径，并配有版本选择下拉菜单——完整方案及如何新建版本请参见[版本管理](versioning.md)。

## 翻译方案 {: #translation-plan }

译者（人工或 AI）直接在 git 中工作，与任何其他改动一样——没有 CMS，也没有独立的翻译应用。首次法文试点（少量页面）已完整验证了整套机制；以下是实际的操作方式。

### 新增/更新翻译 {: #addingupdating-a-translation }

1. 创建分支，新建/编辑 `docs/<locale>/<与英文页面相同的路径>`，翻译正文。代码字面文本（如 `ENT`、`RTN` 等按键名称、屏幕上显示的界面元素名称）保持原样。
2. 在页面中标注它所依据的英文提交：

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   可通过 `git log -1 --format=%H -- docs/en/<path>` 查得该 sha。
3. **如果该英文页面的某个标题被其他页面通过锚点链接引用**（可在 `docs/en/` 中搜索 `#that-heading-slug` 来确认），不要让翻译后标题自动生成的 slug 改变链接目标——请使用 `attr_list`（已启用）显式固定同一个、与语言无关的稳定 ID：

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   忽略这一点不会导致构建失败，但会静默破坏其他尚未翻译、通过回退机制链接到该标题的页面的锚点滚动定位。
4. 提交 PR——与其他改动一样[进行预览](#pr-previews)，包括语言切换器。

### 截图

无需事先复制任何内容。[`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n) 会对某语言*没有*自有副本的**任何**资源回退到英文文件——翻译页面中的 `../assets/foo.png` 无需修改即可正常工作，显示英文截图，直到在 `docs/<locale>/assets/` 下以相同文件名放入真正的本地化截图，此后该文件便静默覆盖回退。

**`de` 与 `fr` 已经拥有真正的本地化截图**——并非在此处抓取，而是从旧的 [`ethos-manual`](https://github.com/FrSkyRC/ethos-manual) 仓库批量导入的；该仓库中恰好有 FrSky 自己团队早已抓取的、近乎完整的分语言截图集（`german/assets/`，以及法文的 `french_LT/assets/`——它是两套法文资源中较完整的一套，而不是其 README 描述为"完成一半"的较小的 `french/assets/`）。文件名与我们的 `docs/en/assets/` 一一对应，因此导入只是直接复制：当前引用的 589 张截图中有 586 张一次性落位到两种语言，完全无需模拟器参与。少数未能匹配的（2-3 个文件，多为旧仓库宏从未覆盖的较新页面）仍按常规回退到英文。

对于 `de`/`fr` 之外的任何语言，或为补齐最后那几个百分点，抓取新截图意味着要使用[截图流水线](screenshot-pipeline.md)——即移植/运行真实的宏装置来驱动模拟器——因为上游并未完成这部分工作。

### 过期跟踪

[翻译状态](translation-status.md)会在每次构建前自动生成（`hooks/i18n_status.py`，通过 `mkdocs.yml` 的 `hooks:` 接入——在本地、PR 预览和生产环境中同样运行，始终为最新状态，从不提交到 git），它会将每种语言的 `translated_from` 标记与各英文页面实际的最后修改提交进行比对，得出：**current**（最新）、**stale**（英文已更新）或 **missing**（缺失）。该页面即为工作清单——无需 GitHub Issues，也无需翻查 Actions 日志。

### 自动翻译（可选）

`scripts/translate.py` 是一个独立的本地脚本（不属于站点构建或 CI），它将上述缺失/过期工作清单交由 Claude API 处理，为每个页面生成初稿译文，并自动标注正确的 `translated_from:` frontmatter：

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

它默认从 `mkdocs.yml` 的 `i18n` 插件配置中读取所有语言（`--only` 可限定特定语言），除传入 `--force` 外会跳过已是最新的内容，并且从不提交或推送——它只写入 `docs/<locale>/` 下的文件，与手工编辑的效果相同。请审阅差异，对任何新翻译的标题执行[锚点固定](#addingupdating-a-translation)检查，然后照常提交 PR。

系统提示词会预先向 Claude 提供手册的领域背景（FrSky Ethos 遥控器固件，面向 RC 爱好者读者）以及一份绝不可翻译的术语列表（物理按键名称、协议名称、品牌名称），这与姊妹仓库 [`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite) 自身的 `bin/i18n/auto-translate.py` 所用技术相同。法文试点期间确立的术语表已内置到 `fr` 中；当另一种语言有若干页面完成翻译并经过审校后，可按同样方式扩展脚本中的 `GLOSSARIES`。

### 导航标签（`nav_translations`）

`nav:` 中的选项卡与侧边栏标签（例如 "Model Setup"）不会自动采用某语言的已翻译页面标题，除非该导航条目完全没有显式标签（例如 `- how-to/index.md`——此时 MkDocs 会使用该页面自身的 H1）。凡是 `nav:` 中给出了显式的 `Label: path.md` 字符串，或命名了某个章节（如作为带子项的字典键的 `Model Setup:`）之处，该标签都会保持英文，直到 `mkdocs.yml` 中该语言的 `nav_translations` 映射覆盖它——只有当某语言的页面覆盖率足够高、翻译界面框架不会显得与大部分内容脱节时，才为其添加该映射。`fr` 的映射是在法文达到全部页面覆盖后填写的；每个末级标签都是从对应页面自身的译文 H1 逐字复制而来，因此侧边栏文本与页面标题完全一致。
