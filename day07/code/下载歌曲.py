import json
import time

import requests

# 分析：
# 1、发送地址：https://api.liumingye.cn/m/api/search
# 2、请求参数格式：json格式 Content-Type:application/json;charset=UTF-8
#     {
#     "page": 1,
#     "text": "五月天",
#     "token": "20230327.09a532d481d9346f6fced0c3d1187f74",
#     "type": "YQM",
#     "v": "beta",
#     "_t": 1710444415459
# }
#
#
# 搜索列表
songName = "五月天"
params = {
    "page": "1",
    "text": "五月天",
    "token": "20230327.664cfb016df5fb6a253685d7ea5d4f1a",
    "type": "YQM",
    "v": "beta",
    "_t": "1710446610038"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://tools.liumingye.cn",
    "Referer": "https://tools.liumingye.cn/music/"
}

t = time.time()
t_int = int(t)
res = requests.post(
    url="https://api.liumingye.cn/m/api/search",
    headers=headers,
    params=params
)

# data_dict =json.loads(res.text)
print(res.text)
# print(data_dict)
# data_list = res_dict['data']['list']
# for item in data_list:
#     print(item)
