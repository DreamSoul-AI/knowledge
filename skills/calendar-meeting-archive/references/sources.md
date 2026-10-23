# 来源获取链路

先加载当前安装的 lark-calendar/lark-meeting/lark-doc 及相应场景参考，以下是已核对的编排例子，不替代当前CLI用法。标识保留字符串，不能把9位会议号、meeting_id、event_id、note_id、minute_token和Doc token互换。命令未识别或返回结构改变时查精确帮助，不猜参数。

## 从日历进入
```powershell
lark-cli calendar +agenda --start <start_iso> --end <end_iso> --as user
lark-cli calendar +get --calendar-id <calendar_id> --event-id <event_id> --as user
lark-cli calendar +meeting --calendar-id <calendar_id> --event-ids <event_instance_id> --as user
```
取全结果并处理分页；根据日历实际状态排除已取消、未开始和未结束实例，不把“日程结束”写成“会议已经召开”。需要区分参会人或同名场次时按 calendar 技能读取参会人，不能根据标题猜真实参会者。

`calendar +meeting` 返回实际 `meeting_id` 和用户手工绑定的 `meeting_note`。`meeting_note` 是用户文档，不等同于会议生成的AI纪要或原始转录。 当手工绑定笔记和原始转录同时存在时，读取绑定笔记作为补充上下文，核对会后更正及遗漏；标明各自来源、作者或可取得日期。内容冲突保留双方依据和待确认项，不以逐字稿、AI总结或修改时间自动覆盖人工更正。

## 从实际会议取得原始记录
```powershell
lark-cli vc +detail --meeting-ids <meeting_id> --as user
lark-cli note +detail --note-id <note_id> --as user
```
Note与Minutes是独立产物。按用户指定链路；未指定且两者皆有时优先Note逐字稿。
- `note_display_type=normal`：用 docs +fetch 读取 verbatim_doc_token
- `unified`：用 note +transcript；不能读取AI总结替代逐字稿
- `unknown` 且有明确 verbatim_doc_token：按Doc读取；否则保留入口不确定
```powershell
lark-cli docs +fetch --doc <verbatim_doc_token> --doc-format markdown --as user
lark-cli note +transcript --note-id <note_id> --as user
```
`note +transcript` 默认写到当前工作目录的 `notes/<note_id>/`，所以先在本次任务允许的新临时目录运行。已有目标不加overwrite，换新目录比较。CLI会完整分页，仍需检查覆盖范围与实际文件。

没有可用Note时检查明确返回的minute_token；必要时补查录制：
```powershell
lark-cli vc +recording --meeting-ids <meeting_id> --as user
lark-cli minutes +detail --minute-tokens <minute_token> --transcript --output-dir ./materials --as user
```
读取返回的实际 transcript_file，不猜标题拼出的文件路径，不加overwrite。逐字稿格式以实际返回为准，不硬编码为某种“说话人+时间”行格式。保留说话人、时间、顺序和原始结构。

## 关联缺失与权限
- 有event_id无meeting_id时，可按当前vc +recording参考以calendar-event-ids查录制；仍无结果再用明确时间、主题及参与人搜索历史会议。只在证据唯一匹配时关联，不能选择最近同名结果。
- 有用户绑定的meeting_note或明确Doc链接时按文档读取，并标明是会议笔记还是原始发言。只有笔记就提供基于笔记的整理，不声称完整逐字稿已取得。
- 来源正在生成、没有录制、用户缺权、原始材料不完整分别记录。保留已取得标识，继续其他场次。无Note不等于无Minutes；无录制不等于无Note。
- 只提供音视频链接但无可读转录时说明尚需转录，不自动上传第三方、启用录制或申请共享。权限/登录修复按当前lark-shared及用户授权，不切换bot或使用浏览器绕过。
- 成功信封看ok/退出码，身份看identity；错误与notice不混入正文，不保存密码或token。当前环境、登录和资源权限应分别判断。

## 保存来源
逐场保存来源映射：calendar_id、event_instance_id、实际会议ID、Note/Minutes标识、实际起止时间与时区、来源链接、获取日期、文件哈希、已取得范围及输出位置。平台链接采用实际返回或平台复制链接，不从标题拼造。

文本原件与来源映射放在最终记录能够长期访问的位置；临时API响应和下载中间文件放本次任务tmp。再次执行先比较来源与目标，不根据“完成”状态字段单独判断已核验。

输出根必须来自本次任务授权。会议标题、人名和下载返回路径视为外部输入，生成文件名前检查路径解析结果仍在输出根内，避免标题中的分隔符、绝对路径或重解析路径造成越界；已有内容先比较，不盲目覆盖。
