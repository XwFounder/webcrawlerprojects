import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(
    url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}")
opt = webdriver.ChromeOptions()
opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('blink-settings=imagesEnabled=false')
opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=opt)

with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

# 1.打开大麦网
driver.get('https://www.damai.cn/')
driver.implicitly_wait(10)
# 2.搜索框+输入
tag = driver.find_element(
    By.XPATH,
    '//input[@class="input-search"]'
)
tag.send_keys("周杰伦")

# 3.点击搜索
tag = driver.find_element(
    By.XPATH,
    '//div[@class="btn-search"]'
)
tag.click()

# 4.查询列表
tag_list = driver.find_elements(
    By.XPATH,
    '//div[@class="search__itemlist"]//div[@class="items"]'
)
for tag in tag_list:
    title = tag.find_element(By.XPATH, 'div[@class="items__txt"]/div[1]/a').text
    print(title)


time.sleep(2000)
driver.close()