# 姜胡说skill

基于姜胡说视频转写稿整理的挣钱方法论，供 Codex 按具体任务调用。Skill 标识为 `jianghushuo-money-methods`，保留一个入口和 17 张方法卡。

2026-10-11 修复了杠杆、复利、自有成果和新增交付成本的遗漏，并补上经营模式约束的判断：拒绝逐客户定制，不等于放弃设计、编程等能力。

## 使用

将本仓库根目录中的 `SKILL.md`、`BUILD_MANIFEST.json`、`references/` 和 `resources/` 复制到 Codex 的 `skills/jianghushuo-money-methods/` 目录，然后在对话中调用 `$jianghushuo-money-methods`。

例如：“用姜胡说的方法比较这两个副业，先检查杠杆与复利。一次只问一个问题。”

## 仓库内容

- `SKILL.md`：调用入口与任务路由。
- `references/`：17 张方法卡、概览、术语和索引。
- `resources/sources/`：来源正文、清单及只读查询工具。
- `resources/methods/`：证据、方法筛选、历史验证和本次修复的实际演练记录。
- `source/capabilities/`：恢复并修复后的编译事实源快照，包括 `verified.yaml`、方法卡、概览和显式资源。
- `docs/`：完整性审查、修复说明和安装核对结果。

安装版和编译源一起保存。Git 仓库独立于安装目录，避免安装目录整体更新时丢失版本历史；安装时只复制上面列出的四项。

## 维护与重建

修改编译事实源，再使用 `cangjie-skill` 的 `scripts/cangjie.py` 编译器生成安装版。编译器来自独立的 `cangjie-skill`，本仓库没有打包其运行环境。

```text
python cangjie.py compile --bundle <本仓库>/source/capabilities --out <独立输出目录>/jianghushuo-money-methods --output single
```

Windows 构建进程及子进程需要 `PYTHONUTF8=1`。先检查新输出，再将发布文件同步回本仓库根目录；不要把编译输出目录设为本仓库根目录，也不要只修改生成后的 `SKILL.md`。编译源中的本机绝对路径保留为此次修复的历史信息，重建时以 `--bundle` 指定的实际目录为准。

`.gitattributes` 禁用自动换行转换，以保存来源正文和构建清单的逐字节哈希。

## 验证与边界

本次核对了 17 张方法卡和 57 条精确引文；31 个发布文件与编译源和构建清单一致。完成 13 种不同输入、17 次新版实际任务演练，包含失败、修订和回归记录，详见 `docs/repair-notes.md` 和 `resources/methods/repair-evaluation.json`。

来源可定位、演练可用、现实经营挣钱是三种不同证据。本次没有真实成交或收入试验，不能据此保证收入。修复源由旧安装版恢复，不能称为找回了原始构建目录。
