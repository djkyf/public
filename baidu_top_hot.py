"""
爬取百度热搜   by djkyf
"""
import requests  # 发送请求
import pandas as pd  # 存入excel数据
from openpyxl.workbook import Workbook
import time

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 百度热搜榜地址
url = 'https://top.baidu.com/api/board?platform=wise&tab=realtime'
# 构造请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Host': 'top.baidu.com',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://top.baidu.com/board?tab=novel',
}
# 发送请求
r = requests.get(url, header)
# 用json格式接收请求数据
json_data = r.json()
title_list = []     # 标题
order_list = []     # 排名
score_list = []     # 热搜指数
desc_list = []      # 描述
url_list = []       # 链接地址
# 爬取置顶热搜
top_content_list = json_data['data']['cards'][0]['topContent']
for item in top_content_list:
    title_list.append(item['query'])
    order_list.append(item['index'])
    score_list.append(item['hotScore'])
    desc_list.append(item['desc'])
    url_list.append(item['url'])
# 爬取普通热搜
content_list = json_data['data']['cards'][0]['content']
for item in content_list:
    title_list.append(item['query'])
    order_list.append(item['index'])
    score_list.append(item['hotScore'])
    desc_list.append(item['desc'])
    url_list.append(item['url'])
df = pd.DataFrame(  # 拼装爬取到的数据为DataFrame
    {
        '热搜标题': title_list,
        '热搜排名': order_list,
        '热搜指数': score_list,
        '描述': desc_list,
        '链接地址': url_list
    }
)
df.to_excel(f'{now}百度热搜榜.xlsx', index=False)  # 保存结果数据
print(f'{now}百度热搜榜爬取结束')
