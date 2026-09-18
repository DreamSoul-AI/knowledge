# MongoDB

<h4 align="center">
    <p>
        <a href="README.md">English</a> |
        <b>中文</b>
    </p>
</h4>

## 目录

1. [简介](#简介)
2. [安装 MongoDB 社区版](#安装-mongodb-社区版)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
3. [配置系统路径](#配置系统路径)
4. [修改 MongoDB 配置文件](#修改-mongodb-配置文件)
5. [启动 MongoDB](#启动-mongodb)
6. [安装 MongoDB Compass](#安装-mongodb-compass)
7. [使用 Compass 连接到 MongoDB](#使用-compass-连接到-mongodb)
8. [使用 PyMongo 操作 MongoDB](#使用-pymongo-操作-mongodb)
    - [安装 PyMongo](#安装-pymongo)
    - [连接到 MongoDB](#连接到-mongodb)
    - [基本的 CRUD 操作](#基本的-crud-操作)
    - [高级 PyMongo 方法](#高级-pymongo-方法)
9. [备份和恢复 MongoDB](#备份和恢复-mongodb)
    - [使用 `mongodump` 进行备份](#使用-mongodump-进行备份)
    - [使用 `mongorestore` 进行恢复](#使用-mongorestore-进行恢复)
10. [最佳实践](#最佳实践)

## 简介

MongoDB 是一种流行的 NoSQL 数据库，提供高性能、高可用性和易扩展性。MongoDB Compass 是一个 MongoDB 的图形用户界面，允许用户以可视化方式与数据库和集合进行交互。本教程将指导您在各种平台上设置 MongoDB 社区版和 MongoDB Compass，并展示如何使用 Python 的 PyMongo 库与 MongoDB 进行交互。

## 安装 MongoDB 社区版

### Windows

1. **下载 MongoDB：**
   - 访问 [MongoDB 社区版下载页面](https://www.mongodb.com/try/download/community)。
   - 选择适用于 Windows 的版本并下载 MSI 安装程序。

2. **运行安装程序：**
   - 打开下载的 MSI 文件以启动安装过程。
   - 选择 **自定义** 安装选项以指定安装路径。

3. **自定义安装路径：**
   - 指定 MongoDB 的安装目录，例如 `E:\MongoDB`。

4. **选择安装选项：**
   - **不要将 MongoDB 安装为服务**：
     - 取消选择 "Install MongoDB as a Service" 选项。
   - **不要在此步骤中安装 MongoDB Compass**：
     - 我们稍后将手动安装 MongoDB Compass。

5. **完成安装：**
   - 按照屏幕上的说明操作，点击 **Install** 完成安装。

### macOS

1. **安装 Homebrew**（如果尚未安装）：
   - 打开终端，输入以下命令以安装 Homebrew：
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **通过 Homebrew 安装 MongoDB：**
   - 使用 Homebrew 安装 MongoDB：
     ```bash
     brew tap mongodb/brew
     brew install mongodb-community@7.0
     ```

3. **创建所需目录：**
   - MongoDB 将使用默认路径来存储数据和日志。如果您希望自定义，可以手动创建必要的目录并更新配置文件。

### Linux

1. **安装 MongoDB：**
   - 打开终端，按照您的特定 Linux 发行版的说明进行操作：

   **Debian/Ubuntu:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y mongodb
   ```

   **Fedora:**
   ```bash
   sudo dnf install -y mongodb
   ```

2. **创建所需目录：**
   - MongoDB 将使用默认路径来存储数据和日志。如果您希望自定义，可以手动创建必要的目录并更新配置文件。

3. **启动 MongoDB：**
   - 使用以下命令启动 MongoDB：
     ```bash
     sudo systemctl start mongod
     ```

## 配置系统路径

安装 MongoDB 后，您需要将 MongoDB 的 `bin` 目录添加到系统的 `Path` 环境变量中，以便可以从命令行运行 `mongod`。

1. **将 MongoDB 添加到系统路径：**
   - **Windows**：打开 **控制面板 > 系统和安全 > 系统 > 高级系统设置**，然后点击 **环境变量**。将 MongoDB 的 `bin` 文件夹路径（如 `E:\MongoDB\Server\7.0\bin`）添加到 `Path` 变量中。
   - **macOS**：通过编辑 shell 配置文件（`~/.bash_profile`, `~/.zshrc` 等）将 MongoDB `bin` 目录添加到您的 PATH 中：
     ```bash
     export PATH="/usr/local/opt/mongodb-community@7.0/bin:$PATH"
     ```
   - **Linux**：通过编辑 shell 配置文件（`~/.bashrc`, `~/.zshrc` 等）将 MongoDB `bin` 目录添加到您的 PATH 中：
     ```bash
     export PATH="/usr/bin/mongodb:$PATH"
     ```

## 修改 MongoDB 配置文件

MongoDB 使用配置文件（`mongod.cfg`）来定义其行为，例如存储数据和日志的位置。

1. **找到配置文件：**
   - 导航到 MongoDB 的 `bin` 目录（例如，在 Windows 上为 `E:\MongoDB\Server\7.0\bin\`）。

2. **编辑 `mongod.cfg`：**
   - 在文本编辑器中打开 `mongod.cfg`（例如，在 Windows 上使用 Notepad，或在 macOS/Linux 上使用 Vim/Nano）。
   - 修改文件如下：

     ```yaml
     # 数据存储位置。
     storage:
       dbPath: E:\MongoDB\data

     # 日志存储位置。
     systemLog:
       destination: file
       logAppend: true
       path: E:\MongoDB\log\mongod.log
     ```

   - 确保 `dbPath` 和 `path` 参数正确设置为 MongoDB 存储数据和日志的目录。

3. **创建所需目录：**
   - 在 MongoDB 目录中手动创建 `data` 和 `log` 文件夹（在 Windows 上为 `E:\MongoDB\data` 和 `E:\MongoDB\log`，在 macOS 上为 `/usr/local/var/mongodb`，在 Linux 上为 `/var/lib/mongo`）。

## 启动 MongoDB

要启动 MongoDB，请使用命令提示符或终端并指向配置文件。

1. **启动 MongoDB：**
   - **Windows**：打开命令提示符并运行：
     ```bash
     mongod --config E:\MongoDB\Server\7.0\bin\mongod.cfg
     ```
   - **macOS/Linux**：使用默认配置启动 MongoDB：
     ```bash
     mongod --config /usr/local/etc/mongod.conf
     ```

   - 如果命令运行没有错误，MongoDB 就已成功启动。通常命令提示符中没有输出表示 MongoDB 正在正常运行。

## 安装 MongoDB Compass

MongoDB Compass 是用于管理 MongoDB 数据库的图形用户界面。

1. **下载 MongoDB Compass：**
   - 访问 [MongoDB Compass 下载页面](https://www.mongodb.com/try/download/compass)。
   - 下载适用于您的系统的安装程序。

2. **安装 MongoDB Compass：**
   - 运行下载的安装程序并按照屏幕上的说明完成安装。

## 使用 Compass 连接到 MongoDB

安装 MongoDB Compass 后，您可以使用它连接到本地的 MongoDB 实例。

1. **打开 MongoDB Compass：**
   - 从开始菜单（Windows）、Launchpad（macOS）或应用菜单（Linux）启动 MongoDB Compass。

2. **连接到 MongoDB：**
   - 在 MongoDB Compass 中，默认连接设置（localhost:27017）适用于本地 MongoDB 实例。
   - 点击 **Connect** 建立与 MongoDB 服务器的连接。

3. **管理您的数据库：**
   - 连接成功后，您可以开始使用 MongoDB Compass 界面管理您的数据库、集合和文档。

## 使用 PyMongo 操作 MongoDB

PyMongo 是一个 Python 分发包，包含与 MongoDB 一起使用的工具。以下步骤将指导您安装 PyMongo 并执行基本的 CRUD 操作，以及更高级的数据操作任务。

### 安装 PyMongo

1. **安装 PyMongo：**
   - 使用 pip 安装 PyMongo：
     ```bash
     pip install pymongo
     ```

### 连接到 MongoDB

1. **导入 PyMongo 库：**
   ```python
   from pymongo import MongoClient
   ```

2. **连接到 MongoDB 服务器：**
   ```python
   client = MongoClient('localhost', 27017)
   ```

3. **访问数据库：**
   ```python
   db = client['mydatabase']
   ```

4. **访问集合：**
   ```python
   collection = db['mycollection']
   ``

`

### 基本的 CRUD 操作

1. **插入文档：**
   ```python
   document = {"name": "John", "age": 30, "city": "New York"}
   collection.insert_one(document)
   ```

2. **查找文档：**
   ```python
   result = collection.find_one({"name": "John"})
   print(result)
   ```


3. **更新文档：**
   ```python
   query = {"name": "John"}
   new_values = {"$set": {"age": 31}}
   collection.update_one(query, new_values)
   ```

4. **删除文档：**
   ```python
   query = {"name": "John"}
   collection.delete_one(query)
   ```

### 高级 PyMongo 方法

1. **使用 `insert_many()` 插入多个文档：**
   - 将多个文档插入到集合中。
   - **示例**：
     ```python
     documents = [
         {"name": "Alice", "age": 24},
         {"name": "Bob", "age": 31}
     ]
     collection.insert_many(documents)
     ```

2. **使用 `update_many()` 更新多个文档：**
   - 更新所有符合筛选条件的文档。
   - **示例**：
     ```python
     collection.update_many(
         {"age": {"$lt": 30}}, 
         {"$set": {"status": "young"}}
     )
     ```

3. **使用 `replace_one()` 替换文档：**
   - 用新文档替换符合筛选条件的单个文档。
   - **示例**：
     ```python
     collection.replace_one(
         {"name": "Alice"}, 
         {"name": "Alice", "age": 32, "city": "Los Angeles"}
     )
     ```

4. **使用 `count_documents()` 计数文档：**
   - 统计符合筛选条件的文档数量。
   - **示例**：
     ```python
     count = collection.count_documents({"age": {"$gt": 30}})
     print(count)
     ```

5. **使用 `distinct()` 获取字段的不同值：**
   - 查找指定字段在集合中所有文档的不同值。
   - **示例**：
     ```python
     distinct_ages = collection.distinct("age")
     print(distinct_ages)
     ```

6. **使用 `aggregate()` 聚合：**
   - 执行聚合操作，允许您处理数据并返回计算结果。
   - **示例**：
     ```python
     pipeline = [
         {"$match": {"age": {"$gt": 20}}},
         {"$group": {"_id": "$city", "average_age": {"$avg": "$age"}}}
     ]
     results = collection.aggregate(pipeline)
     for result in results:
         print(result)
     ```

7. **使用 `create_index()` 创建索引：**
   - 在集合上创建索引以提高查询性能。
   - **示例**：
     ```python
     collection.create_index([("name", 1)])
     ```

8. **使用 `drop()` 删除集合：**
   - 删除整个集合，删除集合中的所有文档。
   - **示例**：
     ```python
     collection.drop()
     ```

9. **使用 `bulk_write()` 执行批量操作：**
   - 在单个批量操作中执行多个写操作，对于大量操作，这可能更高效。
   - **示例**：
     ```python
     from pymongo import InsertOne, DeleteOne, ReplaceOne

     operations = [
         InsertOne({"name": "Henry", "age": 33}),
         DeleteOne({"name": "Alice"}),
         ReplaceOne({"name": "Grace"}, {"name": "Grace", "age": 32})
     ]

     result = collection.bulk_write(operations)
     ```

10. **使用 `find_one_and_update()` 查找并修改：**
    - 查找单个文档并更新它，根据提供的选项返回原始或更新后的文档。
    - **示例**：
      ```python
      result = collection.find_one_and_update(
          {"name": "Charlie"}, 
          {"$set": {"age": 36}},
          return_document=True
      )
      print(result)
      ```

11. **使用 `find_one_and_replace()` 查找并替换：**
    - 查找单个文档并用另一个文档替换它，返回原始或新文档。
    - **示例**：
      ```python
      result = collection.find_one_and_replace(
          {"name": "Charlie"}, 
          {"name": "Charlie", "age": 37, "city": "Boston"}
      )
      print(result)
      ```

12. **使用 `find_one_and_delete()` 查找并删除：**
    - 查找单个文档并删除它，返回被删除的文档。
    - **示例**：
      ```python
      result = collection.find_one_and_delete({"name": "Diana"})
      print(result)
      ```

## 备份和恢复 MongoDB

我们需要使用 [MongoDB 数据库工具](https://www.mongodb.com/try/download/database-tools)

### 使用 `mongodump` 进行备份

`mongodump` 是一个用于创建 MongoDB 数据备份的工具。它将数据导出为 BSON 格式，这是 MongoDB 的原生数据格式。

1. **使用 `mongodump` 创建备份：**

   以下命令将把整个数据库备份为 BSON 文件：

   ```bash
   mongodump --uri="mongodb://localhost:27017" --out=/path/to/backup/directory
   ```

   - `--uri`：MongoDB 连接 URI（示例中为 localhost 和默认端口）。
   - `--out`：指定备份文件存储的目录路径。

2. **备份特定数据库或集合：**

   如果只想备份特定的数据库或集合，请使用以下命令：

   - 备份指定的数据库：
     ```bash
     mongodump --uri="mongodb://localhost:27017" --db=your_database --out=/path/to/backup/directory
     ```

   - 备份数据库中的特定集合：
     ```bash
     mongodump --uri="mongodb://localhost:27017" --db=your_database --collection=your_collection --out=/path/to/backup/directory
     ```

   如果想压缩备份文件，可以使用 `--gzip` 标志。

### 使用 `mongorestore` 进行恢复

`mongorestore` 是一个用于从 `mongodump` 创建的备份中恢复数据的工具。

1. **恢复数据库：**

   使用以下命令从备份恢复整个数据库：

   ```bash
   mongorestore --uri="mongodb://localhost:27017" --dir=/path/to/backup/directory/your_database
   ```

   - `--uri`：MongoDB 连接 URI（示例中为 localhost 和默认端口）。
   - `--dir`：备份文件所在的目录路径。

2. **恢复特定集合：**

   使用以下命令从备份恢复特定集合：

   ```bash
   mongorestore --uri="mongodb://localhost:27017" --db=your_database --collection=your_collection --dir=/path/to/backup/directory/your_database/your_collection.bson
   ```

3. **其他选项：**

   - `--drop`：在恢复备份前，删除现有的集合。
   - `--gzip`：如果备份文件是使用 gzip 压缩的，可以使用此选项。

有关更多信息，请参阅官方 [MongoDB Database Tools 文档](https://www.mongodb.com/zh-cn/docs/database-tools/)，并在 [这里](https://gist.github.com/diaoenmao/32b30c634658fdcdb02eea039e1d473d) 查找自动化备份和恢复过程的 `bash` 脚本。

## 最佳实践

### 确保数据和日志目录的权限
始终确保为 `dbPath` 和 `systemLog` 指定的目录具有适当的权限，以便 MongoDB 可以读取和写入数据和日志。

### 定期备份
定期备份您的 MongoDB 数据库，以避免数据丢失。您可以使用 `mongodump` 创建备份，并使用 `mongorestore` 恢复它们。

### 监控 MongoDB 性能
使用 MongoDB Compass 或 MongoDB Atlas 等工具监控 MongoDB 服务器的性能，包括内存使用、查询性能和数据库大小。
