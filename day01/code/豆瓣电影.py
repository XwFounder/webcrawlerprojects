import json

import requests
# 分析一个网址，用requests请求就可以实现。
#
# 抓包分析：
# 豆瓣电影
#
# 请求方式：GET
#
# 请求地址：https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
#
# ```py
# type: tv
# tag: 热门
# page_limit: 50
# page_start: 0
# ```
#
#
#
# 请求头：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
#
# 请求地址查看关键数据、请求方式：，请求URL，请求参数，请求头，响应体内容，
#
# post请求需要设置请求体：remember=true&name=1897570&password=admin123&ticket=tr03d3SS2iIZqc0qUHofZAHhCfKI-ao-DY6nu-il0O1_XdWyMx2RI2lfPLROQPkbXbInYe45JPqb4reNbZKT1CY1tcHlKEtLlEfwauYpXCCqOrJn7fKHHqUZxH5utuPAdFXE&randstr=%40mVB&tc_app_id=2044348370
res = requests.get(
    url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
)
data_dict = json.loads(res.text)
data_list=data_dict['subjects']
for data in data_list:
    print(data['url'],data['title'])