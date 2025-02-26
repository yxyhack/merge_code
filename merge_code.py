import os
import sys
import re

def remove_comments(content):
    """移除代码中的注释，包括 // 和 /* */"""
    # 去除单行注释 (//)
    content = re.sub(r'//.*', '', content)
    # 去除多行注释 (/* ... */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    return content

def is_text_file(filename):
    """判断文件是否为文本类型文件"""
    text_extensions = {
        # 通用文本文件
        '.txt', '.log', '.csv', '.tsv',
        
        # 标记语言
        '.md', '.markdown', '.rst', '.xml', '.html', '.htm', '.xhtml',
        '.yaml', '.yml', '.json', '.jsonl',
        
        # 配置文件
        '.ini', '.conf', '.cfg', '.config', '.properties', '.prop',
        '.env', '.toml', '.cnf', '.dist', '.editorconfig',
        
        # 脚本语言
        '.py', '.pyw', '.pyx',                  # Python
        '.rb', '.rbw', '.rake',                 # Ruby
        '.pl', '.pm', '.t',                     # Perl
        '.php', '.phtml',                       # PHP
        '.sh', '.bash', '.zsh', '.fish',        # Shell
        '.js', '.jsx', '.ts', '.tsx', '.mjs',   # JavaScript/TypeScript
        '.lua', '.tcl',                         # 其他脚本
        
        # 编译型语言
        '.c', '.h',                             # C
        '.cpp', '.cc', '.cxx', '.hpp', '.hh',   # C++
        '.java',                                # Java
        '.cs',                                  # C#
        '.go',                                  # Go
        '.rs',                                  # Rust
        '.swift',                               # Swift
        '.scala',                               # Scala
        '.kt', '.kts',                          # Kotlin
        '.dart',                                # Dart
        '.f', '.f90', '.f95', '.f03', '.f08',  # Fortran
        '.pas',                                 # Pascal
        '.erl', '.hrl',                         # Erlang
        '.ex', '.exs',                          # Elixir
        '.hs', '.lhs',                          # Haskell
        
        # Web 相关
        '.css', '.scss', '.sass', '.less',
        '.vue', '.svelte',
        
        # 数据库
        '.sql',
        
        # 其他配置文件
        '.gitignore', '.gitattributes',         # Git
        '.dockerignore',                        # Docker
        '.makefile', '.mk'                      # Make
    }
    return os.path.splitext(filename)[1].lower() in text_extensions

def merge_files(source_dir, max_size=None, exclude_dirs=None):
    # 检查目录是否存在
    if not os.path.exists(source_dir):
        print("请提供有效的目录路径。")
        return

    # 将排除目录列表转换为小写，方便后续忽略大小写比较
    exclude_dirs = [d.lower() for d in exclude_dirs] if exclude_dirs else []

    # 初始化输出文件计数器
    file_counter = 1
    output_file = os.path.join(source_dir, f"list_{file_counter}.txt")
    
    # 如果输出文件存在，先删除它
    if os.path.exists(output_file):
        os.remove(output_file)

    current_size = 0  # 当前输出文件的字节大小

    # 遍历目录下的所有文件并合并内容
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(source_dir):
            # 检查当前目录是否在排除列表中
            current_dir = os.path.basename(root).lower()
            if any(excluded_dir in current_dir for excluded_dir in exclude_dirs):
                print(f"跳过排除目录：{root}")
                continue

            for file in files:
                file_path = os.path.join(root, file)
                
                # 跳过隐藏文件、输出文件本身和非文本文件
                if file.startswith('.') or file_path.startswith(output_file) or not is_text_file(file):
                    continue
                
                print(f"处理文件：{file_path}")
                
                try:
                    # 读取文件内容并移除注释
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                        content = infile.read()
                        clean_content = remove_comments(content)
                    
                    # 写入文件路径标记和清理后的内容
                    new_content = f"以下是 {file_path} 文件的内容：\n{clean_content}\n"
                    
                    # 如果启用了分片功能，检查是否需要换新文件
                    if max_size and (current_size + len(new_content.encode('utf-8')) > max_size):
                        # 关闭当前文件，开始写入新文件
                        outfile.close()
                        file_counter += 1
                        output_file = os.path.join(source_dir, f"list_{file_counter}.txt")
                        outfile = open(output_file, 'w', encoding='utf-8')
                        current_size = 0
                    
                    # 写入内容并更新当前文件大小
                    outfile.write(new_content)
                    current_size += len(new_content.encode('utf-8'))

                except Exception as e:
                    print(f"无法处理文件 {file_path}: {e}")

    print(f"所有文件已合并到 {source_dir}/list_x.txt 文件中。")

# 主程序入口
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供要合并文件的目录路径。")
    else:
        source_dir = sys.argv[1]
        max_size = None
        exclude_dirs = []
        
        # 解析命令行参数
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] in ['--part', '-P']:
                if i + 1 < len(sys.argv):
                    try:
                        max_size = int(sys.argv[i + 1])
                        i += 2
                    except ValueError:
                        print("请提供有效的整型数字作为字节大小。")
                        sys.exit(1)
                else:
                    print("--part 参数需要指定大小值。")
                    sys.exit(1)
            elif sys.argv[i] in ['--exclude', '-E']:
                if i + 1 < len(sys.argv):
                    # 支持多个排除目录，用逗号分隔
                    exclude_dirs.extend(sys.argv[i + 1].split(','))
                    i += 2
                else:
                    print("--exclude 参数需要指定排除目录。")
                    sys.exit(1)
            else:
                i += 1
        
        merge_files(source_dir, max_size, exclude_dirs)
