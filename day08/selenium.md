# 1.selenium自动化
selenium用来操作浏览器，在浏览器页面上实现：点击、输入、滑动等操作
不用于selenium,逆向的本质是：
- 分析请求，例如：请求方法、请求参数、加密方式等。
- 用代码模拟请求去实现同等功能。

逆向 vs 自动化Selenium
Selenium： 


- 【优】简单不需要逆向，只需要控制浏览器去执行预设的操作即可


- 【缺点】性能差，不利于批量实现

逆向：

- 【优】算法逆向出来后，性能好且利于批量实现

-  【缺点】语法难搞的js加密算法，不容易逆向


# 2.必备操作
- 安装模块

```
pip3.11 install selenium
```
- 下载驱动
```text
Selenium想要控制谷歌、火狐、IE、Edage等浏览器，必须要使用对应的驱动才行。【Selenium】->【驱动】->【浏览器】
	【Selenium】->【火狐驱动】->【火狐浏览器】
	【Selenium】->【谷歌驱动】->【谷歌浏览器】

谷歌驱动的下载：
	   114及之前版本： http://chromedriver.storage.googleapis.com/index.html
	117/118/119版本： https://googlechromelabs.github.io/chrome-for-testing/
	
浏览器版本的获取：
	在谷歌浏览器上访问 chrome://version/   例如：119.0.6045.200 (正式版本) （64 位） (cohort: Stable) 
```
- 快速使用
```pycon
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

time.sleep(5)
driver.close()
```
## 2.2 寻找标签
```pycon
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('打开网址')

# find_element  find_elements
#  BY.ID 根据id锦进行操作，CLASS_NAME：cclassname,XPATH
tag = driver.find_element(By.ID, "user") 
tag = driver.find_element(By.CLASS_NAME, "c1")
tag = driver.find_element(By.TAG_NAME, "div") # 根据标签名，查找
tag = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div[1]/span[2]")
tag = driver.find_element(By.XPATH, '//*[@id="geetest-wrap"]//input[@name="tel"]')

tag_list = driver.find_elements(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a")
for tag in tag_list:
    print(tag)

time.sleep(5)
driver.close()
```

# 2.3 执行操作
常见的执行操作：点击、输入
```pycon
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

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
```

# 2.4 执行JavaScript
如果【选择标签】【执行操作】这种操作起来比较繁琐，也可以直接在页面上去执行js代码实现功能。
```pycon
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

# #############  1.点击短信登录 #############
time.sleep(3)
sms_btn = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()


# #############  2.输入账号 #############
phone_txt = driver.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
phone_txt.send_keys("18630087660")

# ############# 3.选择国家 #############
time.sleep(2)
driver.execute_script('document.querySelector(".area-code-select").children[18].click()')

# ############# 4.读取cookie #############
data_string = driver.execute_script('return document.cookie;')   # return document.title;
print(data_string)

# ############# 5.读取cookie #############
cookie_list = driver.get_cookies()
print(cookie_list)

time.sleep(2550)
driver.close()
```
# 2.5 等待执行
如果页面加载比较慢、需要等待某个元素加载成功后，在执行某些操作

三种方式：1、基于lambda表达式 2、自定义函数 3、全局配置

1、基于lambda表达式
```pycon
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')
# #############  方式1：点击短信登录 #############
time.sleep(3)
sms_btn = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')

sms_btn.click()
# #############  方式2：点击短信登录（推荐） #############
sms_btn = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
))
sms_btn.click()

```
总结：理解下使用方式和含义，但本质上还需要我们对标签进行各种分析

# 2.6 获取值
当找到某个标签之后，想要获取标签内部值。

**示例1：文本和属性**
例如：`<a id='x1' class="info mine" href="5xclass.cn">武沛齐</a>`
```pycon
driver.get('https://www.5xclass.cn')

tag = driver.find_element(
    By.XPATH,
    '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a[1]'
)
print(tag.text)
print(tag.get_attribute("target"))
print(tag.get_attribute("data-toggle"))

driver.close()
```
```pycon
# **示例3：选择相关**
#
# ```html
# <input type="radio" name="findcar" value="1" checked="">新车
# <input type="radio" name="findcar" value="2">二手机
# ```
driver.get('https://www.autohome.com.cn/beijing/')

# ############### 1.单独找到每一个 ###############
tag = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]/label[1]/span/input'
)
print(tag.get_property("checked")) # True


tag = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]/label[2]/span/input'
)
print(tag.get_property("checked")) # False

# ############### 2.循环找到每一个 ###############
parent = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]'
)

