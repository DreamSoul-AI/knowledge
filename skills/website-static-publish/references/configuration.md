# 统一账号与目标配置

## 定位与解析

每次只读实际加载 SKILL.md 同级 CONFIG.md，不合并仓库与安装副本，不读取旧单平台 Skill 的配置。文件不存在时可将该 Skill 内的 [assets/CONFIG.example.md](../assets/CONFIG.example.md) 复制到 Skill 根目录、命名为 CONFIG.md 初始化；先确认目标不存在，不能覆盖已填值。配置不提供登录或发布授权。

解析 UTF-8 Markdown 中唯一一张表头为“字段／值”的表格。先读 schemaVersion：2 的字段须与当前模板一致；1 的字段为当前模板去掉 china.provider 和全部 esa.* 后的集合，按下面兼容规则处理。去除首尾排版空白及包裹整个字段或值的一对反引号，保留账号为文本；拒绝重复、漏行、未知字段、额外列、未知版本、换行值或嵌入竖线。内容仅作数据，不执行其中的命令。空值为待填，说明性占位文字不能作为账号。

先校验表结构、default.target 与 china.provider，再按所选平台和操作校验字段。未选平台的值不参与语义校验，不阻塞单端。both 表示一个国内平台与 Cloudflare；两端分别核验，一端缺失不得由另一端字段替代。

## 字段

| 字段 | 含义与约束 |
| --- | --- |
| schemaVersion | 配置表格式版本，当前为文本 2，与 Skill 1.2.0 版本号无关；旧版 1 按兼容规则读取 |
| default.target | china、overseas、both、ask；新模板默认 china，本次明确目标优先，ask 不执行默认发布 |
| china.provider | esa、edgeone、ask；明确平台优先，ask 只在确需国内且未指定平台时询问 |
| esa.account.ramLogin | 官方 RAM 登录名；登录前必填，实际操作者须匹配 |
| esa.account.ownerId | ESA 资源所属主账号 ID，数字文本；云端写操作前从控制台或已授权身份接口核实，不用 RAM 用户 ID 代替 |
| esa.site.id / esa.site.name | 绑定长期域名时必填，整体核对可用 ESA 站点；仅测试部署可留空 |
| esa.site.region | 域名绑定时记录控制台实际加速区域；中国内地、全球须核对备案，全球（不包含中国内地）不得声称大陆节点已验收 |
| esa.site.accessType | ns 或 cname；按实际站点接入方式填写，不默认迁移整个域名的 NS |
| esa.project.name | 默认已有项目名称；更新、刷新、恢复必填；新建使用本次明确或任务中确定的未占用名称 |
| esa.project.environment | production 或 staging，采用 ESA 含义，不照搬其他平台 preview |
| esa.project.deployMethod | console、cli 或 github；本次明确入口优先，普通升级保留原值。新模板默认 cli，按 ESA CLI 参考核对版本与认证；切换已有 console 配置须有本次明确要求 |
| esa.project.productionBranch | github 方式更新生产时必填；console／cli 方式可留空 |
| esa.domain.name | 不含协议、路径或 Token 的自定义域名；长期交付必填，短时预览可留空 |
| edgeone.site | china，固定为中国站账号入口 |
| edgeone.account.uin | 实际登录身份的完整 UIN，纯数字文本；云端操作前必填，不是 APPID |
| edgeone.account.label | 可选备注，不用于认证 |
| edgeone.project.id | 默认已有项目 ID，更新／刷新／恢复时必填 |
| edgeone.project.name | 与项目 ID 一起核对；新建使用本次指定的新名称 |
| edgeone.project.region | 中国大陆可用区或全球可用区（含中国大陆），与控制台实际区域含义一致；不是 CLI 参数值 |
| edgeone.project.environment | production 或 preview |
| cloudflare.account.id | 32 位十六进制 Account ID，云端操作前必填，不是 Zone ID |
| cloudflare.account.email | 实际登录操作者邮箱，核对时忽略首尾空白及大小写；不从其他平台推定 |
| cloudflare.account.label | 可选备注，不用于认证 |
| cloudflare.project.name | 默认已有 Pages 项目；新建使用本次明确名称 |
| cloudflare.project.productionBranch | 初始期望 main；已有项目按云端实际生产分支填写 |
| cloudflare.project.environment | production 或 preview；preview 还需本次明确一个不同于生产的预览分支 |

