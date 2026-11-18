# 静态发布配置

将本模板复制到 Skill 根目录，命名为与 SKILL.md 同级的 CONFIG.md；真实配置不放在 assets 中。只修改“值”列。schemaVersion 是配置格式版本，不是 Skill 版本。default.target 默认 china（通过 china.provider 选择 ESA），也可填 overseas、both 或 ask；本次明确目标优先。ESA 与 Cloudflare 均默认使用 CLI，首次授权见双语指南。

| 字段 | 值 |
| --- | --- |
| schemaVersion | 2 |
| default.target | china |
| china.provider | esa |
| esa.account.ramLogin |  |
| esa.account.ownerId |  |
| esa.site.id |  |
| esa.site.name |  |
| esa.site.region |  |
| esa.site.accessType |  |
| esa.project.name |  |
| esa.project.environment | production |
| esa.project.deployMethod | cli |
| esa.project.productionBranch |  |
| esa.domain.name |  |
| edgeone.site | china |
| edgeone.account.uin |  |
| edgeone.account.label |  |
| edgeone.project.id |  |
| edgeone.project.name |  |
| edgeone.project.region | 全球可用区（含中国大陆） |
| edgeone.project.environment | production |
| cloudflare.account.id |  |
| cloudflare.account.email |  |
| cloudflare.account.label |  |
| cloudflare.project.name |  |
| cloudflare.project.productionBranch | main |
| cloudflare.project.environment | production |

只用一个平台时，未选平台的账号与项目可留空；整张表的字段行保留。china.provider 可填 esa、edgeone 或 ask。账号标识、站点及字段要求见 Skill 根目录下的 references/configuration.md。不填写密码、AccessKey、MFA 密钥、Cookie 或限时访问参数。实际 CONFIG.md 不随网站或 Skill 分发，升级保留已有值。

首次绑定时，用户在 `esa.domain.name` 填写自己的完整子域名，或在本次请求中指定；Cloudflare 子域名由本次请求提供。新项目名称与子域名一起指定，不覆盖已有默认项目。模板不预置域名，示例名称不代表已创建或可用；填写配置后仍需完成绑定、DNS 和 HTTPS 验收。
