import requests
# 一般用于 图片、文件、视频 等下载时，获取原始数据。 原始字节
res = requests.get(
    url="https://gd-hbimg.huaban.com/b93fcc5bb4751934bbd56918bdab8184966dca2974df1-bo7qSF",
)
# print(res.content)

with open("v1.png", mode='wb') as f:
    f.write(res.content)