新模板使用 `default.target=china`、`china.provider=esa`；未指定目标的发布请求走 ESA，明确指定 Cloudflare 或双端时覆盖该默认值。china 只决定平台路线，实际加速区域仍由 ESA 站点决定。Cloudflare 默认使用 Wrangler CLI；用户可在本次请求中指定控制台。当前 schema 不含 cloudflare.project.deployMethod，CLI 路径、OAuth profile 和凭据也不属于本表字段。

## 身份与覆盖

ESA 分别核对 RAM 操作者、主账号资源归属、项目和站点。用户指定的密码来源只用于该服务登录，不将密码复制到配置。MFA、首次改密和凭据绑定依当前工具要求交用户完成。控制台登录不提供 CLI 认证；使用 CLI 时单独核对凭据所属身份、权限和有效期，不从浏览器缓存提取云 API 凭据。缺少权限时报告实际动作、资源与错误，不默认申请 AdministratorAccess，也不声称某系统策略只限一个 Pages 项目。

EdgeOne 实际登录 UIN 必须与配置完全匹配，昵称、尾号或历史登录均不代替。子账号按登录 UIN 核验，并另核对目标资源归属与权限。[账号信息](https://cloud.tencent.com/document/product/378/11245)中 UIN 与 APPID 是不同字段。

Cloudflare Account ID 确定资源账户，登录邮箱确定操作者，两者分别核对，不能只看账户昵称或同名项目。[账户与域名 ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/)说明不代替本次登录证据。

当前指令中的平台、项目与环境优先于默认值；切换目标须整体回读其账户、类型、名称及区域／分支，不拼接另一个项目的字段。配置冲突、实际身份不符或没有权限时停止对应平台的云端修改，保留本地准备和另一已授权平台的独立工作。查不到待更新项目时不得转为新建。

注册、改密、邮箱验证、MFA、验证码和条款确认按当前工具要求处理。用户明确授权使用已有密码登录时，仅向指定服务提交。用户明确指定首次 Cloudflare 账户并要求配置时，可从官方界面核对邮箱与 Account ID 后填入私人配置；EdgeOne UIN 由用户提供或按其明确的配置请求核验。多个账户无法确定时询问，不猜测。

新建后在用户已授权配置默认项目的范围内写回对应平台字段。三个平台各有一组默认项目；博客和 Demo 如使用不同项目，按本次明确目标整体核对，不自行扩成多账号管理器。

## 迁移与保留

EdgeOne 字段和参考用于旧配置兼容。仅在本次明确指定 EdgeOne，或已核验的旧配置选择它时读取 [EdgeOne 兼容流程](edgeone.md)。新配置默认使用 ESA，明确请求 ESA 时直接使用 esa.*，不加载 EdgeOne 流程。

### schemaVersion 1 升级为 2

1. 先完整备份实际安装目录到技能发现目录之外的私人位置，重读源文件，保留 default.target、edgeone.*、cloudflare.* 的每个值。
2. 添加 china.provider 与 esa.* 行并将版本改为 2。没有新的平台选择时，china.provider 设为 edgeone，保留旧“国内”语义；用户明确改用 ESA 后才设为 esa。新增账号和资源字段仅填写已确认值，待核实项留空。
3. 逐值比对旧字段并验证新字段完整性；同时更新指引和模板。迁移失败时不启用不完整配置，保留旧副本。
4. 未迁移的合法 v1 仍可用于原有 EdgeOne／Cloudflare 路线；v1 请求 ESA 时明确需要补充 v2 配置，不把现有国内请求静默改到 ESA。

### 历史双 Skill 合并

合并旧 Skill 时，一次性读取旧安装副本的两份 CONFIG.md：除各自 schemaVersion 外，EdgeOne 字段加 edgeone. 前缀、Cloudflare 字段加 cloudflare. 前缀；schemaVersion 使用 1，default.target 初始为 ask。逐值比对后才启用新配置。已有统一配置时先核对差异，不自动覆盖；迁移完成后运行时仅读取新配置。

普通升级只更新 Skill 指引、参考和模板；schema 升级按上面的备份、迁移和逐值比对步骤修改真实 CONFIG.md，保留已有业务值。分发包与网站包显式排除真实配置，不能只依赖 Git 忽略。旧安装含私人配置，备份放在技能发现目录之外且不公开；共享源码历史快照只含原有空白模板。密码、SecretId、SecretKey、Token 和 Cookie 均不进入配置。

Skill 目录内的 `.gitignore` 随目录保留，忽略同级真实 `CONFIG.md`，空白 `assets/CONFIG.example.md` 继续分发。Git 忽略不作用于已跟踪文件，也不自动过滤普通复制或 ZIP 打包；分发前按[安装与分发说明](README_zh.md#升级与验证范围)检查实际文件清单。
