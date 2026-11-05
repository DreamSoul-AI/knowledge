# CPU 内存清理工具入口

[English](README.md) | **中文**

产品由 [CPU Memory Cleanup](https://github.com/DreamSoul-AI/cpu-memory-cleanup) 维护，[最新正式 Release](https://github.com/DreamSoul-AI/cpu-memory-cleanup/releases/latest) 提供 Rust CLI，不需要历史 Python 包。

Knowledge 维护 [cpu-memory-cleanup Skill](../../skills/cpu-memory-cleanup/SKILL.md)、元数据和[安装说明](../../skills/cpu-memory-cleanup/references/README_zh.md)，不包含产品可执行代码。首次初始化、版本解析和验证脚本全部位于产品仓库 scripts/agent-skill。

默认每项任务开始时解析官方 latest 正式版，校验实际附件 SHA256，并独立安装或复用。支持用户指定版本复现；任务内不切换运行时。工具接口从实际 --tool-info 发现，不能假定版本、构建或工具数量永远不变。Skill 自身按宿主方式更新，运行时通过产品初始化脚本更新。

真实工作集整理仅支持 Windows x64；Linux/macOS 产品包只读，不使用此 Windows 初始化入口。工作集整理不是 CPU 调度或内存压缩算法。安装或更新不采样、不清理、不启用自动规则，同机具备命令权限的 Agent 才可调用。

从 Knowledge main 或明确指定的提交安装 Skill；产品初始化脚本见官方[初始化入口](https://github.com/DreamSoul-AI/cpu-memory-cleanup/tree/master/scripts/agent-skill)，也包含在产品 Windows ZIP 中。初始化默认解析最新稳定 Release，普通使用不依赖源码仓库。

普通 Skill 使用只通过 stdout 返回结果，不创建任何运行历史文件或 Markdown，不写任何仓库。整理要求原生程序声明 stdout_only 能力并携带 --no-record；旧版不能靠更新 Skill 获得此能力。用户明确要求保存时才传 --output-dir，只有已保存结果可回看。使用前按实际工具目录核对原生无记录能力。