tag_list = parent.find_elements(
    By.XPATH,
    'label/span/input'
)
for tag in tag_list:
    print( tag.get_property("checked"), tag.get_attribute("value") )

driver.close()
```

# 2.7 源码+bs4
打卡页面后，如果基于selenium不大容易得定位和寻找，也可以结果BS64来进行寻找
```pycon
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://car.yiche.com/')

html_string = driver.page_source

soup = BeautifulSoup(html_string, features="html.parser")
tag_list = soup.find_all(name="div", attrs={"class": "item-brand"})
for tag in tag_list:
    child = tag.find(name='div', attrs={"class": "brand-name"})
    print(child.text)

driver.close()
```
# 2.8 携带Cookie
```pycon
# 关键词
driver.add_cookie({'name': 'foo', 'value': 'bar'})
```
```pycon
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 注意：一定要先访问，不然Cookie无法生效
driver.get('https://dig.chouti.com/about')

# 加cookie
driver.add_cookie({
    'name': 'token',
    'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqaWQiOiJjZHVfNDU3OTI2NDUxNTUiLCJleHBpcmUiOiIxNzA0MzI5NDY5OTMyIn0.8n_tWcEHXsBSXWIY9rBoGWwaLPF8iWIruryhKTe5_ks'
})

# 再访问
driver.get('https://dig.chouti.com/')


time.sleep(2000)
driver.close()
```
# 2.9 IP检测和代理
如果网站进行了IP访问限制。例如：每个IP每天只能操作5次，此时可以选择购买IP，然偶在请求时添加代理IP即可


具体实现步骤：
1、购买IP
2、登录购买IP聚到的平台，配置自己的白名单
3、代码携带代理
````pycon
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}") # "182.106.136.218:40192"

service = Service("driver/chromedriver.exe")

opt = webdriver.ChromeOptions()
# opt.add_argument(f'--proxy-server=222.89.70.40:40001')  # 代理
opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
driver = webdriver.Chrome(service=service, options=opt)


driver.get('https://myip.ipip.net/')

time.sleep(2000)
driver.close()
````
# 其他配置
```pycon
# 如果想要正常使用selenium访问，那就需要隐藏浏览器相关的特征。
opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)
# 如果不想显示展示在浏览器上的操作，只想偷偷的在后台运行。
opt.add_argument('--headless') 
opt.add_argument('--disable-infobars')                    # 禁止策略化
opt.add_argument('--no-sandbox')                          # 解决DevToolsActivePort文件不存在的报错
opt.add_argument('window-size=1920x3000')                 # 指定浏览器分辨率
opt.add_argument('--disable-gpu')                         # 谷歌文档提到需要加上这个属性来规避bug
opt.add_argument('--incognito')                           # 隐身模式（无痕模式）
opt.add_argument('--disable-javascript')                  # 禁用javascript
opt.add_argument('--start-maximized')                     # 最大化运行（全屏窗口）,不设置，取元素会报错
opt.add_argument('--hide-scrollbars')                     # 隐藏滚动条, 应对一些特殊页面
opt.add_argument('lang=en_US')                            # 设置语言
opt.add_argument('blink-settings=imagesEnabled=false')    # 不加载图片, 提升速度
opt.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Androi....')      # 设置User-Agent
opt.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
```

# 3、案例：j东搜索
代码模拟人的行为思路包含
1、打卡j东网址
2、获取j东搜索框的xpath，输入内容，点击click()
3、查询列表
4、获取商标或者商品的标题内容

```pycon
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 换成自己生成的代理
res = requests.get(url="https://dps.kdlapi.com/api/getdps/?secret_id=o60wwtxvs5ukaqqz18ai&num=1&signature=i6s9shfjfiogat5ijecbyfwwc5grwrzj&pt=1&format=json&sep=1")
proxy_string = res.json()['data']['proxy_list'][0]
print(f"获取代理：{proxy_string}")


service = Service("driver/chromedriver.exe")
opt = webdriver.ChromeOptions()

opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('blink-settings=imagesEnabled=false') # 不加载图片

opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=opt)

driver.implicitly_wait(10)

with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

# 1.打开京东
driver.get('https://www.jd.com/')

# 2.搜索框+输入
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
```

# 4.案例：x麦网
思路
1、打卡大麦网
2、搜索框+输入
3、点击搜索
4、查询列表
```pycon
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

service = Service("driver/chromedriver.exe")
opt = webdriver.ChromeOptions()
opt.add_argument(f'--proxy-server={proxy_string}')  # 代理
opt.add_argument('blink-settings=imagesEnabled=false')
opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=service, options=opt)
driver.implicitly_wait(10)
with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

# 1.打开大麦网
driver.get('https://www.damai.cn/')

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

```








