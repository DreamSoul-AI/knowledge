# ESA CLI 发布

ESA 新配置默认使用官方 [aliyun/alibabacloud-esa-cli](https://github.com/aliyun/alibabacloud-esa-cli)。CONFIG.md 提供业务默认值；阿里云 CLI 的 OAuth profile 管理认证；项目工作目录中的 esa.jsonc 管理公开产物。三者不混放秘密，也不把默认项目当作所有新 Demo 的上传目标。

## 固定版本与服务状态

2026-11-16 实测版本为 **esa-cli 1.0.14**、阿里云 CLI **3.5.3**，Windows／Node.js 24.18.0。ESA CLI 要求 Node.js >=18；沿用项目符合要求的工具链。需要安装时放到项目临时目录，固定版本，不通过裸 npx 拉取未知版本。例如：

~~~powershell
npm install --prefix .artifacts/esa-cli --save-exact --ignore-scripts --no-audit --no-fund esa-cli@1.0.14
node .artifacts/esa-cli/node_modules/esa-cli/bin/enter.cjs --version
node .artifacts/esa-cli/node_modules/esa-cli/bin/enter.cjs deploy --help
~~~

1.0.13 只用 GetErService 的 Running 状态判断可用性，新版 Credits 计算订阅可能返回 NotOpened，即使项目和网站正常仍被拒绝。1.0.14 官方修复先查询 GetSubscriptionPlan；Purchased=true 通过，明确未购买时才检查旧服务。遇到此报错先核对已安装版本、订阅和接口返回，不重买套餐或删除校验。自定义 RAM 策略若缺 esa:GetSubscriptionPlan，仅报告该具体动作；老服务还需 esa:GetErService。根据实际错误处理权限，不默认申请管理员权限。

依据：[npm 固定版本](https://www.npmjs.com/package/esa-cli/v/1.0.14)、[官方更新记录](https://github.com/aliyun/alibabacloud-esa-cli/blob/master/CHANGELOG.md)。安装包内 CHANGELOG 与源码用于核对该固定版本，滚动网页不代替本机验证。

## OAuth 认证

优先复用用户为本任务授权的官方阿里云 CLI OAuth profile，不额外创建持久 AccessKey。已有完整环境 STS 组也可直接执行官方 ESA CLI。密码／MFA 用于浏览器登录，不是 ESA CLI 凭据；不从任意浏览器缓存提取密钥。

首次接入由主账号或已有 RAM 管理员安装官方 CLI 应用，并把目标 RAM 用户加入允许访问身份。只给应用分配该用户，不给共享用户增加 RAM 管理员权限。随后在用户本机执行：

~~~powershell
aliyun configure --mode OAuth --profile my-esa-profile
aliyun sts GetCallerIdentity --profile my-esa-profile
~~~

浏览器核对官方应用、RAM 登录名和请求范围，按当前工具规则完成用户授权／MFA。CLI 3.5.3 可用 --no-browser 手动打开本次命令生成的登录 URL；回到 http://127.0.0.1:12345/cli/callback 后页面拒绝连接是手动模式预期现象，把完整回调交回原命令完成配置。回调含一次性授权码，不进入共享记录。OAuth 配置保存在本机 ~/.aliyun/config.json，不拷入网站、仓库或 Skill。

每次执行前核对 GetCallerIdentity 的 RAMUser、AccountId 与 Arn 中用户名，分别对应 CONFIG.md 的 ownerId 和 ramLogin 的用户名部分。主账号、其他用户或归属不符时停止。官方 CLI 负责 profile 刷新；需要重新登录时由用户完成，不把失效凭据降级为其他身份。

依据：[官方 CLI OAuth](https://help.aliyun.com/zh/cli/oauth-credentials)、[管理员配置与用户分配](https://help.aliyun.com/zh/ram/configure-oauth-for-alibaba-cloud-cli)。

## 复用 OAuth profile 执行

随包 [scripts/esa-cli.mjs](../scripts/esa-cli.mjs) 只桥接指定的 **RAM 用户 OAuth profile**，不安装 CLI、不授予权限、不决定项目归属。先调用官方 CLI 验证／刷新身份，再重读该 profile 的临时 STS，通过子进程的 ALIBABA_CLOUD_* 环境传给 ESA CLI；清除继承的其他凭据组，检查有效期，输出过滤已知凭据。没有额外 npm 依赖；不支持用它传入密钥命令行参数。执行记录只保留过滤后的输出。

~~~powershell
node "<skill目录>/scripts/esa-cli.mjs" --profile my-esa-profile --account "<主账号ID>" --user "<RAM用户名>" --aliyun "<aliyun可执行文件>" --cli "<esa-cli的bin/enter.cjs绝对路径>" --cwd "<部署工作目录>" -- project list --keyword my-demo
~~~

--aliyun 可省略以使用 PATH 中的 aliyun；--cwd 默认当前目录。其他参数明确给出，真实值来自本次核验和实际安装，不复制案例账号。脚本读取默认用户目录的官方配置，不自动切换 profile。返回原 ESA 退出码；超时或中断提示先查询部署状态，脚本不会自动重试上传。短期凭据被传入 ESA 进程后不会在运行中刷新，长任务需在发布前确认剩余有效期。

## 项目配置与更新

独立工作目录中的 esa.jsonc 与公开 dist 分离：

~~~json
{
  "name": "my-demo",
  "assets": { "directory": "./dist" }
}
~~~

纯静态目录不添加函数入口。已有项目不随意覆盖 notFoundStrategy；新项目按真实需求选择 404Page 或 singlePageApplication，并验证深层链接。CLI 会向父目录查找配置，执行前核对实际 cwd 与配置，避免加载另一个项目。

1. 首次新建与更新分别处理。更新先用 `project list --keyword`、`deployments list`、`domain list` 核对原项目、版本和域名；查不到不得利用 deploy 的自动创建行为新建。列表名称截断时用官方 `aliyun esa GetRoutine --Name <完整名称> --profile <profile>` 核对。
2. 保留当前完整产物和版本；合集先完整合入新内容，保留旧实验和共享资源。只公开 dist，不上传 CONFIG.md、OAuth 配置、运行记录或脚本。
3. 在上述脚本的 -- 后执行下列官方参数：

~~~text
deploy --name my-demo --assets ./dist --environment production --description release-marker --no-preview
~~~

4. 回读 deployments list 和实际生产部署比例，确认版本已切换；验证原固定网址及全部必要资源、交互、子页刷新和 404。临时测试域名裸地址不能代替固定域名验收。生产和 staging 独立处理，不同时发布两端。
5. 同项目更新再次使用原项目、环境和完整目录，验证原网址显示新版本、原内容保留。异常先查询状态再判断是否需要重试；恢复只在本次授权范围执行。

--no-preview 避免生成和输出带 Token 的预览链接，不影响正常部署。没有固定域名且本次需要测试链接时按主流程处理完整临时参数及有效期。新建、多项目、恢复与无人值守 CI 不由既有项目更新成功推定通过。

## 本地验证

~~~powershell
node --test "<skill目录>/scripts/esa-cli.test.mjs"
~~~

测试身份不符、凭据缺失／过期、环境隔离、刷新后凭据传递、秘密输出过滤及失败退出／不重试，外部进程由测试替身隔离。它们不能代替真实 OAuth、上传和公开访问；平台实测范围见 [验证状态](../SKILL.md#验证状态)。
