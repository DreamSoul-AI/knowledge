# 公开网站部署 Public Website Deployment

[English](README.md) | 简体中文

把 HTML、静态目录或 ZIP 发布到阿里云 ESA Pages、Cloudflare Pages，支持首次发布、原网址更新和自定义子域名首次绑定。新配置默认国内 ESA，两端网站上传默认 CLI。

首次使用：安装 Skill → 填写配置 → 完成 CLI 授权 → 检查并发布。以后复用配置和登录更新同一项目。

## 常用请求

安装配置完成后，直接向 Agent 发送请求。将路径、项目名和网址换成实际值：

```text
使用 $public-website-deployment，检查 ./dist 和发布配置，列出缺项，不上传。
```

```text
使用 $public-website-deployment，把 ./dist 更新到 ESA 已有项目 my-demo，验证原网址。
```

```text
使用 $public-website-deployment，把 ./dist 更新到 Cloudflare 已有项目 my-site，验证原网址。
```

```text
使用 $public-website-deployment，把同一份 ./dist 更新到配置中的 ESA 和 Cloudflare 项目，分别验证原网址。
```

新建时明确说“新建项目”并指定名称。ESA 独立 Demo 使用独立项目和子域名；小实验可加入已有合集的稳定路径。合集更新需基于当前完整站点保留其他实验，详见 [Demo 组织方式](../SKILL.md#esa-demo-组织方式)。

首次绑定可以直接说：

```text
使用 $public-website-deployment，为 ESA 已有项目 my-demo 首次绑定 tools.example.com，完成 DNS 和 HTTPS 验收，不重新上传网站。
```

```text
使用 $public-website-deployment，将 ./dist 发布为 ESA 新项目 my-new-demo，并首次绑定我指定的新子域名 lab.example.com。
```

```text
使用 $public-website-deployment，为 Cloudflare 已有项目 my-site 首次绑定 showcase.dreamsoul.cn，完成 DNS 和 HTTPS 验收，保留 pages.dev 入口。
```

子域名由使用者提供；`showcase.dreamsoul.cn` 是展示示例，使用时替换为自己的子域名。新 Cloudflare 项目同样明确说“新建项目”、给出名称和子域名。详细步骤见[首次绑定](#首次绑定自定义子域名)。

## 安装与运行条件

当前正式版 1.2.0 从 knowledge 的 [main 分支](https://github.com/DreamSoul-AI/knowledge/tree/main/skills/public-website-deployment) 安装完整目录。原名称依次为 `website-static-publish`、`public-website-publish`，现统一使用 `public-website-deployment`，功能范围保持不变。Agent 需要文件读写、命令执行和浏览器授权能力。安装请求：

```text
将提供的 public-website-deployment 安装到当前项目的 .agents/skills/。
复制完整技能目录，排除真实 CONFIG.md 和私人文件，并保留随包 LICENSE。
已有安装先备份并保留配置。此次只安装。
```

使用分发包时保留包内许可证。安装后核对实际加载路径和版本；未识别时重新打开会话。工具按所选平台准备：

| 工具 | 版本与用途 |
| --- | --- |
| Node.js / npm | 实测 Node.js 24.18.0；Wrangler 4.163.0 要求 ≥22.12.0，ESA CLI 要求 ≥18 |
| 阿里云 CLI | ESA OAuth 使用 3.5.3，按[官方说明](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)安装并加入 PATH，运行 `aliyun version` 核对 |
| ESA CLI | 1.0.14，负责 ESA 上传 |
| Wrangler | 4.163.0，负责 Cloudflare Pages 上传 |

复用已有固定版本；缺少工具时，在部署工作目录执行所需的一行：

```powershell
npm install --prefix .artifacts/esa-cli --save-exact --ignore-scripts --no-audit --no-fund esa-cli@1.0.14
npm install --prefix .artifacts/wrangler --save-exact --ignore-scripts --no-audit --no-fund wrangler@4.163.0
```

将 `.artifacts/` 加入网站项目的忽略规则，工具目录与公开 `dist/` 分开。以下 PowerShell 命令使用这些本地安装路径；占位值先替换，检查通过后再执行发布。

## 首次配置

将 [assets/CONFIG.example.md](../assets/CONFIG.example.md) 复制到实际加载的 Skill 根目录，命名为与 `SKILL.md` 同级的 `CONFIG.md`。目标已存在时保留原文件。只修改“值”列，保留字段名、表头和全部字段行。

| 字段 | 填写方式 |
| --- | --- |
| `schemaVersion` | 保持 `2`，表示配置格式版本；Skill 当前版本为 1.2.0 |
| `default.target` | 默认 `china`；可选 `overseas`、`both`、`ask`，分别表示海外、双端、未指定时询问 |
| `china.provider` | 新配置保持 `esa`；china 选择平台路线，实际加速区域另按 ESA 站点核对 |
| `esa.project.deployMethod` | 默认 `cli`；已有 console／github 值在普通升级时保留 |

本次明确的平台、项目和环境优先于默认配置。Cloudflare 默认使用 Wrangler，当前配置表无需增加发布方式字段。只填写所选平台需要的值；登录后从以下来源核对：

| 平台 | 必填信息与来源 |
| --- | --- |
| ESA 身份 | `esa.account.ramLogin` 填官方 RAM 登录名，`esa.account.ownerId` 填资源主账号 ID；用 RAM 资料及 `aliyun sts GetCallerIdentity` 的 AccountId、Arn 核对 |
| ESA 项目 | `esa.project.name` 填已有项目名，`environment` 填 `production` 或 `staging`；从项目列表核对。CLI 方式的 `productionBranch` 可留空 |
| ESA 长期网址 | `esa.site.*` 填站点 ID、名称、实际区域和 `ns`/`cname` 接入方式；`esa.domain.name` 填用户自己的完整子域名，不含协议和路径，本次明确值优先。短时测试可留空 |
| Cloudflare 身份 | `cloudflare.account.id` 填 32 位 Account ID，`email` 填实际操作者邮箱；从 `whoami --json` 核对，Account ID 与 Zone ID 分开识别 |
| Cloudflare 项目 | `cloudflare.project.name`、`productionBranch`、`environment` 分别填已有 Pages 项目、云端实际生产分支、`production`/`preview`；Preview 另指定预览分支 |

可选备注和未使用平台的账号、项目留空。完整字段与旧配置迁移见 [configuration.md](configuration.md)。

Cloudflare 自定义子域名直接在本次请求中指定，配置格式仍为 2，不新增字段。绑定还需要相应的域名、DNS 与证书管理权限；发布登录不自动提供这些权限。本次新项目和域名不会自动覆盖 CONFIG.md 中的默认项目。

`CONFIG.md` 保存账号标识和业务默认值。登录与凭据由官方工具管理：阿里云 OAuth 在本机 `~/.aliyun/config.json`，Wrangler 使用自己的用户配置。CLI 路径和 OAuth profile 名称通过命令传入；密码、密钥、Cookie、Token 不写入配置表或公开产物。

## ESA 首次授权与使用

**1. 授权。** RAM 管理员安装 `official-cli` 应用并允许发布用户访问；该用户还需目标 ESA 资源的操作权限。执行：

```powershell
aliyun configure --mode OAuth --profile my-esa-profile
aliyun sts GetCallerIdentity --profile my-esa-profile
```

选择账号所属的中国站或国际站，完成官方网页授权及 MFA。核对 RAMUser、资源主账号 AccountId 和 Arn 中的用户名，后续复用该 profile。手动浏览器授权见 [OAuth 认证](esa-cli.md#oauth-认证)。

**2. 准备目录。** 构建完整静态产物到 `dist/`，在其同级创建 `esa.jsonc`：

```json
{"name":"my-demo","assets":{"directory":"./dist"}}
```

更新前保存当前线上完整产物，保留已有路由和域名。首次新建需可用 ESA 计算服务；长期网址需完成站点、DNS 和 HTTPS 配置，见 [ESA 流程](esa.md)。

**3. 核对项目。** 固定参数填一次，后续查询和发布复用。`--user` 填 RAM 用户名部分，`--cli` 使用绝对路径：

```powershell
$esaRunner = '<Skill目录>/scripts/esa-cli.mjs'
$esaArgs = @(
    '--profile', 'my-esa-profile',
    '--account', '<资源主账号ID>',
    '--user', '<RAM用户名>',
    '--cli', (Resolve-Path '.artifacts/esa-cli/node_modules/esa-cli/bin/enter.cjs').Path,
    '--cwd', '<部署工作目录绝对路径>'
)
node $esaRunner @esaArgs -- project list --keyword my-demo
node $esaRunner @esaArgs -- deployments list
node $esaRunner @esaArgs -- domain list
```

后两条查询读取工作目录的 `esa.jsonc`，用于已有项目。更新前确认原项目存在且环境和域名正确；查不到目标时先处理，不转为新建。明确新建时先用 project list 检查名称未占用，跳过尚不存在项目的部署和域名查询，再按本次授权执行 deploy；生产版本成功后首次绑定子域名。

**4. 发布并回读。** 以下命令会更新 production：

```powershell
node $esaRunner @esaArgs -- deploy --name my-demo --assets ./dist --environment production --description release-001 --no-preview
node $esaRunner @esaArgs -- deployments list
```

随包脚本验证身份和临时 STS，再调用官方 CLI。`--no-preview` 省略临时预览链接，适用于已有固定域名；需要短时测试链接时按 [ESA CLI 流程](esa-cli.md)处理。

## Cloudflare 首次授权与使用

**1. 登录。** 在工具安装目录取得 Wrangler 绝对路径，检查 CLI 身份：

```powershell
$wranglerPath = (Resolve-Path '.artifacts/wrangler/node_modules/wrangler/bin/wrangler.js').Path
node $wranglerPath --version
node $wranglerPath whoami --json
```

未登录时执行一次授权，然后再次运行 whoami 核对邮箱和账户：

```powershell
node $wranglerPath login --browser=false --scopes account:read user:read pages:write
node $wranglerPath whoami --json
```

在命令生成的官方网页完成授权，等待 CLI 返回。4.163.0 自动加入 `offline_access` 供续期，`--scopes` 只填写上面三项。

**2. 选择账户和项目。** 切换到本次纯静态部署工作目录，检查其中的 Wrangler 配置、`functions/` 和 `_worker.js`，排除其他项目配置及后端入口。设置本次账户并查询：

```powershell
$previousAccountId = $env:CLOUDFLARE_ACCOUNT_ID
$env:CLOUDFLARE_ACCOUNT_ID = '<已核验的 Account ID>'
node $wranglerPath pages project list --json
```

核对原项目及其实际生产分支。模板中的 `main` 按云端实际值填写；更新项目查不到时先处理。明确要求新建且名称可用时，使用 [project create 命令](cloudflare-cli.md#新建与更新)创建。

**3. 发布并回读。** 以下命令会上传完整目录，生产环境使用项目的实际生产分支：

```powershell
node $wranglerPath pages deploy '<完整产物目录绝对路径>' --project-name my-site --branch '<实际生产分支>'
node $wranglerPath pages deployment list --project-name my-site
```

完成或中止后，在同一终端恢复原账户环境变量；自动化调用用 `try/finally` 保证恢复：

```powershell
$env:CLOUDFLARE_ACCOUNT_ID = $previousAccountId
```

Wrangler 接收目录，ZIP 先解压。单文件上限 25 MiB，免费站点上限 20,000 文件；付费额度、项目数量和 Direct Upload 模式限制见 [Cloudflare 参考](cloudflare.md#发布范围与平台限制)。

## 首次绑定自定义子域名

支持已有项目首次绑定、新项目发布成功后绑定新子域名。已有相同绑定直接验收；目标被其他项目或业务使用时停止。本流程不更换域名、不改绑项目、不跳转或停用旧入口。

**ESA：配置目标 → 绑定 → DNS → HTTPS。** 使用 `esa.domain.name` 或本次指定值，复用可用站点。先确认项目已有生产版本，并核对站点、现有绑定和 DNS；已有项目只做绑定时不重新上传。复用前文 `$esaRunner`、`$esaArgs`：

```powershell
$esaDomain = '<用户配置的完整子域名>'
node $esaRunner @esaArgs -- site list
node $esaRunner @esaArgs -- domain list
```

无冲突且尚未绑定时执行：

```powershell
node $esaRunner @esaArgs -- domain add $esaDomain
node $esaRunner @esaArgs -- domain list
```

项目由 `$esaArgs` 的 `--cwd` 下 `esa.jsonc` 决定。NS 接入核对自动生成的记录；CNAME 接入把平台返回的实际目标写入当前权威 DNS。复用覆盖子域名的有效证书，或按平台要求申请并验证；证书正常后检查 HTTPS 和 HTTP 跳转。完整步骤见 [ESA 域名流程](esa.md#自定义域名与-https)。

**Cloudflare：发布项目 → Custom domains → CNAME → HTTPS。** 网站仍通过 Wrangler 发布；首次域名绑定在已核验账户的 Workers & Pages → 目标项目 → Custom domains → Set up a domain 中填写本次子域名。随后在权威 DNS 添加指向该项目实际 `pages.dev` 地址的 CNAME，等待域名及证书激活，再验证网站。仅写 DNS、不在 Pages 中绑定是不完整的。详见 [Cloudflare 域名流程](cloudflare.md#首次绑定自定义子域名)。

域名可在阿里云等注册商购买。Cloudflare 子域名接入可保留原 DNS 服务商；根域名直接接入需另行处理 NS，不包含在本次子域名流程中。两端均核对记录、域名绑定、项目和证书配额；子域名数量不等于可创建的网站数量，当前限额及来源见各平台参考。绑定后交付实际 HTTPS 入口与验证结果，保留已有入口及配置。2026-11-17 已完成 ESA 新项目绑定新子域名、Cloudflare 已有项目首次绑定的线上验收；具体范围见 [验证状态](../SKILL.md#验证状态)。

## 发布前检查与访问验收

1. 按网站现有命令构建，核对入口、资源、路由和额度。仅上传公开静态目录，排除私人配置、凭据和日志；后端、SSR 或 Functions 需求另行确认。
2. 更新保留当前线上完整产物；双端复用同一份目录，分别认证、发布和验收。上传报错或状态未知时先查询远端记录，再决定是否重试。
3. 用未登录平台的访客会话检查原生产网址的新版本、HTTPS、CSS／JS／图片／JSON、主要交互、中文路径、子页刷新和预期 404。合集逐个检查新旧实验。
4. 交付各端实际网址、版本、项目／环境、部署记录和访问结果，记录实测网络。ESA 长期使用已验证的自定义域名，Cloudflare 使用原生产网址；ESA 短时测试链接按[交付规则](esa.md#交付)附完整参数及生成／到期时间。

以后更新：重新构建完整目录 → 复用原项目、环境和域名发布 → 验证原网址。使用内容哈希或版本化资源引用减少新旧资源混用。平台执行细节见 [ESA CLI](esa-cli.md)、[Wrangler](cloudflare-cli.md)，完整规则见 [SKILL.md](../SKILL.md)。

## 目录与职责

| 源码位置 | 用途 |
| --- | --- |
| `SKILL.md` | 调用入口与共用执行规则 |
| `agents/openai.yaml` | 界面元数据 |
| `assets/CONFIG.example.md` | 空白配置模板 |
| `references/` | 中英文指南、字段规则和平台流程；EdgeOne 参考用于旧配置兼容 |
| `scripts/esa-cli.mjs` | ESA OAuth 接续 |
| `scripts/esa-cli.test.mjs` | 接续脚本测试 |
| `.gitignore` | 忽略同级私人 CONFIG.md，随安装保留 |

真实 `CONFIG.md` 在安装后创建于 Skill 根目录。网站产物、CLI、日志和验证输出放在部署工作目录。维护时运行 `node --test "<Skill目录>/scripts/esa-cli.test.mjs"`。

## 升级与验证范围

升级前备份整个安装目录到技能发现目录之外的私人位置。更新指引、元数据、模板和脚本，保留真实 CONFIG.md；schema 变化按[迁移规则](configuration.md#迁移与保留)处理。旧布局中的根 `CONFIG.example.md` 和 `tests/scripts/esa-cli.test.mjs` 已迁至 assets 和 scripts，核对并保留本地修改后移除旧副本。

新模板默认 china；已有 ask、both、overseas 和 ESA console／github 值继续保留。需要改默认 ESA 时设置 `default.target=china`、`china.provider=esa`，配置格式仍为 2。

独立安装或打包时保留随包 MIT LICENSE。检查文件清单，排除 CONFIG.md、USER.md、凭据、日志、截图、私人备份和平台 CLI 安装包；`.gitignore` 保护新文件，打包和已跟踪文件另行核对。

2026-11-17 已用 1.2.0、ESA CLI 1.0.14 和 Wrangler 4.163.0 完成两个已有项目的同站发布、原网址更新及访客验收；随后完成 ESA CLI 新建项目绑定新子域名、Cloudflare 已有项目首次绑定及双端 DNS、证书和访问验收。ESA 资源版本问题通过版本参数修正，部分连接超时经重试完成核验。Cloudflare CLI 新建、绑定后的再次同址更新、合集发布、恢复、无人值守 CI、跨天和目标地区网络仍待验证；完整状态见 [验证状态](../SKILL.md#验证状态)。
