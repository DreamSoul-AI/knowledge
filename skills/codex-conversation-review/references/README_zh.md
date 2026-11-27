# Codex 对话回顾

按指定会话和范围读取公开原始记录，解释讨论目标、转折、决定、纠正及未完事项。默认直接回复，不生成 Markdown、归档版本或上传。整体回顾覆盖完整指定对话，局部问题按指定主题读取，不扩成全账号扫描。

## 读取本地记录

需要 Python 3.8+，无第三方依赖。使用完整 review 技能目录即可独立运行，不依赖 archive。先取得当前或指定会话 ID，用已知会话目录定位文件名，再核对 session_meta。缺失或多份来源应先确定对象。

可用 skill-installer 安装 [codex-conversation-review](https://github.com/DreamSoul-AI/knowledge/tree/main/skills/codex-conversation-review)，保留完整目录。需要完整原文归档时，再安装 archive 并将两者放在同一技能根。技能下个回合可用，当前对话是否重新加载应另行核对。

```text
python <review技能目录>/scripts/review.py --source <会话.jsonl> --session <会话ID> --limit 40
```

只有会话 ID 和已知会话目录时可将 `--source` 换为 `--sessions-root <目录>`。脚本仅按该 ID 匹配文件名，不搜索其他聊天正文。指定文件和 ID 不一致、未知来源或记录类型会报错，不静默省略。

首轮返回 `through_id`、`source_prefix_sha256`、`total_items` 和 `next_offset`。后续每页带同一 `--through-id`、`--expect-prefix-sha256` 和返回的 `--offset`，直到 `next_offset` 为 null。消息页为原话，不是语义摘要；工具结果按需用 `--view records` 读取，记录页有自己的总数与 offset，不能混用两种游标。可用稳定 ID 和 source_line 核对消息与对应工具。

每页重新读取同一个会话文件，未实现字节偏移加速。固定截止后新增消息不会混入，已读前缀变化则停止。调用者需要记录完整工具原件时使用 records 视图或 Python `records.prepare` 的全部 events，不能只传消息页给 archive。源码中的未知格式、缺失时间、未完成行和附件边界见 [记录适配](record-format.md)。

## 回顾与归档

按 [回顾组织](review-standard.md) 阅读和解释，关键结论用消息时间、ID或来源行定位。脚本只提供完整公开记录和时间依据，不替 Agent 自动判断哪些决定有效，不生成隐藏思路。

需要保真归档时，archive 调用 review 取得完整记录及单独回顾，再保存原话、工具、时间与校验。两个完整目录默认同放一个技能根；不同位置使用 archive 的 `--review-skill` 指定。依赖方向只从 archive 到 review，更新旧安装时同时核对两个完整包与实际读取位置。

包内原始记录可能包含个人或业务信息，不因回顾自动复制到其他会话、提交或上传。实际阅读及输出按当前授权执行。
