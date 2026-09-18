# MongoDB

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="README_zh.md">中文</a>
    </p>
</h4>

## Table of Contents

1. [Introduction](#introduction)
2. [Installation of MongoDB Community Edition](#installation-of-mongodb-community-edition)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
3. [Configuration of System Path](#configuration-of-system-path)
4. [Modification of MongoDB Configuration File](#modification-of-mongodb-configuration-file)
5. [Starting MongoDB](#starting-mongodb)
6. [Installation of MongoDB Compass](#installation-of-mongodb-compass)
7. [Connecting to MongoDB Using Compass](#connecting-to-mongodb-using-compass)
8. [Using MongoDB with PyMongo](#using-mongodb-with-pymongo)
    - [Installing PyMongo](#installing-pymongo)
    - [Connecting to MongoDB](#connecting-to-mongodb)
    - [Basic CRUD Operations](#basic-crud-operations)
    - [Advanced PyMongo Methods](#advanced-pymongo-methods)
9. [Backup and Restore MongoDB](#backup-and-restore-mongodb)
    - [Using `mongodump` for Backup](#using-mongodump-for-backup)
    - [Using `mongorestore` for Restore](#using-mongorestore-for-restore)
10. [Best Practices](#best-practices)

## Introduction

MongoDB is a popular NoSQL database that provides high performance, high availability, and easy scalability. MongoDB Compass is a graphical user interface for MongoDB that allows users to interact with their databases and collections visually. This tutorial will guide you through setting up MongoDB Community Edition and MongoDB Compass on various platforms and show you how to interact with MongoDB using Python's PyMongo library.

## Installation of MongoDB Community Edition

### Windows

1. **Download MongoDB:**
   - Visit the [MongoDB Community Edition download page](https://www.mongodb.com/try/download/community).
   - Select the appropriate version for Windows and download the MSI installer.

2. **Run the Installer:**
   - Open the downloaded MSI file to start the installation process.
   - Choose the **Custom** setup option to specify the installation path.

3. **Customize Installation Path:**
   - Specify the directory where MongoDB will be installed, for example, `E:\MongoDB`.

4. **Select Installation Options:**
   - **Do not install MongoDB as a service**:
     - Uncheck the "Install MongoDB as a Service" option.
   - **Do not install MongoDB Compass** during this step:
     - We will manually install MongoDB Compass later.

5. **Complete the Installation:**
   - Follow the on-screen instructions and click **Install** to complete the process.

### macOS

1. **Install Homebrew** (if not already installed):
   - Open Terminal and enter the following command to install Homebrew:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **Install MongoDB via Homebrew:**
   - Use Homebrew to install MongoDB:
     ```bash
     brew tap mongodb/brew
     brew install mongodb-community@7.0
     ```

3. **Create Required Directories:**
   - MongoDB will use the default paths for storing data and logs. If you want to customize, manually create the necessary directories and update the configuration file.

### Linux

1. **Install MongoDB:**
   - Open Terminal and follow the instructions for your specific Linux distribution:

   **Debian/Ubuntu:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y mongodb
   ```

   **Fedora:**
   ```bash
   sudo dnf install -y mongodb
   ```

2. **Create Required Directories:**
   - MongoDB will use the default paths for storing data and logs. If you want to customize, manually create the necessary directories and update the configuration file.

3. **Start MongoDB:**
   - Use the following command to start MongoDB:
     ```bash
     sudo systemctl start mongod
     ```

## Configuration of System Path

After installing MongoDB, you need to add MongoDB's `bin` directory to your system's `Path` environment variable to run `mongod` from the command line.

1. **Add MongoDB to System Path:**
   - **Windows**: Open **Control Panel > System and Security > System > Advanced system settings**, then click **Environment Variables**. Add the path to MongoDB’s `bin` folder, e.g., `E:\MongoDB\Server\7.0\bin`, to the `Path` variable.
   - **macOS**: Add the MongoDB `bin` directory to your PATH by editing your shell profile file (`~/.bash_profile`, `~/.zshrc`, etc.):
     ```bash
     export PATH="/usr/local/opt/mongodb-community@7.0/bin:$PATH"
     ```
   - **Linux**: Add the MongoDB `bin` directory to your PATH by editing your shell profile file (`~/.bashrc`, `~/.zshrc`, etc.):
     ```bash
     export PATH="/usr/bin/mongodb:$PATH"
     ```

## Modification of MongoDB Configuration File

MongoDB uses a configuration file (`mongod.cfg`) to define its behavior, such as where to store data and logs.

1. **Locate the Configuration File:**
   - Navigate to MongoDB’s `bin` directory (e.g., `E:\MongoDB\Server\7.0\bin\` on Windows).

2. **Edit `mongod.cfg`:**
   - Open `mongod.cfg` in a text editor (e.g., Notepad on Windows or Vim/Nano on macOS/Linux).
   - Modify the file as follows:

     ```yaml
     # Where and how to store data.
     storage:
       dbPath: E:\MongoDB\data

     # Where to write logging data.
     systemLog:
       destination: file
       logAppend: true
       path: E:\MongoDB\log\mongod.log
     ```

   - Ensure that the `dbPath` and `path` parameters are correctly set to the directories where MongoDB will store data and logs.

3. **Create Required Directories:**
   - Manually create the `data` and `log` folders in the MongoDB directory (`E:\MongoDB\data` and `E:\MongoDB\log` on Windows, `/usr/local/var/mongodb` on macOS, and `/var/lib/mongo` on Linux).

## Starting MongoDB

To start MongoDB, use the command prompt or terminal and point to the configuration file.

1. **Start MongoDB:**
   - **Windows**: Open Command Prompt and run:
     ```bash
     mongod --config E:\MongoDB\Server\7.0\bin\mongod.cfg
     ```
   - **macOS/Linux**: Start MongoDB using the default configuration:
     ```bash
     mongod --config /usr/local/etc/mongod.conf
     ```

   - If the command runs without errors, MongoDB is successfully started. The absence of output in the command prompt usually indicates that MongoDB is running correctly.

## Installation of MongoDB Compass

MongoDB Compass is a GUI for managing your MongoDB databases.

1. **Download MongoDB Compass:**
   - Visit the [MongoDB Compass download page](https://www.mongodb.com/try/download/compass).
   - Download the installer for your system.

2. **Install MongoDB Compass:**
   - Run the downloaded installer and follow the on-screen instructions to complete the installation.

## Connecting to MongoDB Using Compass

Once MongoDB Compass is installed, you can use it to connect to your local MongoDB instance.

1. **Open MongoDB Compass:**
   - Launch MongoDB Compass from the Start menu (Windows), Launchpad (macOS), or your application menu (Linux).

2. **Connect to MongoDB:**
   - In MongoDB Compass, the default connection settings (localhost:27017) should work for a local MongoDB instance.
   - Click **Connect** to establish a connection to your MongoDB server.

3. **Manage Your Databases:**
   - Once connected, you can start managing your databases, collections, and documents using the MongoDB Compass interface.

## Using MongoDB with PyMongo

PyMongo is a Python distribution containing tools for working with MongoDB. The following steps will guide you through installing PyMongo and performing basic CRUD operations, as well as more advanced data manipulation tasks.

### Installing PyMongo

1. **Install PyMongo:**
   - Use pip to install PyMongo:
     ```bash
     pip install pymongo
     ```

### Connecting to MongoDB

1. **Import the PyMongo Library:**
   ```python
   from pymongo import MongoClient
   ```

2. **Connect to the MongoDB Server:**
   ```python
   client = MongoClient('localhost', 27017)
   ```

3. **Access a Database:**
   ```python
   db = client['mydatabase']
   ```

4. **Access a Collection:**
   ```python
   collection = db['mycollection']
   ```

### Basic CRUD Operations

1. **Insert a Document:**
   ```python
   document = {"name": "John", "age": 30, "city": "New York"}
   collection.insert_one(document)
   ```

2. **Find a Document:**
   ```python
   result = collection.find_one({"name": "John"})
   print(result)
   ```


3. **Update a Document:**
   ```python
   query = {"name": "John"}
   new_values = {"$set": {"age": 31}}
   collection.update_one(query, new_values)
   ```

4. **Delete a Document:**
   ```python
   query = {"name": "John"}
   collection.delete_one(query)
   ```

### Advanced PyMongo Methods

1. **Insert Multiple Documents with `insert_many()`:**
   - Inserts multiple documents into a collection.
   - **Example**:
     ```python
     documents = [
         {"name": "Alice", "age": 24},
         {"name": "Bob", "age": 31}
     ]
     collection.insert_many(documents)
     ```

2. **Update Multiple Documents with `update_many()`:**
   - Updates all documents that match the filter criteria.
   - **Example**:
     ```python
     collection.update_many(
         {"age": {"$lt": 30}}, 
         {"$set": {"status": "young"}}
     )
     ```

3. **Replace a Document with `replace_one()`:**
   - Replaces a single document that matches the filter criteria with a new document.
   - **Example**:
     ```python
     collection.replace_one(
         {"name": "Alice"}, 
         {"name": "Alice", "age": 32, "city": "Los Angeles"}
     )
     ```

4. **Count Documents with `count_documents()`:**
   - Counts the number of documents that match the filter criteria.
   - **Example**:
     ```python
     count = collection.count_documents({"age": {"$gt": 30}})
     print(count)
     ```

5. **Distinct Values with `distinct()`:**
   - Finds the distinct values for a specified field across a single collection.
   - **Example**:
     ```python
     distinct_ages = collection.distinct("age")
     print(distinct_ages)
     ```

6. **Aggregation with `aggregate()`:**
   - Performs aggregation operations, which allow you to process data and return computed results.
   - **Example**:
     ```python
     pipeline = [
         {"$match": {"age": {"$gt": 20}}},
         {"$group": {"_id": "$city", "average_age": {"$avg": "$age"}}}
     ]
     results = collection.aggregate(pipeline)
     for result in results:
         print(result)
     ```

7. **Create an Index with `create_index()`:**
   - Creates an index on the collection to improve query performance.
   - **Example**:
     ```python
     collection.create_index([("name", 1)])
     ```

8. **Drop a Collection with `drop()`:**
   - Drops the entire collection, deleting all documents within it.
   - **Example**:
     ```python
     collection.drop()
     ```

9. **Bulk Operations with `bulk_write()`:**
   - Performs multiple write operations in a single bulk operation, which can be more efficient for large sets of operations.
   - **Example**:
     ```python
     from pymongo import InsertOne, DeleteOne, ReplaceOne

     operations = [
         InsertOne({"name": "Henry", "age": 33}),
         DeleteOne({"name": "Alice"}),
         ReplaceOne({"name": "Grace"}, {"name": "Grace", "age": 32})
     ]

     result = collection.bulk_write(operations)
     ```

10. **Find and Modify with `find_one_and_update()`:**
    - Finds a single document and updates it, returning the original or updated document depending on the options provided.
    - **Example**:
      ```python
      result = collection.find_one_and_update(
          {"name": "Charlie"}, 
          {"$set": {"age": 36}},
          return_document=True
      )
      print(result)
      ```

11. **Find and Replace with `find_one_and_replace()`:**
    - Finds a single document and replaces it with another document, returning the original or new document.
    - **Example**:
      ```python
      result = collection.find_one_and_replace(
          {"name": "Charlie"}, 
          {"name": "Charlie", "age": 37, "city": "Boston"}
      )
      print(result)
      ```

12. **Find and Delete with `find_one_and_delete()`:**
    - Finds a single document and deletes it, returning the deleted document.
    - **Example**:
      ```python
      result = collection.find_one_and_delete({"name": "Diana"})
      print(result)
      ```

## Backup and Restore MongoDB

MongoDB provides a set of utilities for backing up and restoring databases. You can use the `mongodump` and `mongorestore` commands to perform these operations. These tools export and import data in BSON format, MongoDB's native format. You can download the necessary tools from the [MongoDB Database Tools page](https://www.mongodb.com/try/download/database-tools).

### Using `mongodump` for Backup

`mongodump` is a utility that creates backups of MongoDB data in BSON format. Here's how to use it:

#### 1. **Create a Backup with `mongodump`:**

To dump the entire database into BSON files:

```bash
mongodump --uri="mongodb://localhost:27017" --out=/path/to/backup/directory
```

- `--uri`: MongoDB connection URI (the default localhost with port 27017 is used in the example).
- `--out`: Path to the directory where the dump will be stored.

#### 2. **Backup Specific Database or Collection:**

To backup specific databases or collections, use the following commands:

- **Dump a Specific Database:**

  ```bash
  mongodump --uri="mongodb://localhost:27017" --db=your_database --out=/path/to/backup/directory
  ```

- **Dump a Specific Collection from a Database:**

  ```bash
  mongodump --uri="mongodb://localhost:27017" --db=your_database --collection=your_collection --out=/path/to/backup/directory
  ```

- **Compress the Backup Files:**  
  You can use the `--gzip` flag to compress the backup files.

  ```bash
  mongodump --uri="mongodb://localhost:27017" --db=your_database --out=/path/to/backup/directory --gzip
  ```

### Using `mongorestore` for Restore

`mongorestore` is a utility for restoring data from backups created by `mongodump`. You can restore the full database or specific collections as needed.

#### 1. **Restore a Database:**

To restore a database from a dump:

```bash
mongorestore --uri="mongodb://localhost:27017" --dir=/path/to/backup/directory/your_database
```

- `--uri`: MongoDB connection URI (the default localhost with port 27017 is used).
- `--dir`: Path to the directory containing the backup.

#### 2. **Restore a Specific Collection:**

To restore a specific collection from a backup:

```bash
mongorestore --uri="mongodb://localhost:27017" --db=your_database --collection=your_collection --dir=/path/to/backup/directory/your_database/your_collection.bson
```

#### 3. **Additional Options:**

- `--drop`: This option drops the existing collections before restoring the backup. Useful if you want to replace the current data.

  ```bash
  mongorestore --uri="mongodb://localhost:27017" --drop --dir=/path/to/backup/directory/your_database
  ```

- `--gzip`: Use this option if the backup was compressed with gzip.

  ```bash
  mongorestore --uri="mongodb://localhost:27017" --dir=/path/to/backup/directory --gzip
  ```

For further details on these tools, visit the [MongoDB database-tools documentation](https://www.mongodb.com/docs/database-tools/).

You can also automate the backup and restore process using a Bash script. Find a sample script for automating these tasks [here](https://gist.github.com/diaoenmao/32b30c634658fdcdb02eea039e1d473d).

## Best Practices

### Ensure Data and Log Directory Permissions
Always ensure that the directories specified for `dbPath` and `systemLog` have the appropriate permissions for MongoDB to read and write data and logs.

### Regular Backups
Regularly back up your MongoDB databases to avoid data loss. You can use `mongodump` to create backups and `mongorestore` to restore them.

### Monitor MongoDB Performance
Use tools like MongoDB Compass or MongoDB Atlas to monitor the performance of your MongoDB server, including memory usage, query performance, and database size.
