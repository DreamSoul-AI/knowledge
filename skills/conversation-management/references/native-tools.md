# 原生工具与边界

调用前发现当前环境对应工具并读取实际 schema。以下为本轮可用接口的关键参数，不是自建 CLI，也不保证其他宿主提供同名能力。

| **目的** | **工具与实际参数** | **注意** |
| --- | --- | --- |
| 列项目 | list_projects({}) | 返回项目身份与仓库信息，不能证明对话 cwd |
| 列对话 | list_threads({limit, mode, source, hostId, archived, cursor}) | recent 含置顶 UI 顺序；history 按 source/host/归档状态分页，不把第一页当全部 |
| 读目标 | read_thread({threadId, hostId, includeTurns:false}) | 先取元数据，必要再开 includeTurns 与游标读相关任务；不承诺不存在的 cwd 字段 |
| 移项目 | move_thread_to_project({threadId, projectId, hostId, source, beforeThreadId}) | beforeThreadId 只用于手动排序项目；同 host，远程对话不能移成无项目 |
| 恢复分区位置 | move_thread_to_sidebar_section({threadId, sectionId, beforeThreadId, hostId, source}) | sectionId 使用实际返回值；pinned 为置顶，原顺序用有效相邻锚点恢复 |

source 取工具支持的 codex/chatgpt，Codex host 使用实际返回值，不硬编码本机。projectId:null 的移出能力仅在平台允许且本次授权时使用。调用时只传当前模式适用参数，不把全部表中参数机械塞进每次调用。

move_thread_to_project 对新源目录的访问不提供额外授权；若工具提示必须由用户在侧栏移动，报告这个实际限制，不反复调用。工具返回成功后仍回读项目和分区。

handoff_thread({threadId, destinationHostId?, followUpPrompt?}) 是另一种会影响 Git/执行位置的操作；不能移动调用者自身，运行目标可能被中断。普通项目归属修正不调用它。若本次另有明确授权，读取其最新说明并用 get_handoff_status 按返回 revision 核对完成状态。

Git 只读核对可在明确目标目录使用 git rev-parse --show-toplevel、git remote -v、git worktree list --porcelain。对另一对话，这些只能证明被检查目录的身份，不能冒充该对话当前实际 cwd。不要读取应用内部状态来绕开工具缺失。
