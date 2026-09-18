# 设置Python开发环境（PyCharm和Anaconda）

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
本教程将指导您使用PyCharm和Anaconda设置一个强大的Python开发环境。我们将涵盖不同操作系统的安装步骤，验证现有的Python安装，并配置PyCharm以实现高效编码。

## 验证现有的Python安装
在安装新软件之前，请检查现有的Python安装以避免冲突。

### Windows
- 打开命令提示符并输入：`python --version` 或 `py --version`。
- 检查已安装的Python版本，并从控制面板中卸载不必要的版本。

### Mac
- 打开终端并输入：`python --version` 或 `python3 --version`。
- 要卸载，请删除 `/Library/Frameworks/Python.framework/Versions/` 中的Python目录。

### Linux
- 打开终端并输入：`python --version` 或 `python3 --version`。
- 使用您的包管理器卸载不必要的Python版本（例如，`sudo apt-get remove python`）。

## 安装Anaconda
安装最新的Anaconda发行版，其中包括众多预安装的数据科学库和工具。

### 下载Anaconda
- 访问[Anaconda下载页面](https://www.anaconda.com/products/distribution)并下载适合您操作系统的安装程序。

### 安装

#### Windows
- 运行下载的安装程序。
- 如果选择“管理员”，则在安装过程中选择“将Anaconda注册为系统Python”。（推荐）
- 如果选择“仅我”，则在安装过程中勾选“将Anaconda添加到我的PATH环境变量”。
- 完成安装过程。

#### Mac
- 打开终端并运行下载的 `.sh` 脚本：`bash Anaconda3-2023.03-MacOSX-x86_64.sh`（版本号可能有所不同）。
- 按照提示完成安装。

#### Linux
- 打开终端并运行下载的 `.sh` 脚本：`bash Anaconda3-2023.03-Linux-x86_64.sh`（版本号可能有所不同）。
- 按照提示完成安装。

### 验证Anaconda安装
- 打开一个新的终端窗口。
- 输入 `python` 并验证输出是否包含“packaged by Anaconda, Inc.”。

## 安装PyCharm
PyCharm是一款专为Python开发设计的强大IDE。

### PyCharm版本
PyCharm有几个版本：
- **社区版**：免费开源，适合纯Python开发。
- **专业版**：付费版本，包含更多用于Web开发、数据库管理等的功能。
- **教育版**：免费用于教育目的，包含专业版的功能。您可以在[此处](https://www.jetbrains.com/community/education/#students)了解更多并申请教育许可证。

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
- 如果命令提示符前未显示 `(base)` 前缀，请通过转到 `文件` > `设置` > `工具` > `终端` 并将shell路径设置为Conda终端可执行文件，来将默认终端设置为Conda。

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
- **适用于大型项目和自动化**：使用终端运行包含多个模块的大型项目，自动化任务以及处理性能密集型脚

本。更适合管理虚拟环境和与Git等版本控制系统集成。

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
  - 建议使用终端运行脚本以避免内置运行器的问题。
  
- **代码导航**：
  - 使用PyCharm而非VSCode的优势之一是能够通过 `Ctrl + 左键单击` 导航到定义。

- **教育许可证**：
  - 如果您是学生或教育工作者，您可以通过JetBrains网站[申请免费教育许可证](https://www.jetbrains.com/community/education/#students)，用于PyCharm专业版。
