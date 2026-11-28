# 定时任务

[English](README.md) | 简体中文

这里维护可复用的定时任务提示词和配置示例。任务通过已安装的 Skills 处理内容，通过对应工具访问平台。实际调度、账号授权和运行状态由使用者环境维护。

## 任务总表

| **任务** | **参考安排** | **定义状态** | **验证状态** | **入口** |
| --- | --- | --- | --- | --- |
| 定时会议总结 scheduled-meeting-summary | 由部署者配置频率、时间及时区 | 首版 | 手动核验通过，新增写入及触发待覆盖 | [说明](scheduled-meeting-summary/README_zh.md) / [提示词](scheduled-meeting-summary/prompt.md) / [配置](scheduled-meeting-summary/config.example.yaml) |
| 定时电子邮件总结 scheduled-email-summary | 由使用者配置 | 首版定义 | Outlook 只读及摘要格式已验证，其他平台及调度待验证 | [说明](scheduled-email-summary/README_zh.md) / [提示词](scheduled-email-summary/prompt.md) / [配置](scheduled-email-summary/config.example.yaml) |
| 定时工作区同步 scheduled-workspace-sync | 由部署者配置频率、时间及时区 | 首版定义 | 整轮只检查已验证，更新、刷新及触发待验 | [说明](scheduled-workspace-sync/README_zh.md) / [提示词](scheduled-workspace-sync/prompt.md) / [配置](scheduled-workspace-sync/config.example.yaml) |

总表登记本仓库实际存在的任务定义，后续新增任务继续加行，维护其目录和验证状态。参考安排不代表任务已启用，运行账号、承载聊天、平台任务标识和部署状态留在各使用者环境。

当前任务复用 Calendar Meeting Archive、Meeting Minutes 和 Document Sync，增量整理已结束会议。2026年11月15日按新版入口手动执行，实时扫描来源、核验已有稿并比较云端现状，复用已有成果、保留冲突及缺项。本轮没有需要新生成的材料，未为验证重生成或上传副本。新生成及写入、实际定时触发等未覆盖分支继续注明，旧部署的成功不替代新版证据。详见 [本轮运行记录](<../docs/运行记录 Run Record/2026-11-15 定时任务与共享资源验证.md>)。

每项任务在自己的目录维护中英文说明、`prompt.md` 和 `config.example.yaml`。提示词负责调用和衔接，会议内容规范、去重及传输细节继续维护在对应 Skills 和项目规范中。

使用时，把示例配置复制到实际项目的本地配置位置，填写身份核验依据、资料入口、归档位置和状态路径。个人配置、凭据、任务及聊天标识、运行锁、回执和真实会议资料留在运行环境。发布前检查分发清单。

启用、替换或调整现有任务前，核对现有任务、承载位置、时区、范围和已授权动作，并继承旧成果及进度。每次部署单独验证。仓库文件用于准备任务，实际启用通过调度平台完成。


迁接：旧 daily-* 目录改为 scheduled-meeting-summary、scheduled-email-summary、scheduled-workspace-sync。已有任务只迁接定义引用，保留个人调度、状态路径与覆盖游标，不因新目录复制出一套新状态。本次改定义不自动修改实际任务。

旧 daily-* 的提示词仅作兼容转接，正式定义和配置以本表为准。选择自然日报告时，按实际计划触发上下文和业务时区确定前一日；人工日期优先，补漏仍沿旧成功进度接续。
