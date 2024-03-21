import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# driver.get('https://www.5xclass.cn')
#
# tag = driver.find_element(
#     By.XPATH,
#     '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a[1]'
# )
# print(tag.text)
# print(tag.get_attribute("target"))
# print(tag.get_attribute("data-toggle"))
#
# driver.close()

# **示例2：获取值**
# 例如：`<input type='text' value="?" placeholder="?" />`
# 例如：`<select ><option value='1'>北京</option> </option value='2'>上海</option> </select>` ，获取select标签的value属性
driver.get('https://www.bilibili.com/')

time.sleep(10)
# //*[@id="nav-searchform"]/div[1]/input
tag = driver.find_element(
    By.XPATH,
    '//*[@id="nav-searchform"]/div[1]/input'
)
print(tag)
print(tag.text)
print(tag.get_attribute("placeholder"))
print(tag.get_attribute("value"))

time.sleep(1000)
driver.close()

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