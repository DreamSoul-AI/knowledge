---
name: cpu-memory-cleanup
description: 在 Windows 上初始化 CPU 内存清理工具、读取真实内存和进程，并按用户指定范围执行一次工作集整理或回看结果。用户说内存清理、内存压缩或使用此工具时适用；当前能力是工作集整理，不提供 CPU 调度、压缩算法或远程主机控制。
---

# CPU 内存清理

使用已发布的 Rust CLI，不另写清理脚本。只支持同机 Windows x64；其他平台不安装此运行时，不将只读版本或动画当成清理。只读能力与实际维护分别按用户任务使用。

## 初始化

本 Skill 由 Knowledge 维护指令、元数据和安装说明，不携带可执行脚本或产品二进制。所有代码由 [CPU Memory Cleanup 产品仓库](https://github.com/DreamSoul-AI/cpu-memory-cleanup) 维护，包括 `scripts/agent-skill/install-runtime.ps1` 和开发验证用的 `test-runtime.ps1`。

日常使用不要求源码仓库、Git、项目 docs 或开发目录存在。优先使用已经安装到当前用户目录的初始化副本。默认位置是 `%LOCALAPPDATA%/DreamSoul/CPU Memory Cleanup/agent-runtime/setup/`，只需产品的 install-runtime.ps1 及其依赖 release.ps1，不安装或运行开发验证脚本。

首次没有初始化副本时，从官方产品仓库的已公开源码或发布附件取得上述两个文件，核对来源并记录版本或源码 commit，缓存到当前用户目录。代码仍由产品仓库维护，用户目录只是安装副本；不把脚本放回 Knowledge，不要求克隆整个产品仓库，也不向用户的当前项目写入。初始化代码由官方产品仓库维护，可从[初始化代码入口](https://github.com/DreamSoul-AI/cpu-memory-cleanup/tree/master/scripts/agent-skill)取得。下载时记录实际源码提交；引导脚本不固定运行时版本，正式运行时仍解析 latest 或用户指定版本。

每项用户任务开始时调用已安装的初始化脚本一次，默认解析官方最新稳定 Release，核对附件 SHA256 后安装或复用。不要在 Skill 中固定产品版本、构建或摘要；需要复现时传入 `-Version`。同一任务使用同一返回路径。

```powershell
$setup = Join-Path $env:LOCALAPPDATA 'DreamSoul/CPU Memory Cleanup/agent-runtime/setup/install-runtime.ps1'
$runtime = & $setup | ConvertFrom-Json
$exe = $runtime.executable
```

脚本把不同 tag/附件摘要的运行时分别部署到当前用户目录，保存实际版本、构建、来源和逐文件摘要。重复使用先核对已装文件，再通过静态 `--tool-info` 检查身份；发现变化时保留并报错，不直接运行或覆盖。新任务会重新检查 latest，不终止旧任务或覆盖旧运行时。下载失败不能静默降级；离线准备使用已保存的官方 Release 元数据和对应 ZIP，见[使用说明](references/README_zh.md)。

使用宿主已允许执行脚本的 PowerShell 环境，本 Skill 实测 PowerShell 7；5.1 兼容语法的运行尚未验证。不得通过 Bypass、更改执行策略、关闭防护或内联重写绕过限制。运行产品 CLI 不需要 Python、Node、Rust、管理员安装、MCP 或桌面窗口。

安装 Skill 本身没有通用程序执行钩子。用户安装请求明确包含准备运行时，就在安装后初始化；否则首次使用时初始化。初始化不会读取真实内存、清理、打开 GUI、创建服务或自启任务。默认运行位置及离线安装参数见[使用说明](references/README_zh.md)。

## 普通调用不保存运行记录

普通调用只把结果 JSON 返回 stdout，再在对话汇报。不要传 --output-dir，不创建运行目录，不保存 report.json、timing.json、Markdown 或额外回执，不把 JSON 重定向到文件；也不修改源码仓库、用户当前项目、README、开发记录、测试目录或 Git 状态。安装回执用于核对安装完整性，和每次操作的运行记录分开。

维护前检查所选程序 --tool-info 中的 result_persistence：default 必须为 stdout_only，no_record_option 必须为 --no-record。普通整理命令携带 --no-record。旧版缺少此能力时停止维护并说明需要支持无记录的构建；不能删掉参数重试、改传保存目录，或先写文件再删除。只读接口仍可按实际能力使用。

用户明确要求保存本次原始报告时，才使用其指定的 --output-dir，并去掉 --no-record；只有这种结果才支持 memory_result 历史回看。正常无记录结果的 output_dir 为 null，Run ID 只标识本次返回，不意味着已保存。不要为了回看而自动开启保存。

用户明确提供可信本地构建路径时，先通过该文件 --tool-info 核对版本、构建与无记录能力，并在本次任务中使用该路径，不用正式初始化把它换回旧版。注明这是本地候选，不能冒充官方 Release。没有指定路径时走默认正式发布初始化。始终核对实际能力，不能把只改了 Skill 当成已经更新原生程序。

即使用户说“测试一下 Skill”，也不自动写开发文档或持久化运行结果；明确开展产品开发或指定归档时才按相应范围处理。既有历史文件不因本规则自动删除。

## 使用已有工具

使用该任务初始化返回的绝对 `executable` 路径调用 CLI。读取该运行时的 `--tool-info` 核对实际工具、参数、平台能力和确认要求，不能假定工具数量永远不变。下表是当前接口映射；若所需工具缺失或合同改变，先按对应产品说明适配，不猜参数或擅自换成其他范围。不把用户输入拼成 shell 代码。其他同机 Agent 也可执行此过程，宿主必须具备文件和命令执行权限。

| 用户任务 | 工具 |
| --- | --- |
| 看真实内存 | `--tool memory_status` |
| 列进程、定位目标 | `--tool memory_targets` |
| 整理一次全局工作集 | `--tool memory_cleanup --confirm --no-record` |
| 整理一个指定进程 | `--tool memory_process_cleanup --pid <PID> --created-at <本次发现的身份> --confirm --no-record` |
| 整理明确目标批次 | `--tool memory_batch_cleanup --request-file <UTF-8 JSON> --confirm --no-record` |
| 回看已有结果 | `--tool memory_result --run-dir <返回的output_dir>` |

批次 JSON 为 `{"targets":[<memory_targets返回的目标对象>],"protections":[]}`，不要用占位值执行。单目标需传本次发现的 PID 和原始 created_at，不按名称猜 PID，也不在失败后换目标或改为全局。

用户明确要求本次整理时即可执行该范围一次，不重复询问已明确的信息。只要求安装、查看状态或列进程时不整理。范围不清而会改变受影响应用时先明确范围。不要将“安装了 Skill”当成日后自动整理授权，不添加定时规则，不自动重试部分失败。

维护前确保本工具没有另一项在途维护，不与网页/应用按钮并行整理。现有 localhost 会话可通过 `api/session` 和带 `X-Session-Token` 的 `api/state` 核对 busy 与 rule.armed；存在在途动作或规则时先停止本次派发，不擅自关闭用户任务。CLI 的互斥只在实例内，不保证跨进程全局互斥；其他 Agent 也应遵守相同边界。

维护结果取 UTF-8 stdout 的完整 JSON，即使退出码为 1 也要解析。0 表示完整成功，1 表示 partial/failed/unknown/cancelled，2 表示参数或入口错误。对话报告实际版本、成功/失败/跳过计数与前后快照；普通调用 output_dir 应为 null，不报告不存在的历史路径或调用 memory_result。不能只凭退出码丢弃已发生动作，再自动重试。

## 解释结果

报告系统可用量的前后净差与目标工作集事实，注明 partial。工作集下降是驻留减少，不是删除数据、压缩分配量或保证 CPU 提速，后续访问会重新驻留。用户说“CPU 内存压缩”时说明实际能力后按其内存整理意图处理，不声称工具会清理 CPU。

产品发布见[最新正式 Release](https://github.com/DreamSoul-AI/cpu-memory-cleanup/releases/latest)。Knowledge 不复制产品代码；产品新增正式版不要求重写 Skill 的版本号，接口、平台能力或初始化合同改变时再同步技能说明。每次结果应注明实际版本与构建，不能把 latest 当成可复现的版本标识。
