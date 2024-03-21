import time

from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# 注意：一定要先访问，不然Cookie无法生效
driver.get('https://dig.chouti.com/about')

# 加cookie
driver.add_cookie({
    'name': 'token',
    'value': 'Hm_lvt_03b2668f8e8699e91d479d62bc7630f1=1711044305; Hm_lpvt_03b2668f8e8699e91d479d62bc7630f1=1711044305; route=1711044306.294.41.811022; io=Tk9dYsphQ8-3HcXGEDNf'
})

# 再访问
driver.get('https://dig.chouti.com/')


time.sleep(2000)
driver.close()