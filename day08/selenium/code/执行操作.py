import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://passport.bilibili.com/login")

# 1.点击短信登录
time.sleep(3)
sms_btn = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()  # 点击


# 2.输入账号
phone_txt = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
phone_txt.send_keys("18630087660")  # 输入

time.sleep(55)
driver.close()