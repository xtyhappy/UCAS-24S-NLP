import re
from bs4 import BeautifulSoup
import requests
import os

# 定义函数：动态获取指定页面符合条件的链接
def solve(page):  
    """
    根据给定的页码page构造请求链接并发送GET请求，
    从响应中提取符合要求的新闻链接。
    
    参数：
    page (int): 需要抓取的页面编号
    
    返回值：
    urls (list): 包含新闻链接的列表
    """
    base_url = "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2669&k=&num=50&page="
    suffix = "&r=0.7488014654950375&callback=jQuery1112025760955190502766_1604665024595&_=1604665024597"
    url = base_url + str(page) + suffix
    headers = {
      'authority': 'feed.mix.sina.com.cn',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
      'accept': '*/*',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'no-cors',
      'sec-fetch-dest': 'script',
      'referer': 'https://news.sina.com.cn/roll/',
      'accept-language': 'zh-CN,zh;q=0.9',
    }  # 设置请求头信息

    # 发送GET请求并获取响应
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    # 使用正则表达式提取新闻链接，同时将转义的斜线还原
    urls = [url.replace('\\/', '/') for url in re.findall(r'"url":"([^"]+)"', response.text)]
    
    return urls

# 定义函数：下载并写入新闻标题与内容到文本文件
def download_and_write(title, content, output_dir, file_count, total_news):
    """
    将新闻标题和内容写入到指定目录下的文本文件中，
    并按照每100条新闻分隔成不同的文件。
    
    参数：
    title (str): 新闻标题
    content (str): 新闻内容
    output_dir (str): 输出文件夹路径
    file_count (int): 当前写入文件的计数器
    total_news (int): 总新闻数量统计
    
    返回值：
    file_count (int): 更新后的文件计数器
    """
    # 创建用于保存新闻的文件名，并写入内容
    filename = f"{output_dir}/{file_count // 100:05d}.txt"
    with open(filename, 'a+', encoding='utf8') as file_object:
        # 格式化写入标题和内容
        file_object.write(f"{title}\n{content}\n\n")

    # 更新新闻总数和文件计数器
    total_news += 1
    file_count += 1

    # 每写入100条新闻时输出当前进度
    if file_count % 100 == 0:
        print(f'已完成{file_count}条新闻，已存储至文件：{filename}')
    
    return file_count

# 主函数入口
def main():
    """
    爬取新闻的主要流程，包括创建目标文件夹、循环抓取各页新闻及内容，
    并调用download_and_write函数将数据写入文件。
    """
    output_dir = '/Users/amber/Desktop/2024spring/nlp/hw1/data/new_zh_data'
    # 若目标文件夹不存在，则创建之
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    total_news = 0
    file_count = 0
    # 循环遍历预设范围内的页面
    for page in range(1, 201):  # 假设总共有200页，每页50条新闻
        # 获取当前页面的所有新闻链接
        urls = solve(page)
        for each in urls:
            # 对每个新闻链接发送GET请求
            response = requests.get(each)
            soup = BeautifulSoup(response.content, 'lxml')

            # 提取新闻标题和正文内容
            title = soup.find("h1", class_="main-title").string.strip()
            content_tag = soup.find('div', class_="article")
            if content_tag is not None:
                content = ''.join([p.string for p in content_tag.findAll('p') if p.string])

                # 清理并标准化标题字符串
                clean_title = title.replace(':', '').replace('"', '').replace('|', '').replace('/', '').replace('\\', '').replace('*', '').replace('<', '').replace('>', '').replace('?', '')

                # 调用download_and_write函数写入新闻数据
                file_count = download_and_write(clean_title, content, output_dir, file_count, total_news)

# 执行主函数
if __name__ == '__main__':
    main()