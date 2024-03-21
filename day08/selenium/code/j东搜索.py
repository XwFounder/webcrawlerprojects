from selenium import webdriver
from selenium.webdriver.common.by import By

# 代码模拟人的行为思路包含
# 1、打卡j东网址
# 2、获取j东搜索框的xpath，输入内容，点击click()
# 3、查询列表
# 4、获取商标或者商品的标题内容

options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://113.102.239.10")
# http://httpbin.org/ip
options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片
options.add_argument('--disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.maximize_window()


with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

# 1、打卡京东
driver.get('https://www.jd.com/')
driver.implicitly_wait(10)
# 2 获取j东搜索框的xpath，输入内容，点击click()
tag = driver.find_element(
    By.XPATH,
    '//*[@id="key"]'
)
tag.send_keys("iphone手机")
# 3.点击搜索
tag = driver.find_element(
    By.XPATH,
    '//*[@id="search"]/div/div[2]/button'
)
tag.click()
# 4.查询列表
tag_list = driver.find_elements(
    By.XPATH,
    '//*[@id="J_goodsList"]/ul/li'
)
for tag in tag_list:
    # title = tag.find_element(By.XPATH, 'div/div[@class="p-name p-name-type-2"]//em').text
    title = tag.find_element(By.XPATH, 'div/div[@class="p-name p-name-type-2"]/a/em').text
    print(title)

driver.close()


