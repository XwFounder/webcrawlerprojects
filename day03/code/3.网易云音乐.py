import requests
from bs4 import BeautifulSoup

res = requests.get(
    url="https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": "https://music.163.com/"
    }
)
# html根元素
soup = BeautifulSoup(res.text, features="html.parser")

parent_tag = soup.find(name='ul', attrs={"id": "m-pl-container"})

for child in parent_tag.find_all(recursive=False):
    # 通过find方法找到class为"tit f-thide s-fc0"的a标签，提取文本作为歌单的标题。
    # 通过find方法找到img标签，提取src属性作为歌单封面图片的URL。
    title = child.find(name="a", attrs={"class": "tit f-thide s-fc0"}).text
    image_url = child.find(name='imgs').attrs['src']
    print(title, image_url)

    # 每个封面下载下来
    img_res = requests.get(url=image_url)
    file_name = title.split()[0]
    with open(f"{file_name}.jpg", mode='wb') as f:
        f.write(img_res.content)
