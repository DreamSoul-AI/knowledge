# testing-system 接入验证

## 环境与来源

2026-11-26，Windows PowerShell、Node.js v24.18.0。knowledge 工作区原有规划已移出，开始时工作区干净。执行 `git fetch origin dev`、`git switch dev`、`git merge --ff-only origin/dev`，将 dev 快进至 `b67925c46264a9d18ee23fd1a315f0832dbe5753`，随后创建 `feature/add-testing-system`。同步后核对 AGENTS.md、REPO.md 的规则变化与首页当前分类。

通过 `git ls-remote` 核对 testing-system 远端 main，并在忽略目录 `.tmp/add-testing-system/upstream/` 浅克隆同分支，取得提交 [7bb113a3d4ff20e9b661681d09dc68c95a0ce9ae](https://github.com/DreamSoul-AI/testing-system/tree/7bb113a3d4ff20e9b661681d09dc68c95a0ce9ae)。没有修改现有 testing-system 工作区。

读取该提交的 README、安装说明、Skill 入口、界面元数据、版本分发说明和清单。清单标识 Skill `2026.11.20.6`、公共工具 `0.1.1`、契约 `test-evidence/1`。安装说明要求 Node.js 24.x 或不低于 22.12.0 的 22.x，完整安装 `skills/browser-test`。历史 ZIP 属本地材料，没有对外下载地址。

## 已执行检查

在 knowledge 根目录，对暂存的上游源码执行：

```powershell
node .tmp/add-testing-system/upstream/skills/browser-test/scripts/verify.mjs
node .tmp/add-testing-system/upstream/skills/browser-test/scripts/paths.mjs
node .tmp/add-testing-system/upstream/skills/browser-test/scripts/testing-cli.mjs help
```

文件清单和 SHA-256 校验通过，包含清单在内共 46 个文件。内置位置检查和 CLI 帮助入口通过，回执保存在 `.tmp/add-testing-system/`。这些结果只证明暂存目录的完整性和入口可调用。

本轮文档检查脚本为 `.tmp/add-testing-system/check.cjs`，核对五份变更文档的 UTF-8、标题、围栏、冲突标记、本地相对链接、中英文新增上游链接一致性，以及新增上游链接在固定提交中的实际目标。检查通过。默认 `git diff --check` 将原有 CRLF 风格的新增行识别为行尾空白；保留首页既有换行格式，按 `git -c core.whitespace=cr-at-eol diff --check` 复查通过。双语说明已按上游安装要求人工核对。

## 验证边界

未安装或更新用户现有 browser-test，未执行真实项目测试、完整上游自测或跨平台验证。上述本地验证阶段未提交、推送或创建 PR；后续提交与 PR 按用户审阅后的授权办理，不包含合并或发布。README 使用 main 入口便于获取正式来源，以上固定提交仅标识本轮核验基线。新增入口需要 testing-system 私有仓库访问权限，不代表所有 knowledge 读者均可访问。
