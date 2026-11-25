# 飞书授权复用

[中文](README_zh.md) · [Skill](../SKILL.md) · [English](README.md)

调用 `$lark-auth-reuse` 核对已有授权、实际运行身份和失败原因。需要当前环境已有 `lark-cli` 与 `lark-shared`；完整安装本技能后，它提供诊断和接续流程，不另存凭据。

**同一台机器上的多个对话可以复用已有授权**。前提是它们调用 CLI 时使用同一实际系统用户、应用、profile 和可访问的凭证环境。换一个对话本身不要求重新扫码。工作区约定可以统一检查和调用方式，但不会改变操作系统的凭证访问权限。

本指南配合当前环境已有的 `lark-shared` 技能和 `lark-cli` 使用，不新增登录技能、凭证服务或安装步骤。业务操作继续读取对应的飞书技能，并遵守本次任务的读写授权。

## 正常时直接复用

在本次任务获准的运行环境中检查已有登录：

```powershell
lark-cli auth status --json --verify
lark-cli whoami --as user
```

核对服务端验证结果、实际用户及 token 状态。显示 `user` 但 token 为 `missing`，不能算用户身份已可用。代表用户执行后续业务命令时显式指定 `--as user`，不要依赖自动选择身份。

身份与 token 可用时，直接沿已有登录调用。CLI 负责有效 token 复用及其支持的续期，不为每个对话保存另一份令牌。某个资源可读，只说明本次身份能读取该资源，不代表其他资源或写入操作也已获准。

## 显示 missing 时先核对环境

先取得实际进程身份及必要的非敏感配置信息：

```powershell
[System.Security.Principal.WindowsIdentity]::GetCurrent().Name
lark-cli --version
$larkReuseConfig = lark-cli config show | ConvertFrom-Json
$larkReuseConfig | Select-Object profile,profileSource,workspace,brand,appId
```

这些字段用于本机比较，部分版本或配置可能没有全部字段。只展示实际需要的选择字段，不打印完整配置、`appSecret`、token 或其他密钥。对外提交诊断结果时进一步去除真实账号、应用及 profile 标识。

**环境变量不等于实际进程身份**。`USERNAME`、`USERPROFILE` 等字符串即使相同，进程也可能以不同 Windows 用户运行。配置文件可读，也不代表该用户能读取已有凭证。

若实际身份或凭证访问环境不同，保留两边的非敏感诊断结果。需要使用既有用户凭据时，按执行工具正常审批流程，在已获准、凭证可用的环境中运行相应命令，说明具体任务及读写影响。获准后重新核对身份，只接续必要的失败调用，避免重复已成功的写入。

不要复制注册表或令牌、关闭隔离、静默改用 bot，或让所有命令无条件提升权限。也不要先注销或反复扫码来处理运行身份差异。

## 分清授权与资源权限

| 实际情况 | 检查方向 |
| --- | --- |
| 应用或 profile 不同 | 当前项目采用的配置和身份 |
| 同一环境仍 missing 或刷新失败 | 已有登录状态及具体错误 |
| 用户有效但缺少 scope | 应用范围和用户同意范围 |
| 用户有效但资源拒绝访问 | 目标资源的访问权限 |

**应用范围**，是应用在平台后台获准调用哪些接口。**用户同意范围**，是用户授予该应用的授权范围。**资源权限**，是该用户对具体文档、表格等对象的访问权。三者分别核对，不能用重新扫码替代资源授权处理。

只有确实需要新增用户授权或已有登录无法恢复时，才沿当前 `lark-shared` 的增量授权流程处理所需业务域或 scope。由 Agent 展示当次生成的授权链接与二维码，用户完成后接续。不复用过期链接，不默认申请全部权限。应用配置问题及资源权限问题按实际责任方处理，不擅自更换账号或扩权。

## 机制与验证范围

核对 `lark-cli` 1.0.93 官方实现可见，用户凭证按应用和用户标识定位，不按聊天 ID 分开保存。Windows 后端使用当前用户的 HKCU 和 DPAPI，因此实际 Windows 身份会影响凭证读取。见 [凭证定位](https://github.com/larksuite/cli/blob/v1.0.93/internal/auth/token_store.go) 和 [Windows 凭证存储](https://github.com/larksuite/cli/blob/v1.0.93/internal/keychain/keychain_windows.go)。其他版本应核对对应实现。

本次已在同一机器的两个独立正常进程中验证相同应用、profile 和用户身份，两者均通过服务端身份核验，并读取同一既有资源。另一受限进程的实际 Windows 身份不同，无法访问相应凭证环境，报告 `missing`。全程未新登录、注销、复制凭据、修改权限或写入业务资源。

官方 [用户 token 调用与刷新实现](https://github.com/larksuite/cli/blob/v1.0.93/internal/auth/uat_client.go) 支持有效 token 复用及需要时的刷新，并用账户锁协调。此次实跑开始时 token 均有效，续期机制仅作源码核对，未验证真实过期、并发刷新或长期失效恢复。

以上支持同机独立进程复用，不能据此声称所有桌面聊天已自动选择正确运行环境。跨设备、其他系统用户及其他应用或 profile 的共用也未验证。使用时先核对当前实际身份，再按具体错误接续，避免不必要的重复授权。
