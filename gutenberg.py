# 匯入套件
# 操作 browser 的 API
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# 匯入套件
from bs4 import BeautifulSoup as bs

# 匯入 Time 工具
import time

# 匯入 json 工具
import json

# 匯入 執行 command 工具
import os

# 匯入 正規表達式
import re

from time import sleep
from pprint import pprint
from urllib import parse


# 使用 web Driver
# myService = Service(executable_path='./chromedriver.exe')  # windows版
myService = Service(executable_path='/usr/local/bin/chromedriver')  # mac版
dri = webdriver.Chrome(service=myService)

# 開啟 指定網頁 首頁
dri.get("https://www.gutenberg.org/browse/languages/zh")

# 取得檢視原始碼的內容 (page_source 取得的 html，是動態的、使用者操作過後的結果)
html = dri.page_source

# 建立 soup 物件
soup = bs(html, 'lxml')

# 取得書名 List
title = soup.select('div.pgdbbylanguage ul li a')

# Regular expresion 中文
reg = r'[\u4e00-\u9fa5]*'

# 列出幾本中文書
count = 0
for t in title:
    it = re.search(reg, t.get_text())

    print(t.get_text())
    print(type(t.get_text()))
    print(it[0])
    if it[0] != '' and count < 200:
        count += 1
print(f'總共有 {len(title)} 本書 , 中文書共有{count} 本書')

# # 設定首頁網址
# url = 'https://www.gutenberg.org'

# # 建立整理放置古騰堡計畫的 List
# listGutenberg = []

# # 建立儲存資料夾
# folder = '/Users/allentsai/python_web_scraping-master/Gutenberg_ebooks'
# if os.path.exists(folder) == False:
#     os.makedirs(folder)

# # 將書名與主連結放進 List
# count = 0
# for t in title:
#     it = re.search(reg, t.get_text())
#     if it[0] != '' and count < 600:
#         count += 1
#         listGutenberg.append({
#             'index': count,
#             'title': t.get_text(),
#             'main_link': f"{url}{t['href']}",
#             'sub_link': ''
#         })

# # 取得下載連結
# for l in range(len(listGutenberg)):
#     dri.get(listGutenberg[l]['main_link'])
#     html = dri.page_source
#     soup = bs(html, 'lxml')
#     linkList = soup.select('tr[about]')
#     reg = r'.*txt.*'
#     for i in linkList:
#         r = re.search(reg, i['about'])
#         if r != None:
#             listGutenberg[l]['sub_link'] = i['about']

#             # 儲存小說內文
#             dri.get(listGutenberg[l]['sub_link'])
#             html = dri.page_source
#             soup = bs(html, 'lxml')

#             # 顯示目前正在處理第幾本書
#             print(
#                 f"目前正在儲存第『 {listGutenberg[l]['index']} 』本 : {listGutenberg[l]['title']}")

#             # 睡個一下等 loading 畫面
#             sleep(3)

#             # 取得小說內文
#             cont = soup.select_one('pre')

#             # 建立小說txt檔
#             with open(f"{folder}/{listGutenberg[l]['index']}_{listGutenberg[l]['title']}.txt", "w", encoding="utf-8") as file:
#                 file.write(listGutenberg[l]['title']+'\n')

#             # 剔除英文，留下中文內文
#             reg = r'[\u4e00-\u9fa5]+[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]*[\n]?|[\u4e00-\u9fa5]*[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+[\n]?'
#             # 使用正規表達式的finditer迭代方式儲存符合中文的內文
#             it = re.finditer(reg, cont.get_text())
#             if it != None:
#                 for i in it:
#                     if i[0] != '':
#                         with open(f"{folder}/{listGutenberg[l]['index']}_{listGutenberg[l]['title']}.txt", "a", encoding="utf-8") as file:
#                             file.write(i[0])

# # 儲存書本資訊的 json 檔
# with open(f"{folder}/Gutenberg_Info.json", "w", encoding="utf-8") as js:
#     js.write(json.dumps(listGutenberg, ensure_ascii=False))

# # 關閉瀏覽器
# dri.quit()

# print('已儲存完成')
