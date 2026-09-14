# Git
<h4 align="center">
    <p>
        <a href="README.md">English</a> |
        <b>中文</b>
    </p>
</h4>

## 目录

1. [简介](#简介)
2. [Git 的安装](#git-的安装)
3. [配置用户名和密码](#配置用户名和密码)
4. [使用 Clash (VPN) 设置 Git 代理](#使用-clash-vpn-设置-git-代理)
5. [基本 Git 命令](#基本-git-命令)
    - [git clone](#git-clone)
    - [git pull](#git-pull)
    - [git branch](#git-branch)
    - [git checkout](#git-checkout)
    - [git status](#git-status)
    - [git add --all](#git-add---all)
    - [git reset](#git-reset)
    - [git commit -m "[some message here]"](#git-commit--m-some-message-here)
    - [git push](#git-push)
6. [合并一个仓库到另一个仓库](#合并一个仓库到另一个仓库)
7. [最佳实践](#最佳实践)

## 简介

Git 是一个分布式版本控制系统，用于在软件开发过程中跟踪源代码的更改。GitHub 是一个基于 Web 的平台，使用 Git 并提供额外的功能，如协作、代码审查和项目管理。本教程将指导你了解使用 Git 和 GitHub 的基础知识。

## Git 的安装

### Windows

1. 从 [git-scm.com](https://git-scm.com/downloads) 下载 Git 安装程序。
2. 运行安装程序并按照屏幕上的说明进行操作（默认设置即可）。
3. 要验证安装，打开命令提示符并输入：
   ```bash
   git --version
   ```

### MacOS

1. 如果尚未安装 Homebrew，请安装 Homebrew：
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. 使用 Homebrew 安装 Git：
   ```bash
   brew install git
   ```
3. 要验证安装，打开终端并输入：
   ```bash
   git --version
   ```

### Linux

1. 打开终端。
2. 使用包管理器安装 Git：
   - **Debian/Ubuntu:**
     ```bash
     sudo apt-get update
     sudo apt-get install git
     ```
   - **Fedora:**
     ```bash
     sudo dnf install git
     ```
3. 要验证安装，输入：
   ```bash
   git --version
   ```

## 配置用户名和密码

安装 Git 后，你需要设置你的用户名和电子邮件地址。这很重要，因为每个 Git 提交都会使用这些信息。此外，当你将提交推送到 GitHub 时，这些详细信息将用于将提交归属于你的 GitHub 帐户。

1. 设置你的用户名：
   ```bash
   git config --global user.name "Your Name"
   ```

2. 设置你的电子邮件地址：
   ```bash
   git config --global user.email "your.email@example.com"
   ```

3. 配置 Git 以存储你的凭据：
   ```bash
   git config --global credential.helper store
   ```

4. 下次执行需要身份验证的 Git 操作（例如 `git push`）时，Git 会提示你输入用户名和密码，并将它们存储在主目录中的纯文本文件中（`~/.git-credentials`）。

有关将 Git 与 GitHub 连接的更多信息，请参阅 [GitHub 文档](https://docs.github.com/en/get-started/quickstart/set-up-git)。

## 使用 Clash (VPN) 设置 Git 代理

在需要使用 VPN 的环境中（如使用 Clash 时），你可能需要配置 Git 以使用代理。这确保了 Git 可以通过 VPN 连接到远程仓库。请按照以下步骤在 Linux 上为 Git 设置代理：

### 设置 Git 代理的步骤：

1. **设置代理配置**：
   要全局配置 Git 的 HTTP 代理，请使用以下命令：
   ```bash
   git config --global http.proxy http://127.0.0.1:7890
   git config --global https.proxy http://127.0.0.1:7890
   ```
   将 `127.0.0.1` 替换为你的代理服务器 IP 地址，将 `7890` 替换为 Clash 使用的端口号。如果你的代理服务器需要身份验证，命令应包括你的用户名和密码，如下所示：
   ```bash
   git config --global http.proxy http://username:password@127.0.0.1:7890
   git config --global https.proxy http://username:password@127.0.0.1:7890
   ```
   如果不需要身份验证，则可以省略 `username:password@` 部分。

2. **验证代理配置**：
   要检查代理是否设置正确，请运行：
   ```bash
   git config --global --get http.proxy
   git config --global --get https.proxy
   ```
   此命令应输出你刚刚设置的代理配置。

3. **移除代理配置**：
   如果你想移除代理配置，你可以使用以下命令：
   ```bash
   git config --global --unset http.proxy
   git config --global --unset https.proxy
   ```

## 基本 Git 命令

### git clone

将一个仓库克隆到新创建的目录中。这对于将远程仓库复制到本地计算机非常有用。

```bash
git clone <repository_URL>
```

### git pull

从另一个仓库或本地分支获取并集成。这用于使用远程仓库（例如 GitHub）的最新更改更新本地仓库。

```bash
git pull
```

### git branch

列出、创建或删除分支。分支对于隔离开发功能非常有用。

列出所有分支：

```bash
git branch
```

创建新分支：

```bash
git branch <branch_name>
```

删除分支：

```bash
git branch -d <branch_name>
```

### git checkout

切换分支或恢复工作树文件。这对于在不同分支和提交之间移动非常有用。

切换到现有分支：

```bash
git checkout <branch_name>
```

创建并切换到新分支：

```bash
git checkout -b <branch_name>
```

### git status

显示工作树状态。它对于查看哪些更改已暂存、哪些未暂存以及哪些文件未被 Git 跟踪非常有用。

```bash
git status
```

### git add --all

暂存工作目录中的所有更改以进行下一次提交。这包括新的、修改的和删除的文件。

```bash
git add --all
```

### git reset

取消暂存已添加到暂存区的文件，但保持工作目录不变。

```bash
git reset
```

### git commit -m "[some message here]"

记录对仓库所做的更改并附带消息。消息应描述所做的更改。

```bash
git commit -m "[some message here]"
```

### git push

将本地仓库内容上传到远程仓库（例如 GitHub）。这需要在 GitHub 上设置一个远程仓库并将本地仓库连接到它。如果你从 GitHub 克隆了一个仓库，它会自动连接。

```bash
git push
```

#### 推送到 GitHub 的步骤：

1. **在 GitHub 上创建一个仓库：**

   - 访问 [GitHub](https://github.com/) 并登录。
   - 点击右上角的 "+" 图标并选择 "New repository"。
   - 输入仓库名称并点击 "Create repository"。

2. **将 GitHub 仓库添加为远程仓库：**

   - 复制 GitHub 仓库的 URL。
   - 在本地仓库中，添加远程仓库：

   ```bash
   git remote add origin <repository_URL>
   ```

3. **将更改推送到 GitHub：**

   ```bash
   git push -u origin main
   ```

通过这些步骤，你可以将本地仓库连接到 GitHub 并将更改推送到远程仓库。

## 合并一个仓库到另一个仓库

要将一个仓库合并到另一个仓库并保留提交记录，请按照以下步骤操作：

1. 在目标仓库中将源仓库添加为远程仓库。
   ```bash
   git remote add source_repo <source_repo_URL>
   ```

2. 获取源仓库的分支及其各自的提交。
   ```bash
   git fetch source_repo
   ```

3. 创建一个新分支以包含源仓库的历史记录。
   ```bash
   git checkout -b source_branch source_repo/main
   ```

4. 将源仓库分支合并到目标仓库的分支中。
   ```bash
   git checkout main
   git merge source_branch
   ```

5. 将更改推送到远程仓库。
   ```bash
   git push
   ```

通过这些步骤，你可以确保源仓库的提交历史记录保留在目标仓库中。

## 最佳实践

### 使用 .gitignore 模板
要避免将不必要的文件（如操作系统特定文件、IDE 配置文件和构建工件）推送到你的仓库，请始终使用 `.gitignore` 文件。GitHub 提供了不同编程语言和开发环境的 `.gitignore` 模板集合。你可以参考[这个用于 Python 的 .gitignore 文件示例](https://github.com/diaoenmao/RPipe/blob/main/.gitignore)。

### 避免推送数据集和输出文件
避免将大数据集和输出文件推送到你的 GitHub 仓库。使用 `.gitignore` 文件避免将这些文件推送到你的仓库，确保你的仓库保持干净和高效。
