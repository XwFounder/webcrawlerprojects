from bs4 import BeautifulSoup

html_string = """<div>
    <h1 class="item">武沛齐</h1>
    <ul class="item">
        <li>篮球</li>
        <li>足球</li>
    </ul>
    <div id='x3'>
      <span>5xclass.cn</span>
        <a href="www.xxx.com" class='info'>pythonav.com</a>
        <span class='xx1'>武沛齐</span>
    </div>
</div>"""

soup =BeautifulSoup(html_string, features="html.parser")

tag = soup.find(name='a')
# 循环读取，先找到某个夫标签、然后再通过子标签寻找
parent_tag = soup.find(name='div', attrs={"id": "x3"})
child_tag = parent_tag.find(name='li')
# 读取多个标签
tag_list = soup.find_all(name="li")
# print(tag)       # 标签对象
# print(tag.name)  # 标签名字 a
# print(tag.text)  # 标签文本 pythonav.com
# print(tag.attrs) # 标签属性 {'href': 'www.xxx.com', 'class': ['info']}
# print(child_tag)
print(tag_list)