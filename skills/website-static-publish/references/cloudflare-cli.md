# Wrangler CLI 发布

Cloudflare 默认读取本流程；本次明确选择控制台时改读对应入口。工具缺失按下文准备。2026-11-17 已使用 Wrangler 4.163.0、Node.js 24.18.0 完成 OAuth 认证、既有 Pages 项目发布、原网址更新和访客验收。CLI 新建项目、恢复和无人值守 CI 仍未实测。

## 准备与身份

复用项目已固定的 Wrangler 和包管理器，先检查版本及相关子命令帮助；工具缺失时按[官方安装说明](https://developers.cloudflare.com/workers/wrangler/install-and-update/)安装到合适的本地工具范围，不默认全局安装或升级网站依赖。使用现有认证；需要 OAuth 登录时由用户完成官方授权，不从浏览器导出 Cookie。

没有既定工具时，可在部署工作目录中安装已验证版本；该目录须排除在网站产物和 Skill 分发包之外：

```powershell
npm install --prefix .artifacts/wrangler --save-exact --ignore-scripts --no-audit --no-fund wrangler@4.163.0
node .artifacts/wrangler/node_modules/wrangler/bin/wrangler.js --version
```

下文的 `wrangler` 表示已核验的入口；本地安装时使用 `node "<wrangler/bin/wrangler.js 的绝对路径>"` 替换它，不依赖全局命令或裸 npx 下载。

以下为已安装 Wrangler 时在 PowerShell 中的只读入口：

```powershell
wrangler --version
wrangler whoami --json
wrangler pages project list --json
```

先从 whoami 核对实际邮箱及账户，再按 统一 CONFIG.md 的 cloudflare.account.id 选择账户。多账户时在本次进程中显式设置 `CLOUDFLARE_ACCOUNT_ID`，退出操作时恢复原值；不把该环境变量当作认证。项目列表需匹配目标名称、生产分支和实际账户。参数以已安装版本帮助为准，不支持 --json 时读其普通输出，不编造字段。

本轮固定版要求 Node.js >=22.12.0。首次 OAuth 可执行 `wrangler login --browser=false --scopes account:read user:read pages:write`，由用户核对并确认官方授权。该版本自动附加 `offline_access`，不要把它作为 `--scopes` 参数，否则会被拒绝。授权等待超时后重新运行命令，使用新生成的链接；不复用失效回调，也不把授权链接、一次性代码或令牌写入共享记录。控制台登录与 Wrangler 登录分别核验。

## 新建与更新

[Pages 命令](https://developers.cloudflare.com/workers/wrangler/commands/pages/)为官方执行入口：

- 新建仅在已授权且确认不存在目标项目后执行 `wrangler pages project create <项目名> --production-branch <生产分支>`。
- 上传执行 `wrangler pages deploy <完整产物目录> --project-name <已核验项目名> --branch <本次目标分支>`，产物目录使用实际绝对路径，不传 ZIP。
- 生产分支取云端实际值；预览使用明确的其他分支，不用 `--env production` 代替 Pages 分支选择。
- 执行前检查工作目录中的 Wrangler 配置、functions/ 及 `_worker.js`，避免附带上传后端或读取其他项目配置；必要时在隔离的纯静态工作目录执行。
- 上传前按[范围与限制](cloudflare.md#发布范围与平台限制)核对目录文件数和单文件大小，不能把整站限制误写成只支持单页，也不把尚未核验的付费额度当作保证。
- 上传后用 `wrangler pages deployment list --project-name <项目名>` 回读状态与部署记录，随后回到 SKILL.md 的访客验收，不把 CLI 退出码当作全部访问检查。

账号 Token 的权限、保存和 CI 注入需要独立设计，不为一次上传生成长期凭据。未知状态先查询部署记录，不能连续重复发布。恢复优先使用经过核验的官方控制台恢复操作，或按用户要求重发保留包；不编造 Wrangler rollback 子命令。

身份命令依据：[General commands](https://developers.cloudflare.com/workers/wrangler/commands/general/)。只读核对和真实部署必须分别记录执行结果。
