import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}") # "182.106.136.218:40192"


opt = webdriver.ChromeOptions()
# opt.add_argument(f'--proxy-server=222.89.70.40:40001')  # 代理
opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=opt)


driver.get('https://myip.ipip.net/')

time.sleep(2000)
driver.close()