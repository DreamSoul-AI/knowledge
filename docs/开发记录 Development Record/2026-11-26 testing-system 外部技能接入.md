# testing-system 外部技能接入

在中英文首页的研发运行分类增加项目测试 `browser-test`，仅保留表格内的一条简介，提供源码、安装更新和使用说明入口及私有仓库权限提示。详细安装步骤、运行条件和调用示例由上游说明维护。

参照现有 Figma 接入方式，[testing-system](https://github.com/DreamSoul-AI/testing-system) 独立维护流程、模板和工具，knowledge 负责发现与安装入口，不复制 Skill 或工具源码。上游当前通过源码目录分发，历史 ZIP 没有对外下载地址，因此安装入口采用上游 [INSTALL.md](https://github.com/DreamSoul-AI/testing-system/blob/main/skills/browser-test/INSTALL.md)，不添加 Release 下载链接。

本轮从同步后的 dev 创建 `feature/add-testing-system`。正式来源采用 testing-system 远端 main，不采用其他本地开发分支中的版本。版本与验证范围见[运行记录](<../运行记录 Run Record/2026-11-26 testing-system 接入验证.md>)。此次只修改目录说明和研发记录；本地审阅确认后，按用户授权提交、推送功能分支并创建合入 dev 的 PR。
