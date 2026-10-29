# CPU 内存清理工具入口

[English](README.md) | **中文**

这里是调用说明入口，不包含内存整理实现、安装器或自动运行任务。产品Package、CLI和桌面统一维护在 [cpu-memory-cleanup](https://github.com/DreamSoul-AI/cpu-memory-cleanup)。

完整的版本固定、安装、五个工具、授权边界、目标身份和离线回看合同见 [工具接入说明](https://github.com/DreamSoul-AI/cpu-memory-cleanup/blob/a539905f9bf1d43569fb6473fa7b0ff25963223c/docs/%E5%B7%A5%E5%85%B7%E6%8E%A5%E5%85%A5%20Tool%20Integration%20CPU%20%E5%86%85%E5%AD%98%E6%B8%85%E7%90%86.md)。该说明固定到a539905，功能安装固定到9c7d725，来自PR #11，不能用已发布v0.2.0冒充新的单进程能力。

本工具面向同机Python程序和能执行本地子进程的Agent宿主，通过包或CLI使用。不是MCP服务，不属于可由skill-installer安装的SKILL目录。宿主先按实际环境准备包，再读取静态 --tool-info，维护许可由宿主落实。安装到用户环境和实际运行不是阅读本指南的隐含动作。

当前约定禁止真实采样或清理时，仅静态目录、离线回看和假接口验证可执行。进程列表也是实时读取，不得默认运行。这里只维护链接与入口边界，不复制产品代码或另一套参数清单。
