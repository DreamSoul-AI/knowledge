# 多仓库共享资源接入代码结构设计

## 实现映射

| 模块 | 职责 |
| --- | --- |
| `tools/shared-repository-resources/link_shared.py` | 配置、预检、执行和 JSON 结果 |
| `config.example.json` | 通用资源映射案例 |
| `examples/research.config.example.json` | 可选研发配置 |
| `tests/test_link_shared.py` | 临时仓库和真实链接验证 |

`make_plan` 解析版本化 JSON，拒绝重复键、未知合同字段、越界或重叠映射，核对目录及 Git 跟踪，返回明确入口清单。路径相对配置文件解析，选择部分仓库时只计划对应映射。

`execute` 依次复核和执行清单，复用正确链接，仅创建显式允许的新资源。`link_state` 判断真实入口，`ordinary_parent_chain` 拒绝经链接或 Windows 目录联接点转向的父目录，`ensure_ignored` 保留现有规则并核对忽略效果。

`main` 提供预览、显式执行和仓库子集选择，输出 UTF-8 JSON。失败时返回已核验的完成项及具体错误，不自动清理实际入口；下一次重新计划并按文件系统现状接续。

## 依赖和状态

运行仅依赖 Python 标准库、Git 及系统链接权限。Git 子命令通过参数数组调用，仓库路径显式传递，不修改全局 Git 设置。没有隐式安装、调度、网络访问或外部配置解析库。

状态以真实链接及资源为准，报告记录本轮已核验项。未核验的部分创建可能需要运行后检查，不能把完成项列表当作全批事务提交记录。配置和资源在运行期间应保持稳定。
