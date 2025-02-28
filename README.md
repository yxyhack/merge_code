## 📜 README (English)

# File Merger and Comment Remover

This script merges text files from a specified directory, removes comments from supported code files, and optionally splits the output based on a specified size limit.

### ✨ Features
- Recursively scans a directory and merges text-based files.
- Removes `//` and `/* */` comments from programming languages.
- Skips binary files and hidden files.
- Supports optional file size limit for split output (`--part`).
- Allows excluding specific directories (`--exclude`).

### 📦 Supported File Types
- Programming languages: Python, JavaScript, C, Java, Rust, etc.
- Config files: `.ini`, `.yaml`, `.json`, `.toml`, `.conf`, etc.
- Markup files: `.md`, `.html`, `.xml`, etc.
- Other text-based files like `.log`, `.csv`, `.sql`.

### 🚀 Usage

#### 1. Basic Usage
```sh
python merge_files.py /path/to/directory
```
This will merge all supported text files in the directory into `list_1.txt`.

#### 2. Set a File Size Limit (Splitting)
```sh
python merge_files.py /path/to/directory --part 5000000
```
This will split the merged output into multiple files, each with a maximum size of ~5MB.

#### 3. Exclude Specific Directories
```sh
python merge_files.py /path/to/directory --exclude node_modules,venv
```
This will ignore files inside `node_modules` and `venv` folders.

### ⚠️ Notes
- Hidden files and binary files are ignored.
- The script overwrites `list_x.txt` files inside the directory.

---

## 📜 README (中文)

# 文件合并与注释移除工具

该脚本用于合并指定目录下的文本文件，同时移除代码文件中的注释，并可根据指定大小拆分输出。

### ✨ 功能特点
- 递归扫描目录并合并所有文本文件。
- 移除代码文件中的 `//` 和 `/* */` 注释。
- 跳过二进制文件和隐藏文件。
- 支持文件大小限制（`--part`）自动拆分。
- 可指定排除目录（`--exclude`）。

### 📦 支持的文件类型
- 代码文件：Python、JavaScript、C、Java、Rust 等。
- 配置文件：`.ini`、`.yaml`、`.json`、`.toml`、`.conf` 等。
- 标记语言文件：`.md`、`.html`、`.xml` 等。
- 其他文本文件：`.log`、`.csv`、`.sql` 等。

### 🚀 使用方法

#### 1. 基本使用
```sh
python merge_files.py /path/to/directory
```
将合并目录中的所有支持文件，并输出至 `list_1.txt`。

#### 2. 设置文件大小限制（自动拆分）
```sh
python merge_files.py /path/to/directory --part 5000000
```
如果合并后文件大于 5MB，将拆分成多个文件。

#### 3. 排除指定目录
```sh
python merge_files.py /path/to/directory --exclude node_modules,venv
```
忽略 `node_modules` 和 `venv` 目录中的文件。

### ⚠️ 注意
- 隐藏文件和二进制文件会自动忽略。
- 生成的 `list_x.txt` 文件可能会被覆盖，请注意备份。
