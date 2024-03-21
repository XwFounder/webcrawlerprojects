import time

from selenium import webdriver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建一个webDriver的实例，接下来的所有操作都是在该实例上进行，以Chrome实例为例
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://passport.bilibili.com/login")
time.sleep(8)
driver.close()