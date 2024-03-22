import re
import time
import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)

# 1.打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2.点击【文字点选验证】
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[4]'
))
tag.click()

# 3.点击开始验证 //*[@id="captcha"]/div[2]/div[1]/div[1]
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.CLASS_NAME,
    'geetest_btn_click'
))
tag.click()

time.sleep(5)

# 要识别的目标图片
target_tag = driver.find_element(
    By.CLASS_NAME,
    'geetest_ques_back'
)
target_tag.screenshot("target.png") # 找到目标图片然后截屏

# 识别图片
bg_tag = driver.find_element(
    By.CLASS_NAME,
    'geetest_bg'
)
bg_tag.screenshot("bg.png") # 背景图片

time.sleep(2000)
driver.close()