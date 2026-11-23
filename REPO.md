# knowledge 仓库约定



维护可独立安装的技能、指南与工具。各技能保留自身依赖、验证和分发边界。



## 研发入口



- [项目首页](README.md) 维护用途、安装和使用方式。

- [研发文档导航](docs/README.md) 定位现行设计、计划与历史记录。



## 本项目约定与入口



本项目分发可独立安装的 Agent 技能与工具。根入口约束本仓库维护工作，不能通过某个技能的发布把所有 DreamSoul 内部要求隐式传给使用者。



- [英文入口](README.md)、[中文入口](README_zh.md)、[技能目录](skills/)、[工具目录](tools/)、[许可证](LICENSE)

- 每个技能的 SKILL.md、agents 元数据、references 与 scripts 按实际依赖一起维护。教程留在所属技能中，保持中英文说明、安装路径及发布包一致，不能只复制单个指令文件就宣称完成安装

- 修改目标技能前读取其自身说明和引用。保留用户授权、凭据保护、原始记录与错误处理边界，不因调研案例或示例命令自动执行外部操作

- 保持技能可移植，不能新增个人盘符、账号或必须存在的公司私有资料依赖。内部规范链接是维护入口，实际采用仍需核对适用范围和权限

- 验证按目标技能或工具现有能力选择，不虚构全仓统一测试命令。打包时保留长期依赖和许可证，检查包内路径与敏感数据；不自动安装到用户环境或发布

- 分支沿研发协作规范使用：`main` 保存已发布版本，`dev` 为长期开发集成分支；日常改动从 `dev` 创建必要的短期分支，经 PR 核验后合入 `dev`，稳定后通过 `dev → main` 发布 PR 进入正式版本，不直接推送这两个长期分支。

- PR 完成合并后在同轮收尾中删除对应远端及不再使用的本地短期分支；未合并分支先核对差异，明确合入、被替代或放弃后再清理。保留 `main`、`dev` 和仍有实际工作的短期分支，不留已完成分支作历史存档。清理前保留未提交改动，检查关联工作区；活动工作区不强制删除。



- 个人技能可使用按已确认GitHub username直接命名的长期分支，不加任务前缀。已登记的 `diaoenmao` 是个人长期分支，日常分支清理、PR合并后清理及无活动检查均排除；以后按本人确认登记，不凭分支外观推定。`main/dev` 继续承担通用发布和集成，个人技能不默认合回通用分支。个人分支不改变仓库可见性，业务原文、凭据及真实个人配置不随技能分发。
- 更新时逐项沿已有采用来源选择通用正式版或本人个人分支，并固定提交。个人分支继承的通用文件不代表这些能力已改用个人来源，不用其旧快照替换通用新版。客户端的长期保留登记和GitHub服务端删除保护分别核对；不以文字约定冒充服务端限制。

## 名称



- 技能和独立工具沿用已有目录或上游英文标识，使用小写字母、数字和连字符，如 `work-summary`、`github-summary`、`grok-bot-cli`，不另起 `Work Summary` 等英文显示名

- 中文说明可并列保留，如“工作总结 work-summary”。目录、SKILL.md 的 `name`、调用名、界面 `display_name` 及双语首页保持对应；名称调整时核对安装版和实际分发包的相关入口

- 改显示写法不擅自更换目录或调用标识；外部技能沿用上游标识。历史名称保留来源身份，正文中的产品名和技术术语按原有写法使用，不做全文大小写替换



## Workspace 采用记录



- 单项更新：[Workspace 65657c5](https://github.com/DreamSoul-AI/workspace/tree/65657c50cf6d98ac1898ae0183cb9ca98498e0a9)。采用旧对话重读、新对话定位、文档主动补链接、浏览器收尾、飞书专节及 CLI 任务临时目录、共享资源主动检查；保留项目专有约定和原整版基线。共享 data/models 直接复用，仅 artifacts 按仓库隔离，接入示例见 [Workspace 教程](https://github.com/DreamSoul-AI/workspace/blob/main/templates/software-engineering/examples/shared-resources/README.md)。

- 单项更新：[Workspace f01fab8](https://github.com/DreamSoul-AI/workspace/tree/f01fab8598f570a45eca8320e546d636268b700a)。采用通用文档规范及飞书/GitHub 平台章节入口、首次接入默认值和已有选择保留、代码架构设计与代码结构设计并列命名；图表简洁要求随通用规范读取。保留本项目专有约定、既有文档路径及原整版基线。[规范分发副本](https://github.com/DreamSoul-AI/workspace/blob/f01fab8598f570a45eca8320e546d636268b700a/%E6%96%87%E6%A1%A3/%E8%A7%84%E8%8C%83/%E9%80%9A%E7%94%A8/%E9%80%9A%E7%94%A8%E6%96%87%E6%A1%A3%E8%A7%84%E8%8C%83.md)。
- 单项更新：[Workspace 823d496](https://github.com/DreamSoul-AI/workspace/tree/823d4965035899d66a2d57751f1d28fbf934f99a)。采用临时产物与共享入口分工、资料根定位、目录升级检查、双端文档先改本地及面向读者的汇报；源码、测试、项目 docs 与专有约定保留，原整版基线继续沿用。
- 单项更新：[Workspace ea16de5](https://github.com/DreamSoul-AI/workspace/tree/ea16de5eda676aadaeefc1897ce0b83c062de2b6)。采用常规问题直接处理、结合目标和进度主动建议下一步；Knowledge 能力更新沿 [Workspace 教程](https://github.com/DreamSoul-AI/workspace/blob/main/资料/教程和工具/使用教程.md#workspace-与-knowledge-更新) 默认接入，保留通用与个人来源、项目专有约定和原整版基线。
