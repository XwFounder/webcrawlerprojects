import requests
from bs4 import BeautifulSoup

# 请求获取HTML文本
res = requests.get(
    url="https://car.yiche.com/"
)

# print(res.text)
soup = BeautifulSoup(res.text, features="html.parser")

# tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
# for tag in tag_list:
#     print(tag.attrs["data-name"])
#
# 集合遍历操作：获取同级标签、属性,然后在通过父标签下的子标签查询想要额数据内容
tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
for tag in tag_list:
    child = tag.find(name='div', attrs={"class": "brand-name"})
    print(child.text)
