# Python 环境管理与排障 Python Environment Management

<h4 align="center">
    <p>
        <a href="README.md">English</a> |
        <b>中文</b>
    </p>
</h4>

## 目录
1. [简介](#简介)
2. [验证现有的Python安装](#验证现有的Python安装)
    - [Windows](#windows)
    - [Mac](#mac)
    - [Linux](#linux)
3. [安装Anaconda](#安装anaconda)
    - [下载Anaconda](#下载anaconda)
    - [安装](#安装)
        - [Windows](#windows-1)
        - [Mac](#mac-1)
        - [Linux](#linux-1)
    - [验证Anaconda安装](#验证anaconda安装)
4. [安装PyCharm](#安装pycharm)
    - [PyCharm版本](#pycharm版本)
    - [下载PyCharm](#下载pycharm)
    - [安装](#安装-1)
        - [Windows](#windows-2)
        - [Mac](#mac-2)
        - [Linux](#linux-2)
5. [配置PyCharm与Anaconda](#配置pycharm与anaconda)
    - [打开PyCharm](#打开pycharm)
    - [设置Anaconda环境](#设置anaconda环境)
    - [为Conda配置终端](#为conda配置终端)
6. [排除数据和输出文件夹](#排除数据和输出文件夹)
    - [标记为排除](#标记为排除)
    - [修改`.idea`文件夹](#修改idea文件夹)
7. [使用符号链接共享数据](#使用符号链接共享数据)
8. [使用终端与Jupyter Notebooks运行Python脚本](#使用终端与jupyter-notebooks运行python脚本)
    - [终端](#终端)
    - [Jupyter Notebooks](#jupyter-notebooks)
9. [调试](#调试)
    - [使用 `print()` 和 `exit()` 进行基本调试](#使用-print-和-exit-进行基本调试)
    - [使用 `pdb` 进行高级调试](#使用-pdb-进行高级调试)
    - [PyCharm交互式运行器](#pycharm交互式运行器)
10. [其他提示](#其他提示)

---

## 简介
本技能用于检查、准备和诊断项目的 Python 环境，以实际解释器、依赖和目标命令为依据。交付可验证的运行环境或有证据的故障诊断，不是通用安装教程；只要求诊断时不实施修复。调用名保留 `python-environment`。后面的 PyCharm／Anaconda 内容是可选路线，先遵守项目已有工具和版本要求。已有环境满足任务时直接复用，不为统一工具重装环境。

### 调用与核验
环境检查、各管理工具的操作边界及交付接口见 [环境操作参考](environment-operations.md)。尤其注意 `uv run` 可能自动同步依赖，`pip check` 通过只说明依赖元数据兼容，不能证明原生库、导入或计算正常。只诊断时优先直接使用已确认的解释器，不执行自动同步或修复。

可提供项目路径、指定解释器或环境、适用要求和目标命令，均为按需输入，例如：“使用 Python 环境技能检查这个项目，复用现有环境，运行它的轻量测试，不安装或升级依赖。”未指定时从当前项目说明定位，不固定个人路径。

用选定环境的解释器检查身份与依赖，例如 Windows PowerShell：
```powershell
# 路径仅为项目环境示例，先核实实际位置
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable, sys.prefix, sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```
匹配版本号、看到 `(base)` 或“激活成功”都不能代替解释器和导入位置核对。可直接指定解释器选择环境，无须默认修改全局 PATH；但 Conda 或原生扩展还可能需要其运行时设置，不能把解释器可启动当成全部依赖健康。环境隔离及创建方式见 [Python venv 文档](https://docs.python.org/3/library/venv.html)。

需要安装依赖时，先读项目说明和依赖文件。确认使用 pip 后，通过已选解释器执行 `-m pip`；使用其他管理工具的项目沿其工具执行。`requirements.txt` 可能包含构建、远端源或可编辑安装，不一定是完整锁文件，不能见到文件就直接安装。解释器绑定方式见 [pip 使用指南](https://pip.pypa.io/en/stable/user_guide/)。

固定版本、锁文件或哈希校验失败时保留错误，不擅自放宽版本、关闭校验或转为全局安装。采用哈希模式的项目应维持完整约束，见 [pip 安装校验说明](https://pip.pypa.io/en/stable/topics/secure-installs/)。安装失败不保证环境完全未变，应核对受影响包再报告。

已有环境损坏时，先区分解释器缺失、依赖缺失、源码导入路径和 IDE／Notebook 选择错误。保留旧目录及用户文件，必要时在本次允许范围内另建恢复环境，不默认覆盖、清空或卸载。源码布局项目优先采用它已声明的测试或启动入口，不因普通终端不能直接导入包就立即安装。

完成后给出所用环境、实际改动、运行命令、结果和剩余限制。安装成功、导入成功、测试通过分别记录，不把局部运行扩大为所有环境均可用。

### 缺什么才补什么
先按目标命令判断是否可用，区分实际阻塞项、可选功能和无关环境问题。能完成目标就直接复用，不为整理环境重装或升级。确实缺少必要依赖时，先说明缺项依据、最小处理、影响范围和验证命令，再在已有授权内按项目工具及固定要求补齐。不为少装一个包绕过锁文件，也不顺手装上全部 extras 或修复其他包。

最终交付讲清：用了哪个环境与管理工具、在哪个目录执行什么命令、实际改了什么或没有改动、运行结果怎样、还有哪些限制。待执行方案与实际修改分开，诊断未修复不能写成已经可用。需要交接时引用项目原有依赖声明和锁文件，不把共享基础环境的全部包导出当作项目要求。具体判断和交付例子见 [环境操作参考](environment-operations.md)。

## 验证现有的Python安装
在安装新软件之前，请检查现有的Python安装以避免冲突。

### Windows
- 打开命令提示符并输入：`python --version` 或 `py --version`。
- 核对项目实际使用的解释器路径和版本，保留其他项目及系统正在使用的安装，不把卸载作为常规检查。

### Mac
- 打开终端并输入：`python --version` 或 `python3 --version`。
- 核对解释器来源和项目环境，不直接删除系统或第三方管理的 Python 目录。

### Linux
- 打开终端并输入：`python --version` 或 `python3 --version`。
- 保留操作系统和包管理器依赖的 Python，优先使用项目隔离环境，不通过卸载系统 Python 排障。

## 安装Anaconda
仅在项目已采用 Conda 或本人选择该路线时安装 Anaconda／Conda，已有合适环境可跳过。先核对项目所需 Python 版本、平台与已有依赖，不自动下载大型发行版或升级到最新版。

### 下载Anaconda
- 访问[Anaconda下载页面](https://www.anaconda.com/products/distribution)并下载适合您操作系统的安装程序。

### 安装

#### Windows
- 运行下载的安装程序。
- 按当前使用者和项目需要选择安装范围，不默认注册为系统 Python 或添加到全局 PATH。
- 已有终端和项目继续使用其原环境，需要改变默认设置时另确认影响范围。
- 完成安装过程。

#### Mac
- 选择适合本机处理器架构的安装程序，使用实际下载的 `.sh` 文件名运行 `bash`，不沿用旧版本或其他架构的文件名。
- 按照提示完成安装。

#### Linux
- 选择适合本机系统与处理器架构的安装程序，使用实际下载的 `.sh` 文件名运行 `bash`。
- 按照提示完成安装。

### 验证Anaconda安装
- 打开一个新的终端窗口。
- 输入 `python` 并验证输出是否包含“packaged by Anaconda, Inc.”。

## 安装PyCharm
PyCharm是一款专为Python开发设计的强大IDE。

### PyCharm版本
安装前以 [PyCharm 官方下载页](https://www.jetbrains.com/pycharm/download/) 的当前产品和许可说明为准，不将历史版本划分当作当前事实。已有合适编辑器时可以跳过本节。

### 下载PyCharm
- 访问[PyCharm下载页面](https://www.jetbrains.com/pycharm/download/)并下载适合您操作系统的版本。

### 安装

#### Windows
- 运行下载的安装程序并按照安装向导操作。
- 选择“将PyCharm添加到上下文菜单（右键菜单）”选项以便于访问。
- 可选择创建桌面快捷方式。

#### Mac
- 打开下载的 `.dmg` 文件并将PyCharm拖动到应用程序文件夹。

#### Linux
- 解压下载的tar包并从 `bin` 子目录运行 `./pycharm.sh`。

## 配置PyCharm与Anaconda

### 打开PyCharm
创建一个新项目或打开一个现有项目。

### 设置Anaconda环境
- 转到 `文件` > `设置`（或在Mac上 `PyCharm` > `偏好设置`）。
- 导航到 `项目: <project_name>` > `Python解释器`。
- 点击齿轮图标并选择 `添加`。
- 选择 `系统环境` 或 `Conda环境` 并指定Anaconda安装路径。

### 为Conda配置终端
- 仅在项目采用 Conda 时核对终端与 IDE 指向的环境是否一致，不因缺少 `(base)` 前缀就切换默认终端。IDE 菜单随版本变化，重点是选择项目真实解释器，不是固定菜单路径。

## 排除数据和输出文件夹

### 标记为排除
1. 在项目工具窗口中，找到`data`和`output`文件夹（或其他包含大文件或生成内容的目录）。
2. 右键点击每个文件夹。
3. 选择**标记目录为** > **排除**。

### 为什么要排除这些文件夹？

排除`data`和`output`目录可以帮助PyCharm避免索引不必要或大型文件。尤其是在项目加载期间，索引这些文件夹可能会导致PyCharm显著变慢，甚至挂起IDE。通过排除这些文件夹，您可以确保PyCharm跳过它们的索引，从而提高性能并减少加载时间。

### 修改`.idea`文件夹

如果您不想通过PyCharm界面手动排除文件夹，您可以修改`.idea`文件夹中的`.iml`文件，使用编程方式排除文件夹。这确保了像`data`和`output`这样的文件夹不会被索引，防止在加载过程中冻结IDE。

要排除文件夹，在`.iml`文件中找到`<content>`标签，并添加以下内容：

```xml
<content url="file://$MODULE_DIR$">
    <excludeFolder url="file://$MODULE_DIR$/data" />
    <excludeFolder url="file://$MODULE_DIR$/output" />
</content>
```

这样可以确保PyCharm跳过指定文件夹的索引，保持项目中大型文件或数据集的流畅性能。

## 使用符号链接共享数据

如果您有多个项目需要共享相同的数据源，使用`data`文件夹的符号链接可以通过避免多个项目复制相同数据来节省磁盘空间。创建一个符号链接指向共享的数据源，而不是在项目中重复数据。

创建符号链接：

- **在Windows上**，使用以下命令：
  ```bash
  mklink /D data "C:\path\to\shared\data"
  ```

- **在Linux/macOS上**，使用此命令：
  ```bash
  ln -s /path/to/shared/data data
  ```

这样，`data`文件夹将指向一个共享位置，允许多个项目访问相同的数据而不占用额外的磁盘空间。

## 使用终端与Jupyter Notebooks运行Python脚本

### 终端
- **适用于大型项目和自动化**：使用终端运行包含多个模块的项目、自动化任务和性能密集型脚本，核对项目环境与工作目录。

### Jupyter Notebooks
- **适用于演示和概念验证**：适用于概念验证、数据可视化演示和创建文档良好的报告。当您需要快速原型化想法或展示概念时，请使用笔记本。

通过遵循这些步骤，您将拥有一个强大且高效的Python开发环境，并已准备好进行任何数据科学或开发项目。

## 调试

有效的调试对于开发健壮的Python应用程序至关重要。以下是三种调试Python脚本的方法：

### 使用 `print()` 和 `exit()` 进行基本调试
使用 `print()` 语句输出变量值和执行流。这种方法对简单的调试任务快速有效。

示例：
```python
def add(a, b):
    print(f"Adding {a} and {b}")
    result = a + b
    print(f"Result: {result}")
    return result

add(2, 3)
exit()  # 在此处终止脚本以进行检查
```

### 使用 `pdb` 进行高级调试
Python调试器（`pdb`）允许进行更精细的调试，例如设置断点和逐步执行代码。

使用 `pdb`：
1. 在脚本中导入 `pdb`。
2. 在要开始调试的地方插入 `pdb.set_trace()`。

示例：
```python
import pdb

def add(a, b):
    pdb.set_trace()  # 从此处开始调试
    result = a + b
    return result

add(2, 3)
```

### PyCharm交互式运行器
如果您不使用终端，PyCharm的交互式运行器提供了一个用户友好的调试环境，具有断点、监视和变量检查等强大功能。

使用PyCharm的交互式运行器：
1. 通过点击行号旁边的沟槽设置断点。
2. 右键点击您的脚本并选择“调试”以启动调试器。
3. 使用调试控制逐步执行代码、检查变量和评估表达式。

这些方法提供了从使用 `print()` 和 `exit()` 进行快速检查，到使用 `pdb` 进行详细检查，再到在PyCharm中使用全面调试环境的各种调试选项。选择最适合您调试需求的方法。

## 其他提示
- **使用终端而非PyCharm运行器**：
  - 终端、IDE 运行器与 Notebook 均可使用，发生差异时分别核对解释器、工作目录、环境变量和内核，不默认禁用某一种入口。
  
- **代码导航**：
  - 按已安装编辑器及扩展的实际功能使用跳转、补全和调试，不将某个快捷键当作选择环境管理工具的依据。

- **教育许可证**：
  - 如果您是学生或教育工作者，您可以通过JetBrains网站[申请免费教育许可证](https://www.jetbrains.com/community/education/#students)，用于PyCharm专业版。
