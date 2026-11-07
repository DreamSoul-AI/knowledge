# Python Environment Management

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
Inspect, prepare and troubleshoot the Python environment for an actual project command. Deliver a verified environment or an evidence-based diagnosis; a diagnosis-only request does not authorize repair. The invocation name remains `python-environment`. Follow existing project tools, versions and environments first; the PyCharm/Anaconda route below is optional background, not a universal installation requirement.

### Use and verify
See the focused [environment operations reference](environment-operations.md) for manager selection, command side effects and handoff. In particular, `uv run` may synchronize dependencies; a passing `pip check` does not establish native-runtime or application health. For diagnosis, prefer the confirmed existing interpreter without automatic sync or repair.

Optionally supply a project path, interpreter/environment, applicable requirements and target command. Otherwise read the current project's declarations. A useful request is: “Check this project's environment, reuse what exists, run its lightweight tests, and do not install or upgrade dependencies.”

Use the selected interpreter directly to inspect `sys.executable`, `sys.prefix`, `sys.base_prefix`, package import locations and `-m pip --version`. Equal versions or an activation prompt do not establish interpreter identity. Direct invocation selects the interpreter without defaulting to global PATH changes, but Conda or native extensions may still require their runtime setup. See the [Python venv documentation](https://docs.python.org/3/library/venv.html).

Read dependency files before executing them. When pip is appropriate, use the confirmed interpreter's full path with `-m pip`; otherwise follow the project's declared manager. A requirements file can contain builds, editable installs and remote sources, and need not be a complete lock. See the [pip user guide](https://pip.pypa.io/en/stable/user_guide/).

Respect pins, lock semantics and hashes. Do not bypass failure by relaxing versions, disabling checks or installing globally. See [pip hash-checking guidance](https://pip.pypa.io/en/stable/topics/secure-installs/). A failed install is not guaranteed to be transactional: inspect affected packages rather than assuming nothing changed.

For missing or broken environments, distinguish interpreter failure, missing packages, project import paths and IDE/kernel selection. Preserve the old directory and user files; recover separately within the authorized scope or ask before replacement. Prefer declared source-layout/test entry points over unnecessary installation. Report the actual environment, changes, runnable command, result and unresolved limits; a small successful test does not establish all backends or workflows.

### Fill gaps and hand off
Judge readiness against the target command, separating blocking gaps, optional features and unrelated findings. Reuse a working environment without cleanup or upgrades. Before a needed change, state the evidence, smallest sufficient action, affected scope and verification command; execute within existing authorization through the project's manager and constraints. Do not cherry-pick around a lockfile or install all extras.

Return the environment/manager, cwd and copyable command, actual change or none, observed result and remaining limits. Separate proposals from executed changes and successful execution from diagnosis only. For recreation, reference existing project declarations and locks rather than dumping all shared-environment packages. See the decision and handoff examples in [Environment operations](environment-operations.md).

## Verify Existing Python Installations
Before installing new software, check for any existing Python installations to avoid conflicts.

### Windows
- Open Command Prompt and type: `python --version` or `py --version`.
- Check the interpreter path and required version; preserve installations used by the OS or other projects instead of uninstalling as routine diagnosis.

### Mac
- Open Terminal and type: `python --version` or `python3 --version`.
- Identify the interpreter and project environment; do not directly delete system or third-party-managed Python directories.

### Linux
- Open Terminal and type: `python --version` or `python3 --version`.
- Preserve Python used by the OS and package manager. Prefer an isolated project environment over uninstalling system Python.

## Install Anaconda
Use this route only when the project adopts Conda or the user chooses it. Skip it when a suitable environment already exists; check the required Python version and platform rather than automatically downloading a large distribution or upgrading to the newest release.

### Download Anaconda
- Go to the [Anaconda download page](https://www.anaconda.com/products/distribution) and download the installer for your operating system.

### Installation

#### Windows
- Run the downloaded installer.
- Select the installation scope for the actual user and project; do not default to registering system Python or changing global PATH.
- Keep existing terminal and project defaults unless changing them is within the requested scope.
- Complete the installation process.

#### Mac
- Select the installer for the actual processor architecture and run `bash` with its downloaded `.sh` filename, not an old release or another architecture's filename.
- Follow the prompts to complete the installation.

#### Linux
- Select the installer for the actual OS and processor architecture and run `bash` with its downloaded `.sh` filename.
- Follow the prompts to complete the installation.

### Verify Anaconda Installation
- Open a new terminal window.
- Type `python` and verify the output includes "packaged by Anaconda, Inc."

## Install PyCharm
PyCharm is a powerful IDE specifically designed for Python development.

### PyCharm Editions
Check the current product and licensing information on the [official download page](https://www.jetbrains.com/pycharm/download/) rather than treating historical edition names as current requirements. An existing suitable editor is sufficient.

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
- For a Conda project, check that the terminal and IDE use the intended environment. A missing `(base)` prefix alone is not a reason to change the default shell. Menu names vary; select the actual project interpreter rather than relying on a fixed menu path.

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
  - Terminal, IDE runner and Notebook are all valid entry points. Diagnose their interpreter, working directory, environment variables and kernel separately instead of disabling one by default.
  
- **Code Navigation**:
  - Use navigation, completion and debugging supported by the chosen editor and extensions; a shortcut is not a reason to change environment managers.

- **Educational Licenses**:
  - Check current eligibility and terms on the JetBrains [education page](https://www.jetbrains.com/community/education/#students).
