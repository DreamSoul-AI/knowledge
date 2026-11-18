# 阿里云 ESA Pages

用于本次明确 ESA 或 china.provider=esa 的目标。读取[统一配置](configuration.md)，先核对身份，再执行首次发布、同址更新或检查。新配置默认走 [ESA CLI](esa-cli.md)。2026-11-16 已实测控制台首次发布与更新、固定域名和 HTTPS，随后以 CLI 完成既有项目的两次生产发布及同址更新；实际账号、额度及部署结果以当次回执为准。

## 账号、站点与费用

- 控制台入口：[ESA](https://esa.console.aliyun.com/) → 边缘计算和 AI → 函数和 Pages。RAM 登录名与资源主账号 ID 分别核对。账号密码登录成功不代表 Pages、DNS 或证书权限通过。
- 读取项目现状和计算订阅，确认函数和 Pages 可用。仅测试链接发布检查项目创建／更新权限；长期域名再检查站点、绑定、实际权威 DNS 和证书所需权限。记录缺失动作与资源，不默认授予账号级管理员权限。
- 2026-11-16 计算免费订阅标价为 ¥0/月、100 Credits。额度耗尽暂停与订阅到期释放资源是不同条件；官方说明订阅到期停止服务并立即释放资源。逐单记录实际期限和自动续费状态，不把零元订单解释为永久有效；新增订阅按本次授权处理。
- 自定义域名要求账号下已有配置套餐并完成 NS 或 CNAME 接入的可用 ESA 站点。核对套餐、到期、静态额度及超限处理；需要动态函数时另核对计费。新购、续费或超出任务范围的权限变更按本次授权处理。
- 中国内地或全球区域要求域名 ICP 备案；域名注册成功不代表已备案。现有域名在阿里云注册也不代表权威 DNS 一定由阿里云托管。

依据：[RAM 身份](https://help.aliyun.com/zh/edge-security-acceleration/esa/security-and-compliance/identity-management)、[ESA 授权信息](https://help.aliyun.com/zh/edge-security-acceleration/esa/api-esa-2024-09-10-ram)、[站点接入](https://help.aliyun.com/zh/edge-security-acceleration/esa/getting-started/add-your-website-to-esa)、[计费](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/functions-and-pages-billing)。

## 选择发布入口

按[主流程的组织规则](../SKILL.md#esa-demo-组织方式)区分独立 Demo 与实验合集。独立 Demo 使用各自的 Pages 项目和子域名；合集按项目根目录整体部署，实验子目录成为访问路径，不能把某个实验目录当成整个项目上传。核对项目与版本配额，不因额度不足自动覆盖其他项目或升级套餐。

同一根域名下的多个 Demo 优先复用已有可用 ESA 站点，分别绑定子域名并核对各自的 DNS 与证书覆盖，无需每个 Pages 项目再开一个站点套餐。项目独立部署不等于额度隔离：同一计算订阅的项目共用 Credits；站点配置与站点用量封顶会影响该站点下的多个子域名。合集新增路径无需新增 DNS 或证书。依据：[域名绑定](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/trigger)、[计算订阅](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/functions-and-pages-billing)、[用量封顶](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/usage-cap)。

已有本地 HTML、目录或 ZIP：默认按 CLI 流程准备完整静态目录，ZIP 先安全解压。用户明确选择控制台或已有配置为 console 时，可使用“创建 → 本地上传”，无需另建 AccessKey。2026-11-16 控制台支持 ZIP、文件夹、HTML、JS、TS，单次上传不超过 200 MB；只实测纯静态 ZIP，其他类型仍需核对运行时。

CLI 或自动化按 [ESA CLI](esa-cli.md)准备配置和已授权 OAuth profile／临时凭据。AccessKey 查询受限不阻止已配置 OAuth 的用户发布，也不等于控制台不能上传。不要用重新购买套餐、提升为管理员或静默改用控制台来掩盖 CLI 的具体错误。

已有 GitHub 项目：按[官方流程](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/connect-pages-to-github)导入指定仓库，核对仓库授权范围、生产分支、安装命令、构建命令和产物目录。纯静态产物无需引入框架。后续通过同一项目和分支部署；发布到 GitHub 本身应属于本次授权范围。

CLI／GitHub 构建中 `esa.jsonc` 优先于对应控制台构建设置。纯静态项目只配置 `assets.directory`，不为托管静态页面添加函数入口。静态博客和多页 Demo 根据实际需要采用 `404Page`，SPA 才使用 `singlePageApplication`；验证尾斜杠、子页刷新与 404，见[构建及路由](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/build-pages)。纯产物 ZIP 未包含部署配置时，不假定外部 esa.jsonc 会生效；实测未知路径返回平台 404，而非包内自定义 404 页面。

## 首次发布与同址更新

1. 核对公开目录、文件数和体积；官方 Pages 限制与所选入口限制分别核对，本地上传页面当前上限 200 MB。保留完整 V1 产物与摘要。
2. 明确项目名和环境，读取同名资源。首次新建与已有项目更新分别处理；更新目标查不到时停止，不利用 CLI 的自动创建行为另建项目。
3. 控制台首次使用“创建 → 本地上传 → 直接部署”；更新进入原项目“部署 → 重新上传 → 开始构建”。实测两者自动部署 production；若本次目标是 staging，先确认该入口支持选择环境，不能误发生产。回读代码版本、生产发布比例与构建结果，不仅依据上传或构建开始提示。
4. 项目“访问”弹窗提供公共测试链接；保留完整 Token 与生成时间，官方有效期为 60 分钟。分享弹窗完整链接，不复制跳转后已去除参数的地址栏网址。裸域名或过期 Token 不作为长期公开入口。
5. V2 保留同一项目、域名和环境，只更新完整产物；合集先按主流程合入变更并核对旧内容保留。已绑定固定域名时验证原固定入口；尚用测试链接时使用仍有效的完整链接，检查新旧页面、资源与交互，不能只检查新部署专属地址。
6. 状态不明先查询已有部署。失败保留原始错误和上一个可用版本，不反复新建。恢复只有在用户要求时执行，核对目标版本的环境兼容性并再次验收。

依据：[Pages 能力与限制](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/what-is-functions-and-pages/)、[测试域名期限](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/create-pages-by-cli)。

访客校验实测：完整链接首次返回 307，设置同名 esa_er_token 临时访客 Cookie 后跳转到不含参数的页面；这不是阿里云登录会话。HTTP 检查从完整入口开始，仅保留该响应颁发的临时 Cookie，跟随同源跳转后检查页面及资源。HTML 规范化路径还可能再次重定向。全新访客直接访问裸域名返回 401，不将首跳 307 或缺失参数的 401 误报为发布失败。

## 自定义域名与 HTTPS

### 项目与子域名

仅处理已有项目首次绑定、新项目绑定新子域名。使用本次明确的完整子域名，未指定时读取 `esa.domain.name`；域名由使用者配置，模板保持空白。核对账户、可用站点、项目和生产版本，确认目标属于该站点。根域名已注册后，子域名通过 DNS 和平台绑定建立，无需逐个注册；注册商不一定是实际 DNS 服务商。

- 已有项目：查询并确认生产版本，不为单纯绑定重新上传网站。相同域名已绑定同一项目时复用并验收。
- 新项目：检查项目名与子域名未占用；在独立目录配置新项目名，按已授权的新建流程发布完整产物，回读生产部署后再绑定。不要先对尚不存在的项目执行 `domain list` 或 `domain add`。

读取子域名现有解析、用途、TTL、绑定和证书覆盖，保存必要基线。已有其他项目绑定、同名 A／AAAA／CNAME 或业务用途冲突时停止，不覆盖、不解绑。仅请求检查时不创建项目、DNS 记录或证书。域名更换、改绑与旧入口处置不在本流程内。

绑定前分别核对 DNS 记录、ESA 站点、项目及证书配额。2026-11-17 官方[套餐对比](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/package-function-comparison/)列出免费版单站点 100 条 DNS 记录，包含已有记录，不等于还能创建 100 个网站；[使用限制](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/limits-on-using-esa)列出免费账号只能绑定 1 个站点。同一根域名下复用站点、增加子域名记录，与把子域名独立接入为另一个站点不同。实际剩余数量以账户状态为准。

### 站点、绑定与 DNS

尚无站点时，在“站点管理 → 新增站点”添加根域名，按用户指定选择区域、接入方式和套餐。2026-11-16 未备案域名的中国内地／全球选项不可选，“全球（不包含中国内地）”可选。CNAME 接入保留原权威 DNS；在原 DNS 服务商添加页面给出的 `_esaauth` TXT，回到站点点击验证，确认站点已启用后再绑定 Pages。验证值需读取完整内容，不能使用界面的省略文本。

优先通过 [ESA CLI 首次绑定](esa-cli.md#首次绑定子域名)向核验后的项目添加域名；明确使用控制台时，在 Pages 的“域名 → 域名绑定”添加。ESA 会生成站点内部记录，成功后回读域名与项目关系。绑定不等于外部 DNS 或证书已经完成。

| 站点接入方式 | DNS 操作 |
| --- | --- |
| NS | 核对 ESA 自动生成的绑定记录，确认权威解析生效，不再到旧 DNS 服务商添加重复记录 |
| CNAME | 从新增域名的“查看 DNS 记录”读取该域名实际 CNAME 值，在当前权威 DNS 添加对应主机记录；已有完全一致的记录可复用 |

DNS 写入使用该服务已授权的官方工具；域名注册在阿里云不代表阿里云 DNS API 就是正确入口。填写主机记录时核对服务商要求的相对名称或完整域名，避免后缀重复。不同域名的 CNAME 值不能互换，不使用临时测试网址；保留 TTL，等待解析和平台状态同步，超时先查记录与传播情况，不重复创建。首次子域名绑定不需要改变整个根域名的 NS。

若权威 DNS 为阿里云云解析，2026-11-17 官方[记录限制](https://help.aliyun.com/zh/dns/pubz-faq-related-to-domain-name-resolution-resolution-records)为单主域名最多 10 万条解析记录；这是 DNS 配额，与 ESA 的站点记录和项目配额分别检查。未备案限制中国内地加速区域的选择，访客在具体网络是否可达仍需实测。

### 证书与 HTTPS 验收

先检查证书池；已有有效证书覆盖完整主机名时复用，否则在站点“SSL/TLS → 边缘证书”申请覆盖目标的证书。根域名证书不自动覆盖子域名，泛域名覆盖范围需逐一核对。输入框可能自动补全站点后缀，提交前确认完整名称。完成平台要求的 DCV 验证，若签发受阻检查 DNS、CAA 与验证记录；等待异步任务，不重复申请替代排查。[证书和验证规则](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/configure-edge-certificates/)

证书可用后，在无云平台登录的会话中核对证书主机名、信任链和有效期，不跳过 TLS 校验；检查生产版本、CSS／JS／图片／JSON、中文路径、交互、子页刷新和预期 404。HTTPS 正常后，为目标主机开启授权范围内的 HTTP→HTTPS 跳转，验证保留路径及查询参数、无循环；共享站点已有规则先核对影响范围。记录实际访问网络，不把本机通过写成大陆及海外全网验收。

交付项目、完整 HTTPS 入口、绑定／DNS／证书状态和验证结果。只部分完成时明确卡在哪一步，保留已完成资源与原入口；修复本次新增资源须先回读当前状态，不自动删除项目、DNS 或证书。完成首次绑定后，内容更新继续使用原项目和该固定域名。

若 HTML 字节与产物不同，先保留响应并定位具体差异。本次 `/index.html` 出现额外 RUM 性能采样脚本；在“速度和网络 → 速度监测”关闭默认开启的“自适应性能优化”后恢复字节一致。仅在确有此差异且目标需要保留原始页面时处理，不因此关闭 WAF、DDoS 或所有安全防护，也不通过放宽资源校验掩盖差异。

免费站点当次支持零元购买、续费，流量与请求不计费；实际订单期限仍须记录。计算订阅独立核对，不能仅凭收银台通用“ER按量付费”配置标签推定计算免费版被升级。检查真实套餐和实例，不启用未授权增值项。用户要求费用保护时，可设置站点用量封顶；阈值按实际业务确定，停用站点比删除 DNS 更易恢复，但有约 10–15 分钟统计延迟，且影响同一站点下其他子域名。费用预警只提醒，不作为实时扣费上限。

核对证书覆盖、HTTPS 状态、DNS 生效和匿名实际页面。后续更新保留绑定。备案完成后仍需在原站点手动切换加速区域、等待配置生效并从目标网络复验，不自动重建项目或更换网址。依据：[域名配置](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/trigger)、[免费站点](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/free-plan)、[用量封顶](https://help.aliyun.com/zh/edge-security-acceleration/esa/product-overview/usage-cap)。

## 交付

长期交付提供已验证的自定义域名。短时测试链接保留完整参数，注明生成时间、到期时间及用户时区，并标注 60 分钟有效期。记录项目、环境、V1／V2 版本、产物摘要、域名、套餐及实际网络范围。账号详情放私人配置，密码、MFA 密钥、AccessKey、登录 Cookie 与 Token 不进入共享记录或网站。

首次发布、同址更新、匿名访问、跨天回访和大陆网络分别验收。跨天尚未发生时写“待验证”，不以修改本机时间或重新生成 Token 代替。
