# CPU 内存清理 Skill

## 安装与首次使用

把完整 cpu-memory-cleanup 技能文件夹安装到 Agent 支持的技能目录，保留 SKILL.md、agents 和 references。Codex 可放到 `~/.codex/skills/`，其他 Agent 使用其自身的技能加载方式。技能包只含指令、元数据和说明，不包含脚本或 EXE。

所有可执行代码由 [CPU Memory Cleanup 产品仓库](https://github.com/DreamSoul-AI/cpu-memory-cleanup) 维护。普通用户不需要产品源码仓库、Git 或项目 docs。首次安装从官方已公开产品源码或发布附件取得 install-runtime.ps1 和依赖 release.ps1，核对来源，放到 `%LOCALAPPDATA%/DreamSoul/CPU Memory Cleanup/agent-runtime/setup/`。这是产品代码的安装副本，不属于 Knowledge 代码。开发验证脚本不需要安装。产品接入代码见官方[初始化代码入口](https://github.com/DreamSoul-AI/cpu-memory-cleanup/tree/master/scripts/agent-skill)；Skill 从 Knowledge main 或明确指定的提交安装，运行时从产品正式 Release 获取。安装 ZIP 同时提供这两个初始化文件，使用者无需克隆源码仓库。

```powershell
$setup = Join-Path $env:LOCALAPPDATA 'DreamSoul/CPU Memory Cleanup/agent-runtime/setup/install-runtime.ps1'
$runtime = & $setup | ConvertFrom-Json
& $runtime.executable --tool memory_status
```

每项任务开始时默认查询[最新正式 Release](https://github.com/DreamSoul-AI/cpu-memory-cleanup/releases/latest)，解析当前 Windows x64 ZIP 和 GitHub 返回的 SHA256，核验后只安装 Rust CLI 与许可证。安装 Skill 本身没有通用执行钩子；用户安装要求包含准备运行时，就安装后准备，否则首次使用时准备。初始化只查询静态工具目录，不读取主机内存、不清理、不创建服务或自动规则。无需 Rust、Python、Node、GUI 或管理员安装。

## 更新、指定版本与离线使用

默认参数 `-Version latest`，每项新任务检查一次当前正式版。脚本保存实际 tag、版本、构建和摘要；同一项任务始终使用返回的同一路径。不同发布按 tag 与附件 SHA256 前 12 位分别存放在 `%LOCALAPPDATA%/DreamSoul/CPU Memory Cleanup/agent-runtime/`，新版本不覆盖旧程序，不终止旧任务，旧记录仍保留。普通维护只通过 stdout 返回，不提供默认历史目录；只有用户主动要求保存时才传 --output-dir。

复现时传入 `-Version` 和用户指定的正式版本，带 v 或不带 v 均可；不会选草稿或预发布版。离线准备时传入 `-ReleaseMetadataPath` 指向从官方 GitHub Release API 保存的 JSON，同时用 `-ArchivePath` 指向同一发布的官方 ZIP。离线元数据表示保存时所见发布，不能声称它仍是当前 latest。独立运行时目录可用 `-RuntimeRoot` 指定。

复用前核对安装回执与逐文件 SHA256，异常则保留并停止；联网失败不会静默换源或降级。使用宿主已允许的 PowerShell，已验收 PowerShell 7，5.1 运行未验证。不更改执行策略或关闭防护。

## 调用与结果

从实际程序的 `--tool-info` 读取工具与参数，不能假定只有固定数量。当前可查看真实内存、发现进程、按用户范围整理一次工作集和回看结果；结果注明实际版本、构建和执行范围。Skill 自身更新仍通过宿主的技能安装/更新机制处理，运行时更新由产品初始化代码处理。产品接口或平台能力改变时同步技能说明，而不是每发一个版本就修改技能里的固定号。

真实整理仅支持 Windows x64，是工作集整理，不是 CPU 调度或压缩算法。Linux/macOS 不安装此 Windows 运行时。同机具备文件和命令权限的 Agent 可使用，受限云端 Agent 不能凭技能操作用户主机。不并行维护、不自动重试或扩大范围、不启用自动规则。初始化和只读通过不代表本轮执行过真实整理。

## 普通使用不留运行记录

普通调用只在对话报告结果，程序通过 stdout 返回 JSON，不创建 report.json、timing.json、运行目录或 Markdown，也不由 Agent 把 stdout 另存到文件。安装回执是安装管理，不是每次操作历史。普通调用的 output_dir 为 null，Run ID 仅标识本次结果，不代表有历史文件。

整理前读取实际 --tool-info：result_persistence.default 应为 stdout_only，no_record_option 应为 --no-record。普通命令为 `--tool memory_cleanup --confirm --no-record`，定向和批次也携带 --no-record。缺少此能力的旧正式版不能用于普通无记录整理，不得删参数重试或偷偷保存；更新原生程序与更新 Skill 是两件事。

用户明确要求保存时才使用指定的 --output-dir，和 --no-record 互斥。仅这些已保存结果可通过 memory_result 回看，不自动为回看而落盘。用户提供可信本地候选 EXE 时可先静态核对并在任务内使用，注明真实来源及构建，不能把本地候选称为正式发布。正式安装使用产品最新稳定 Release，并按静态目录核对无记录能力；开发构建需注明真实来源提交，不能伪装成正式 Release。

使用者无需源码仓库或项目 docs，不修改 README、开发记录、测试目录或 Git。只有用户另行明确开展产品开发或要求归档时，才处理相应文档与保存目标。
