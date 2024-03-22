import re
import time
import ddddocr
import requests
import base64
import requests
from hashlib import md5
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from PIL import Image, ImageDraw
from io import BytesIO

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 1.打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2.点击【滑动拼图验证】
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[4]'
))
tag.click()

# 3.点击开始验证
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.CLASS_NAME,
    'geetest_btn_click'
))
tag.click()

# 4.等待验证码出来
time.sleep(5)

# 5.识别任务图片
target_word_list = []
parent = driver.find_element(By.CLASS_NAME, 'geetest_ques_back')
tag_list = parent.find_elements(By.TAG_NAME, "img")
for tag in tag_list:
    ocr = ddddocr.DdddOcr(show_ad=False)
    word = ocr.classification(tag.screenshot_as_png)
    target_word_list.append(word)

print("要识别的文字：", target_word_list)

# 6.背景图片
bg_tag = driver.find_element(
    By.CLASS_NAME,
    'geetest_bg'
)
content = bg_tag.screenshot_as_png
bg_tag.screenshot("bg.png")

# 7.识别背景中的所有文字并获取坐标
res = requests.post(
    url='http://upload.chaojiying.net/Upload/Processing.php',
    data={
        'user': "wupeiqi",
        'pass2': md5("qwe123..".encode('utf-8')).hexdigest(),
        'codetype': "9501",
        'file_base64': base64.b64encode(content)
    },
    headers={
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
)

res_dict = res.json()
print(res_dict)

# 8.每个字的坐标  {"鸭":(196,85), ...}    target_word_list = ["花","鸭","字"]
bg_word_dict = {}
for item in res_dict["pic_str"].split("|"):
    word, x, y = item.split(",")
    bg_word_dict[word] = (x, y)

print(bg_word_dict)

time.sleep(1000)
driver.close()