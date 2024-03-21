import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)

driver.get('https://www.5xclass.cn')
tag = driver.find_element(
    By.XPATH,
    '/html/body/div/div[2]/div/div[2]/div/div[2]'
)

# 截图&保存
tag.screenshot("demo.png")

# 截图&图片内容
body = tag.screenshot_as_png
print(body)

# 截图&Base64编码格式图片内容
b64_body = tag.screenshot_as_base64
print(b64_body)

driver.close()