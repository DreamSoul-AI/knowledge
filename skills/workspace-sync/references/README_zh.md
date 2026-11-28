# 工作区同步 workspace-sync

将完整的 `skills/workspace-sync/` 目录安装到当前运行器的技能目录，保留 `SKILL.md`、`agents/` 和引用文件。已有安装先比较并保留定制。

使用：`用 $workspace-sync 更新工作区`。默认更新明确本地目标的规则、模板及已采用能力，保留项目和个人设置并回读。只检查时给预览，不写目标。

需要时直接说“同时更新组织仓库”，或在实际配置中选择 `github_distribution.enabled: true`。从本人已有配置、采用清单取得organization、repo、目标分支和排除项，不要求重新列已知目标。未选择时，即使清单列有多个仓库，也不做远端写入。读取GitHub来源与向GitHub分发分开判断，配置字段不是CLI参数。

远端路径保留原有提交、PR、检查、合并和回读流程；云端和下载包只在本轮另有相应交付要求时进入，不因选择组织仓库就全部执行。结合维护者身份和本轮目标，可简短提示有此选项，默认本地工作继续，不固定增加审批提问。

模板由本技能更新，已采用的技能和工具默认交给 [knowledge-update](../../knowledge-update/SKILL.md)，使用同一轮范围、来源快照和授权。安装本技能时也准备完整的knowledge-update目录，或提供当前可读的入口；不会因此安装所有Knowledge技能。检查模式双方都不写目标，更新模式复用已有采用记录；同轮已经处理的目标直接复用结果。这里不创建每周定时任务。

[技能正文](../SKILL.md) · [English](README.md)

## 可选私有 Git

默认拉模板/规则及接 knowledge-update，不写个人 Git。只有显式选择并配置 private_git.enabled、repo、branch、allowlist 和必要依赖时，才按 [私有 Git 同步](private-git.md) 写入。组织分发独立沿 github_distribution.enabled，清单存在不代表启用。检查模式所有目标只读。配置示例见 [配置](config.example.yaml)。

旧 workspace-update 暂留兼容入口，实际每日任务和组织消费者迁接回读后才删除；不同时调用两份流程。knowledge-update 保留名称，不反向调用。
