import re

# 定义源文件和目标文件路径
source_file = '/Users/amber/Desktop/2024spring/nlp/hw1/data/en_data/total_en.txt'
target_file = '/Users/amber/Desktop/2024spring/nlp/hw1/data/en_data/cleannovelen.txt'

# 使用 with open... as 语句打开源文件和目标文件
with open(source_file, 'r') as infile, open(target_file, 'w') as outfile:
    # 读取源文件的内容
    content = infile.read()
    # 使用正则表达式去除除了字母和空格以外的所有字符
    clean_content = re.sub('[^a-zA-Z ]+', '', content)
    # 将所有小写字母转化为大写字母
    upper_content = clean_content.upper()
    # 写回目标文件
    outfile.write(upper_content)

print("处理完成，文件已保存为 cleannovelen.txt")
