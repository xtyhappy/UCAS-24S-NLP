import os

# 定义源目录和目标文件
source_dir = '/Users/amber/Desktop/2024spring/nlp/hw1/data/en_data/corpus'
target_file = '/Users/amber/Desktop/2024spring/nlp/hw1/data/en_data/total_en.txt'

# 使用 with open... as 语句创建或覆盖目标文件
with open(target_file, 'w') as outfile:
    # os.walk() 遍历源目录
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 检查文件扩展名是否为 .txt
            if file.endswith('.txt'):
                # 构造文件的完整路径
                file_path = os.path.join(root, file)
                # 使用 with open... as 语句以只读模式打开每个文本文件
                with open(file_path, 'r') as infile:
                    # 将文件内容写入目标文件
                    outfile.write(infile.read() + '\n') # 添加换行符以分隔不同文件的内容

print("所有 .txt 文件已合并到 total_en.txt")
