# CPU 内存清理工具入口

[English](README.md) | **中文**

产品由 [CPU Memory Cleanup](https://github.com/DreamSoul-AI/cpu-memory-cleanup) 维护，[最新正式 Release](https://github.com/DreamSoul-AI/cpu-memory-cleanup/releases/latest) 提供 Rust CLI，不需要历史 Python 包。

Knowledge 维护 [cpu-memory-cleanup Skill](../../skills/cpu-memory-cleanup/SKILL.md)、元数据和[安装说明](../../skills/cpu-memory-cleanup/references/README_zh.md)，不包含产品可执行代码。首次初始化、版本解析和验证脚本全部位于产品仓库 scripts/agent-skill。

默认每项任务开始时解析官方 latest 正式版，校验实际附件 SHA256，并独立安装或复用。支持用户指定版本复现；任务内不切换运行时。工具接口从实际 --tool-info 发现，不能假定版本、构建或工具数量永远不变。Skill 自身按宿主方式更新，运行时通过产品初始化脚本更新。

真实工作集整理仅支持 Windows x64；Linux/macOS 产品包只读，不使用此 Windows 初始化入口。工作集整理不是 CPU 调度或内存压缩算法。安装或更新不采样、不清理、不启用自动规则，同机具备命令权限的 Agent 才可调用。

产品接入脚本已在官方[对应源码提交](https://github.com/DreamSoul-AI/cpu-memory-cleanup/tree/fab1230ed0e63d5afa010b80e240e10b5bd559b0/scripts/agent-skill)，Skill 和 ZIP 以包含它们的 Knowledge 开发分支为准。当前先从云端固定提交重装验证，暂不发布新 Release；普通使用不依赖用户拥有源码仓库。

普通 Skill 使用只通过 stdout 返回结果，不创建任何运行历史文件或 Markdown，不写任何仓库。整理要求原生程序声明 stdout_only 能力并携带 --no-record；旧版不能靠更新 Skill 获得此能力。用户明确要求保存时才传 --output-dir，只有已保存结果可回看。新原生行为目前仅本地构建，尚未发布。
