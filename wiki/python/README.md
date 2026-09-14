# Setting Up a Python Development Environment with PyCharm and Anaconda

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="README_zh.md">中文</a>
    </p>
</h4>

## Table of Contents
1. [Introduction](#introduction)
2. [Verify Existing Python Installations](#verify-existing-python-installations)
    - [Windows](#windows)
    - [Mac](#mac)
    - [Linux](#linux)
3. [Install Anaconda](#install-anaconda)
    - [Download Anaconda](#download-anaconda)
    - [Installation](#installation)
        - [Windows](#windows-1)
        - [Mac](#mac-1)
        - [Linux](#linux-1)
    - [Verify Anaconda Installation](#verify-anaconda-installation)
4. [Install PyCharm](#install-pycharm)
    - [PyCharm Editions](#pycharm-editions)
    - [Download PyCharm](#download-pycharm)
    - [Installation](#installation-1)
        - [Windows](#windows-2)
        - [Mac](#mac-2)
        - [Linux](#linux-2)
5. [Configure PyCharm with Anaconda](#configure-pycharm-with-anaconda)
    - [Open PyCharm](#open-pycharm)
    - [Set Up Anaconda Environment](#set-up-anaconda-environment)
    - [Configure Terminal for Conda](#configure-terminal-for-conda)
6. [Exclude Data and Output Folders](#exclude-data-and-output-folders)
    - [Mark as Excluded](#mark-as-excluded)
    - [Modifying the `.idea` Folder](#modifying-the-idea-folder)
7. [Use Symbolic Links for Shared Data](#use-symbolic-links-for-shared-data)
8. [Using Terminal vs. Jupyter Notebooks to Run Python Scripts](#using-terminal-vs-jupyter-notebooks-to-run-python-scripts)
    - [Terminal](#terminal)
    - [Jupyter Notebooks](#jupyter-notebooks)
9. [Debugging](#debugging)
    - [Basic Debugging with `print()` and `exit()`](#basic-debugging-with-print-and-exit)
    - [Advanced Debugging with `pdb`](#advanced-debugging-with-pdb)
    - [PyCharm Interactive Runner](#pycharm-interactive-runner)
10. [Additional Tips](#additional-tips)

---

## Introduction
This tutorial will guide you through setting up a robust Python development environment using PyCharm and Anaconda. We'll cover installation steps for different operating systems, verify your existing Python installations, and configure PyCharm for efficient coding.

## Verify Existing Python Installations
Before installing new software, check for any existing Python installations to avoid conflicts.

### Windows
- Open Command Prompt and type: `python --version` or `py --version`.
- Check installed Python versions and uninstall unnecessary ones from the Control Panel.

### Mac
- Open Terminal and type: `python --version` or `python3 --version`.
- To uninstall, remove the Python directories from `/Library/Frameworks/Python.framework/Versions/`.

### Linux
- Open Terminal and type: `python --version` or `python3 --version`.
- Use your package manager to uninstall unnecessary Python versions (e.g., `sudo apt-get remove python`).

## Install Anaconda
Install the latest Anaconda distribution, which includes numerous pre-installed libraries and tools for data science.

### Download Anaconda
- Go to the [Anaconda download page](https://www.anaconda.com/products/distribution) and download the installer for your operating system.

### Installation

#### Windows
- Run the downloaded installer.
- If select "Administrator", then select "Register Anaconda as the system Python" during installation. (recommended)
- If select "Just Me", then check "Add Anaconda to my PATH environment variable" during installation.
- Complete the installation process.

#### Mac
- Open Terminal and run the downloaded `.sh` script: `bash Anaconda3-2023.03-MacOSX-x86_64.sh` (version number may vary).
- Follow the prompts to complete the installation.

#### Linux
- Open Terminal and run the downloaded `.sh` script: `bash Anaconda3-2023.03-Linux-x86_64.sh` (version number may vary).
- Follow the prompts to complete the installation.

### Verify Anaconda Installation
- Open a new terminal window.
- Type `python` and verify the output includes "packaged by Anaconda, Inc."

## Install PyCharm
PyCharm is a powerful IDE specifically designed for Python development.

### PyCharm Editions
PyCharm comes in several editions:
- **Community Edition**: Free and open-source, suitable for pure Python development.
- **Professional Edition**: Paid version with additional features for web development, database management, and more.
- **Educational Edition**: Free for educational purposes, includes features included in the Professional Edition. You can learn more and apply for an educational license [here](https://www.jetbrains.com/community/education/#students).

### Download PyCharm
- Go to the [PyCharm download page](https://www.jetbrains.com/pycharm/download/) and download the appropriate edition for your operating system.

### Installation

#### Windows
- Run the downloaded installer and follow the installation wizard.
- Select the option to "Add PyCharm to context menu (right-click menu)" for easier access.
- Optionally, choose to create a desktop shortcut.

#### Mac
- Open the downloaded `.dmg` file and drag PyCharm to the Applications folder.

#### Linux
- Extract the downloaded tarball and run `./pycharm.sh` from the `bin` subdirectory.

## Configure PyCharm with Anaconda

### Open PyCharm
Create a new project or open an existing one.

### Set Up Anaconda Environment
- Go to `File` > `Settings` (or `PyCharm` > `Preferences` on Mac).
- Navigate to `Project: <project_name>` > `Python Interpreter`.
- Click the gear icon and select `Add`.
- Choose `System Environment` or `Conda Environment` and specify the path to your Anaconda installation.

### Configure Terminal for Conda
- If the `(base)` prefix does not appear in front of the command prompt, set the default terminal to Conda by going to `File` > `Settings` > `Tools` > `Terminal` and setting the shell path to the Conda terminal executable.

## Exclude Data and Output Folders

### Mark as Excluded
1. In the Project tool window, locate the `data` and `output` folders (or other directories containing large files or generated content).
2. Right-click on each folder.
3. Select **Mark Directory as** > **Excluded**.

### Why Exclude These Folders?

Excluding the `data` and `output` directories helps PyCharm avoid indexing unnecessary or large files. Indexing these folders, especially during project loading, can cause PyCharm to significantly slow down or even hang the IDE if the directories contain a large number of files. By excluding these directories, you ensure that PyCharm skips indexing them, which improves performance and reduces load time.

### Modifying the `.idea` Folder

If you prefer not to exclude directories manually through the PyCharm interface, you can modify the `.iml` file inside the `.idea` folder to exclude directories programmatically. This ensures that large folders, such as `data` and `output`, won’t be indexed, preventing the IDE from freezing during the loading process.

To exclude folders, locate the `<content>` tag in the `.iml` file and add the following lines:

```xml
<content url="file://$MODULE_DIR$">
    <excludeFolder url="file://$MODULE_DIR$/data" />
    <excludeFolder url="file://$MODULE_DIR$/output" />
</content>
```

This ensures that PyCharm skips indexing the specified folders, which is essential for maintaining smooth performance when dealing with projects containing large files or datasets.

## Use Symbolic Links for Shared Data

If you have multiple projects that need to share the same data sources, using symbolic links for the `data` folder can save disk space by avoiding multiple copies of the same data. Instead of duplicating the data across projects, create a symbolic link to a shared data source.

To create a symbolic link:

- **On Windows**, use the following command:
  ```bash
  mklink /D data "C:\path\to\shared\data"
  ```

- **On Linux/macOS**, use this command:
  ```bash
  ln -s /path/to/shared/data data
  ```

This way, the `data` folder will point to a shared location, allowing multiple projects to access the same data without consuming additional disk space.

## Using Terminal vs. Jupyter Notebooks to Run Python Scripts

### Terminal
- **Best for Large Projects and Automation**: Use the terminal for running large projects with multiple modules, automating tasks, and handling performance-intensive scripts. It's more suitable for managing virtual environments and integrating with version control systems like Git.

### Jupyter Notebooks
- **Best for Demos and Proof of Concepts**: Ideal for proof of concept, data visualization of demo, and creating well-documented reports. Use notebooks when you need to quickly prototype ideas or demonstrate concepts.

By following these steps, you will have a powerful and efficient Python development environment set up with PyCharm and Anaconda, ready for any data science or development projects.

## Debugging

Effective debugging is crucial for developing robust Python applications. Here are three methods to debug your Python scripts:

### Basic Debugging with `print()` and `exit()`
Use `print()` statements to output variable values and the flow of execution. This method is quick and effective for simple debugging tasks.

Example:
```python
def add(a, b):
    print(f"Adding {a} and {b}")
    result = a + b
    print(f"Result: {result}")
    return result

add(2, 3)
exit()  # Terminate the script here for inspection
```

### Advanced Debugging with `pdb`
The Python debugger (`pdb`) allows for more fine-tuned debugging, such as setting breakpoints and stepping through code.

To use `pdb`:
1. Import `pdb` in your script.
2. Insert `pdb.set_trace()` where you want to start debugging.

Example:
```python
import pdb

def add(a, b):
    pdb.set_trace()  # Start debugging here
    result = a + b
    return result

add(2, 3)
```

### PyCharm Interactive Runner
If you are not using the terminal, PyCharm's interactive runner provides a user-friendly debugging environment with powerful features such as breakpoints, watches, and variable inspection.

To use PyCharm's interactive runner:
1. Set breakpoints by clicking in the gutter next to the line numbers.
2. Right-click your script and select "Debug" to start the debugger.
3. Use the debugging controls to step through your code, inspect variables, and evaluate expressions.

These methods offer a range of options for debugging, from quick checks with `print()` and `exit()`, to detailed inspection with `pdb`, to a comprehensive debugging environment in PyCharm. Choose the method that best fits your debugging needs.

## Additional Tips
- **Using Terminal Instead of PyCharm Runner**:
  - It's recommended to use the Terminal for running scripts to avoid issues with the built-in runner.
  
- **Code Navigation**:
  - One of the advantages of using PyCharm over VSCode is the ability to navigate to definitions with `Ctrl + Left Click`.

- **Educational Licenses**:
  - If you're a student or educator, you can apply for a free educational license for PyCharm Professional Edition through the JetBrains website [here](https://www.jetbrains.com/community/education/#students
