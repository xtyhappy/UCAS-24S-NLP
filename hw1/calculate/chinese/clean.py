import re
import os

def merge_files(src_folder, start_file, end_file, dest_file):
    with open(dest_file, 'w', encoding='utf8') as output_file:
        for i in range(start_file, end_file + 1):
            filename = f"{src_folder}/{i:05d}.txt"
            with open(filename, 'r', encoding='utf8') as input_file:
                output_file.write(input_file.read())

def clean_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf8') as file:
        content = file.read()

        # 删除“责任编辑：（姓名）”
        content = re.sub(r"责任编辑：\（.*?）", "", content)

        # 去除“来源：（新闻来源）”
        content = re.sub(r"来源：\（.*?）", "", content)

        # 只保留汉字字符
        content = re.sub(r"[^\u4e00-\u9fa5]", "", content)

        with open(output_file, 'w', encoding='utf8') as output_file:
            output_file.write(content)

def main():
    src_folder = '/Users/amber/Desktop/2024spring/nlp/hw1/data/new_zh_data'
    dest_file = f'{src_folder}/total.txt'
    output_file = f'{src_folder}/cleannewzh.txt'

    # 合并文件
    merge_files(src_folder, 0, 24, dest_file)

    # 清洗数据
    clean_data(dest_file, output_file)

if __name__ == '__main__':
    main()
