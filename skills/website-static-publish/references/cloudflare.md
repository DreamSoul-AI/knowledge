# 海外 Cloudflare Pages

目标为 overseas 或 both 时读取。使用统一 CONFIG.md 中的 cloudflare.* 字段，并先按[配置规则](configuration.md)核对 Account ID、实际登录邮箱、项目与生产分支。部署区域由 Pages 管理，不套用 EdgeOne 区域字段。

## 默认 CLI 发布

默认按 [Wrangler 流程](cloudflare-cli.md)执行：准备固定版本、核验 CLI 身份与目标账户、核对已有项目或本次新建名称、上传完整目录、回读部署并验收生产网址。浏览器只在首次 OAuth 或续期要求时协助授权，不以控制台登录代替 CLI 登录。只有用户明确选择控制台时使用下节；CLI 失败先查具体原因与远端状态，不静默切换入口。

Wrangler 接收目录，不直接接收 ZIP；ZIP 须先按共用流程安全解压。工作目录中的 Functions 和配置可能影响上传，须与产物一起检查。更新显式传入实际生产分支，避免迁移分支被识别为 Preview。

## 控制台发布

1. 在[Cloudflare 控制台](https://dash.cloudflare.com/)确认实际操作者、选定账户和项目权限。注册与邮箱验证由用户完成；不以其他平台邮箱或账户昵称代替实际身份。
2. 新建当前入口为 Workers & Pages → Create application → Continue to Pages → Drag and drop your files / Get started。初始页的 Worker“Upload your static files”不是 Pages；核对类型再继续。同名项目先读取，不覆盖或自动改名。Direct Upload 不能原地切换 Git 集成，但可继续控制台或 Wrangler 更新。
3. 更新进入原账户内原 Pages 项目，选择 Create deployment，确认 Production 或 Preview。生产环境对应云端实际生产分支；预览使用本次明确的其他分支。不得因查不到目标改成新建。
4. 选择完整目录或 ZIP，核对数量、层级与全部上传成功，再执行已授权部署，回读真实状态、部署标识及地址。文件选择器等待较久时先查看已上传状态，不重复部署。输入形式、数量及体积以[Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)和[限制](https://developers.cloudflare.com/pages/platform/limits/)为准。
5. 取得实际生产网址与部署专属网址，不能根据项目名猜测后宣称可用。更新必须验证同一生产入口的新版本。状态未知时先查看已有部署，保持真实错误，不转付费套餐或切平台绕过。

控制台上传不需要 CLI，也不要求建立 Git 或生成长期 API Token；这是用户明确选择的替代入口。

## 发布范围与平台限制

本 Skill 发布预先构建好的纯静态文件，支持多页面、CSS、JavaScript、图片、JSON 与中文路径。它不自动部署 SSR、Pages Functions、Workers、数据库或服务端 API；这属于当前流程的支持边界，并非 Cloudflare 完全不支持后端。浏览器调用已有外部 API 时仍需验收接口可达性、CORS 和公开范围。

以下依据 2026-11-17 核对的 [Pages 限制](https://developers.cloudflare.com/pages/platform/limits/)与 [Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)，发布前应结合实际套餐与 CLI 版本复核：

- 单个静态文件不超过 25 MiB；免费套餐每站点最多 20,000 个文件。控制台拖放入口另有 1,000 文件限制。
- Limits 页列出付费套餐可达 100,000 文件，并要求项目设置 `PAGES_WRANGLER_MAJOR_VERSION=4`；Direct Upload 页仍列 Wrangler 20,000。两份页面对较大目录的说明存在差异，当前流程未验证超出 20,000 的上传，应先核对实际套餐、CLI 能力与平台回执，不自动升级套餐或把付费上限当作当前能力。

  本地固定 Wrangler 4.163.0 源码从上传授权声明的 `max_file_count_allowed` 读取数量上限，缺失时默认 20,000；因此不能把 20,000 描述成该版本在所有账户上的硬编码上限。这是源码核对，未用真实大目录进行额度测试。
- 每账户 Pages 项目上限为 100；新账户前 48 小时另有防滥用的新建限制。项目配额不等于本 Skill 可随意新建的授权。
- Direct Upload 项目不能原地转换为 Git 集成；要使用 Git 集成需另建项目。继续通过 Wrangler 更新原项目不受此转换限制影响。
- 免费套餐的 500 次/月是文档中 Git 触发的构建额度；当前路径上传本地构建产物，不能据此宣称 CLI 只允许发布 500 次，也不承诺无限上传或零费用。

上传前检查文件数、单文件大小与静态边界；超限先报告具体文件或数量。外置大文件、拆分项目、引入 R2 或付费方案需要按本次需求另行处理。已有项目的 CLI 发布与同址更新已实测；CLI 新建、真实恢复、无人值守 CI 和额度边界尚未实测。

## 访客与链接

- 用无 Cloudflare 登录 Cookie 的会话访问普通生产网址，确认 HTTP 状态、目标内容、版本、HTTPS、资源、交互与子页刷新。检查是否启用 Access 等保护；需要登录时分别报告部署成功和公开验收未通过，不自行关闭保护。生产与预览可能不同，见[预览说明](https://developers.cloudflare.com/pages/configuration/preview-deployments/)。
- 交付实际验证的完整可点击生产网址；部署专属／预览网址另列并标明用途。保留平台实际返回的必要参数，不编造 eo_token 或照搬国内链接。
- 普通 pages.dev 地址按项目存续提供服务，没有 EdgeOne 的 3 小时机制，以实际平台状态为准，不承诺永久。若实际取得限时地址则保留全部参数，注明用户时区下生成与到期时间，计算值标为预计，并提醒复制原始完整链接。
- 更新后，普通旧路径和诊断请求可能返回不同缓存内容。分别记录生产域名、本次部署域名及旧部署的验证范围，未验证撤回就不承诺旧内容消失。本机网络通过不代表海外运营商或大陆三网已测。

## 恢复与边界

用户要求恢复时先核对原项目、账户与目标历史生产部署；官方[Rollback](https://developers.cloudflare.com/pages/configuration/rollbacks/)仅支持成功的生产部署，预览部署不作为恢复目标。不可用时可按授权重发保留的完整旧包，随后核对生产指向和实际版本；不编造 Wrangler rollback 或用删除项目代替恢复。

自定义域名、DNS、付费资源、Workers／Functions 后端、Git 集成和无人值守 CI 按实际任务处理。本文路径不会更改未选择的 EdgeOne 目标。
