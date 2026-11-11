# 数据适配与验证边界

脚本将完整行读取、phase 筛选、ID 去重、原文位置校验、转达解析及工具调用与返回分离集成在包内，不依赖外部样本脚本。

- 只处理 session_meta 确认的指定会话。公开 message 来自 response_item；不同时导出 event_msg 镜像，避免重复。
- 用户发言和正式回复的时间来自原始 `response_item.timestamp`，默认转为北京时间显示，可用 `--utc-offset` 指定显示时差。原始字段仍保留在 archive.json；时间行位于原话校验范围外，不改变正文或来源顺序。缺失、无时区或无效时间明确标注，核对报告保留警告。
- `event_msg` 中的 task_started、task_complete、turn_aborted 仅用于时间依据，以 turn_id 和 started_at 核对轮次，不复制其中的消息镜像。耗时仅使用非负整数 duration_ms，一轮只有一条正式回复且原生完成记录已在截止点以内时才显示完成耗时。中断耗时只标在该轮最后一条用户消息处，缺失的生命周期不推算。timing.json 保存来源行、原始时间、轮次、原生耗时及显示值，和正文一起参与版本哈希。
- 用户消息通过 `content_item_kinds` 中的 `user.text` 识别。规则注入和环境、打开页面等已知上下文不视为用户原话；显式调用技能产生的 `skills.selected_skill_instructions` 属于系统提供的技能上下文，单独排除，不冒充用户发言。无法识别的用户来源停止并提示，不静默丢弃。
- Goals 的 `goal.internal_context` 和 `user.goal` 仅在来源为 harness 且正文具有对应 `codex_internal_context` 包装时作为自动上下文排除，并计入 exclusions。直接用户发言仍按 `user.text` 保留，未知类型、混合未知类型、来源或包装不匹配继续停止。
- 确认回复中的 `send_user_message_question_reply` 包装按字面原文使用 text 代码围栏，避免导入器将其作为 XML 标签移除，标签、反斜杠和换行仍逐字符核对。
- assistant 的 commentary 属于公开进度，final_answer 属于正式回复。reasoning 不输出。未知 phase 停止。
- 已观察到的 configuration_update 仅含 reasoning 配置时排除；agent_message 仅在作者与接收方为内部 Agent 路径、元数据明确来自 collaboration 工具时作为内部协作记录排除，并分别计入 exclusions。伴随页面的 codex_apps_selected_page_part_N_of_M 上下文作为 injected_context 排除。未知形状或来源继续停止，不把内部协作或页面上下文当作用户发言或正式回复。
- 两种工具调用族 custom_tool_call / function_call 及其 output 按原顺序保留。转达 XML 从 function_call_output 提取 input 和 source_thread_id，保留独立来源与边界，不冒充用户直接发言；不把整段工具返回重复显示为转达正文。
- 消息正文按 content 分段顺序连接，不 strip、不改链接、不修错别字。附件平台包装单列；用户消息附带的非文字内容仅记录类型，不宣称已取得原始附件。工具图片仅记录类型，不导出 data URL、图片编码或隐藏推理。
- 用户与正式回复若自带会改变归档层级的 H1 至 H4 标题、Setext 标题或未闭合代码围栏，对有结构冲突的整条消息使用长度足够的 text 代码围栏。围栏内文字原样保留，校验报告标记这种展示降级；普通正文、列表、表格和已闭合代码块保持原有排版。不要为统一样式改写原话。
- 公开进度添加引用前缀并转义 Markdown 控制符，反向还原后逐字符校验。较长工具参数与返回保存于 tools.json；主文档引用完整记录，并显示实际返回的退出码、截断提示和异常输出，未取得的错误原因不补写。
- 最末未换行的 JSONL 行留待下次读取；完整行 JSON 错误停止。已归档 ID 的内容或顺序变化、历史记录消失时停止，旧版本保留。
- archive.json 是筛选后的公开记录，不复制原始 JSONL，避免把 reasoning、系统配置与凭据上下文整份归档。
- 增量以全部已读公开记录为依据去重，首次实现仍会重读单个文件，不是按字节 offset 加速。新版本以内容哈希命名，通过原子替换 current.json 提交；崩溃留下的未提交版本不代表归档成功，成功重跑可复用相同版本。

本地 JSONL 属于当前已观察格式，不承诺其他 Codex 版本、云端或远程会话兼容。来源已截断的工具返回、记录外的附件、被删除历史和压缩前已缺失的消息不能恢复。原话一致性校验只覆盖实际可取得的输入，不等同于再次通过 UI 全量比对。
