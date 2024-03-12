from bs4 import BeautifulSoup
html_string = """<div>
    <h1 class="item x1" id="x2">武沛齐</h1>
    <ul class="item">
        <li>篮球</li>
        <li>足球</li>
    </ul>
    <div id='x3'>
        <span>5xclass.cn</span>
        <a href="www.xxx.com" class='info'>pythonav.com</a>
        <div>
            <span>xx</span>
            <span>xx</span>
        </div>
    </div>
</div>"""

# 根据标签名称，获取标签（只获取找到的第1个）
soup = BeautifulSoup(html_string, features="html.parser")

# parent_tag = soup.find(attrs={"id": "x3"})
# for tag in parent_tag.find_all(recursive=False):
#     print(tag.name)

# tag_list = soup.find_all(name="li")
# for tag in tag_list:
#     print(tag.name, tag.text)

# parent_tag = soup.find(attrs={"id": "x3"})
# tag = parent_tag.find(name='a')
# print(tag.name)
# print(tag.text)
# print(tag.attrs)

# tag = soup.find(name='h1')
# print(tag)  # 对象（包裹）
# print(tag.name)
# print(tag.text)
# print(tag.attrs)

# tag = soup.find(name='a')
# print(tag)  # 对象（包裹）
# print(tag.name)
# print(tag.text)
# print(tag.attrs)

# tag = soup.find(name="div", attrs={"id": "x3"})
# print(tag)  # 对象（包裹）
# print(tag.name)
# print(tag.text)
# print(tag.attrs)


# tag = soup.find(name="ul", attrs={"class": "item"})
# print(tag)  # 对象（包裹）
# print(tag.name)
# print(tag.text)
# print(tag.attrs)
