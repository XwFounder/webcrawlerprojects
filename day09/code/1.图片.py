import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)


# 1.打开首页
driver.get('https://www.geetest.com/adaptive-captcha-demo')

# 2.点击【滑动拼图验证】
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[3]'
))
tag.click()

# 3.点击开始验证
tag = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.CLASS_NAME,
    'geetest_btn_click'
))
tag.click()


# 4.读取背景图片
def fetch_bg_func(dv):
    tag_object = dv.find_element(
        By.CLASS_NAME,
        'geetest_bg'
    )
    style_string = tag_object.get_attribute("style")
    match_list = re.findall('url\(\"(.*)\"\);', style_string)  # ["http..." ]     []
    if match_list:
        return match_list[0]


bg_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_bg_func)
print("背景图：", bg_image_url)


# 4.读取缺口图片
def fetch_slice_func(dv):
    tag_object = dv.find_element(
        By.CLASS_NAME,
        'geetest_slice_bg'
    )
    style_string = tag_object.get_attribute("style")
    match_list = re.findall('url\(\"(.*)\"\);', style_string)
    if match_list:
        return match_list[0]


slice_image_url = WebDriverWait(driver, 30, 0.5).until(fetch_slice_func)
print("缺口图：", slice_image_url)

time.sleep(2000)
driver.close()