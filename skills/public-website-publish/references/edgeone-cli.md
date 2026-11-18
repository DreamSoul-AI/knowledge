# CLI 接续说明

仅在本次需要命令行发布且环境具备相应能力时阅读。2026-11-06 已核对官方参考，但本项目尚未安装 EdgeOne CLI、配置 API Token 或执行 CLI 发布；以下不是实测完成声明。

## 官方流程与本项目适配

参考[官方部署 Skill 固定版本](https://github.com/TencentEdgeOne/edgeone-makers-tools/blob/e6ead945373c8dc56dca91d3e586e3c7cccd0079/codex/makers-deploy.md)（自报版本 2.12.4）和[当前 CLI 文档](https://pages.edgeone.ai/zh/document/edgeone-cli)。复用官方 CLI，不自行实现底层上传 API。

- 先按[配置读取规则](configuration.md)解析账号和本次目标，包括本次明确覆盖默认值的情况。CLI 与控制台共用同一配置和身份核验条件；读取配置不是 CLI 认证。本节的 EdgeOne 路线面向中国站，命令显式传 `--site china`，不采用出口 IP 猜测。
- 使用 `edgeone -v`、`edgeone whoami` 和 `edgeone makers deploy --help` 检查当前版本、身份和实际参数。官方固定版本要求非交互认证部署 CLI 至少为 1.6.0；执行时还须核对当前帮助，不自动升级项目依赖。
- 复用已经工作的登录方式；需要登录时使用官方浏览器流程，保持中国站。不要从任意账号缓存中搜索 Token，也不要让用户把密钥粘贴进聊天。
- 官方部署参考支持预先注入 `EDGEONE_PAGES_API_TOKEN`；这是账号级凭据，不能宣称只控制单项目。使用环境已有的凭据管理方式，不把 Token 写入仓库或公开产物。
- 纯静态发布无需 `makers init`、函数目录、Blob 或 KV。不要为了部署生成无关后端能力。

## 命令示例

以下为 PowerShell 模板，会真实发布到已核验的已有项目。在网站项目根目录运行，替换产物路径；Codex 先读取统一 Skill 同级 `CONFIG.md` 的 edgeone.* 字段，完成字段校验，并通过控制台等只读方式核对实际 UIN、项目 ID、名称、区域、直接上传类型及目标环境，再把本次目标的项目名和环境填入下方变量。CLI 本身不会读取 Markdown，不能对 `CONFIG.md` 使用 `ConvertFrom-Json`。空值检查只防止漏填，不代替身份与目标核验。**`-n` 指定名称不存在时会自动创建项目**；更新时若无法确认目标存在且 ID 一致，停止该次更新，不能试运行部署来检查。本次使用另一目标时按读取规则先解析整个目标。

```powershell
$env:PAGES_SOURCE = 'skills'
$eoPublishPath = '.\publish\site'
$eoProjectName = '' # 填入从 CONFIG.md 读取并经云端核验的本次项目名称
$eoEnvironment = '' # 填入本次已核验的 production 或 preview
if ([string]::IsNullOrWhiteSpace($eoProjectName) -or
    $eoEnvironment -notin @('production', 'preview')) {
    throw '请先完成 CONFIG.md 和实际身份／目标核验，再填写项目名称与环境。'
}
edgeone.cmd makers deploy $eoPublishPath -n $eoProjectName -e $eoEnvironment --site china --json
if ($LASTEXITCODE -ne 0) {
    throw 'EdgeOne 发布失败；保留原始错误，检查部署记录后再决定是否重试。'
}
```

`edgeone.cmd` 是 Windows npm 入口；其他系统使用当前环境实际的 `edgeone` 可执行文件。上例假定已认证，不传入明文 Token。新建项目且 CLI 区域参数未核实时使用控制台明确选区，不依赖默认区域；已有项目更新不顺便改区。

## 读取结果与核验

固定版本官方参考说明 `--json` 在标准输出最后一行返回对象。先确认进程正常结束，再按实际输出解析，不把进度行当 JSON。成功需核对 `status`、`url`、`projectId`、`deploymentId` 和 `consoleUrl`；字段缺失、目标不匹配或状态不明时不宣称已完成。

完整保留返回 `url` 的查询参数，再按主 Skill 做独立访客验证。CLI 退出码为 0 不能代替页面检查。若只需更新过期预览链接，回到控制台刷新，不为了取链接重新部署。

官方参考的匿名认领流程、整套技能安装命令及要求用户保存 Token 的步骤不属于本 Skill 默认范围。控制台同项目更新已实测；域名、CI、通过 CLI 更新与恢复的实测由后续任务补齐。
