# 多仓库共享资源接入

[English](README.md) | 简体中文

让多个仓库通过目录符号链接复用部分资源，同时保留各仓库自己的访问入口。实际资源保存在明确的目标目录，减少重复存放。

资源名称、目录位置、仓内入口和每个仓库采用的子集均由 JSON 配置决定，可用于不同项目布局和目录资源类型。

## 研发场景示例

研发中的多个 repo 可以共享数据（data）、模型及权重（models），并集中管理、按需复用运行产物（artifacts）。产物可按项目隔离，也可以将需要复用的部分明确共享。[研发示例说明](examples/README_zh.md) 和 [示例配置](examples/research.config.example.json) 展示这一常用组织方式，其他场景可调整资源和映射。

## 配置

研发项目可从 [研发示例](examples/research.config.example.json) 起步，其他场景可参考 [通用示例](config.example.json)，填写实际目录。所有相对路径以配置文件所在目录为基准，与工具检出位置和命令的当前目录无关。换设备后核对该设备上的实际位置和资源是否存在。

```json
{
  "version": 1,
  "resources": {
    "icons": {"path": "shared/icons"},
    "reports": {"path": "shared/reports", "create": true}
  },
  "repositories": {
    "app": {
      "path": "repositories/app",
      "links": {"assets/icons": "icons", ".local/reports": "reports"}
    },
    "exporter": {
      "path": "repositories/exporter",
      "links": {"inputs/icons": "icons"}
    }
  }
}
```

- `resources` 的键是使用者定义的资源名，`path` 是已有目录，`create` 默认 `false`
- `create: true` 仅允许为该资源新建空目录。已有损坏链接仍会被拦截，不会因此重建一个空资源来掩盖缺失
- `repositories` 的键是稳定标识，`path` 指 Git 仓库根目录。允许目录分散、名称不同，Git worktree 的根目录也可使用
- `links` 把仓内相对路径映射到资源名。使用 `/` 分隔，每个仓库可以采用不同入口、选择不同资源
- 资源可以共用，也可以显式分开，例如两个项目分别映射到自己的结果目录。工具不会按仓库文件夹名隐式生成目标

真实个人路径留在本机配置，不随公共项目提交。示例中的目录和仓库不会由预览自动创建。

## 使用

需要 Python 3.10+、Git，以及当前进程创建目录符号链接的权限。Windows 是否可用取决于实际权限或开发者模式，工具不自行提权，也不退回复制或目录联接点。

从本工具目录执行，先预览全部映射：

```text
python link_shared.py --config <实际配置.json>
```

核对 JSON 报告中的入口、目标和操作范围，再明确执行：

```text
python link_shared.py --config <实际配置.json> --apply
```

只处理配置中的部分仓库：

```text
python link_shared.py --config <实际配置.json> --repositories app --apply
```

默认预览不写入。执行会为显式允许的缺失资源创建目录，建立目录符号链接，并按需向各仓库 `.gitignore` 追加精确入口规则，保留既有内容。输出为 UTF-8 JSON，退出码 `0` 表示所请求操作完成，`1` 表示校验或执行失败。

## 重跑和冲突

全部配置先完成预检，再进入写入阶段。实体文件或目录占用、链接指向其他目标、损坏链接、Git 已跟踪内容、路径越界、映射重叠及经符号链接或 Windows 目录联接点转向的入口父目录，都会报告具体冲突并停止。

已经正确的链接直接复用，核对实际目标与 Git 忽略。执行中断可能留下已完成部分；JSON 的 `completed` 记录已核验项，重跑根据真实文件系统接续，不删除或覆盖旧入口。工具不支持并发修改同一批路径，执行时应保持配置、资源和入口稳定。

当前只处理目录资源，不复制、移动、删除或上传内容，也不更改项目消费者的配置。链接建好后，还要检查项目是否实际读取该入口。符号链接不负责跨设备传输、环境兼容或共享资源的多方写入协调。

## 研发示例和验证

[研发示例](examples/research.config.example.json) 演示共享数据、权重并按项目隔离结果。这是可选配置，通用实现不依赖这些资源名称。

运行隔离测试：

```text
python -B tests/test_link_shared.py
```

测试只创建临时 Git 仓库和合成资源。可通过 `SHARED_RESOURCES_TEST_ROOT` 指定临时根目录，通过 `SHARED_RESOURCES_TEST_REPORT` 指定逐项 JSON 结果文件。Windows 需要允许测试进程创建符号链接。已验证两种 Windows 布局、工具换位置、重跑、冲突和中断接续，其他操作系统尚未实测。
