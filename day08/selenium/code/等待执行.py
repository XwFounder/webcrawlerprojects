import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#  1两种方式， 第一种显示等待页面加载完毕，第二种隐式加载页面，总共30秒，每次0.5秒进行查询要出来的页面
driver.get('https://passport.bilibili.com/login')
# # #############  方式1：点击短信登录 #############
# time.sleep(3)
# sms_btn = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')

# sms_btn.click()
# #############  方式2：点击短信登录（推荐） #############
sms_btn = WebDriverWait(driver, 30, 0.5).until(lambda dv: dv.find_element(
    By.XPATH,
    '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
))
sms_btn.click()

#  2、自定义函数

def func(dv):
    print("无返回值，则间隔0.5s执行一次此函数；如有返回值，则复制给sms_btn变量")
    # <div xxx="123" id="uuu"></div>
    # <img src="..."/>
    tag = dv.find_element(
        By.XPATH,
        '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
    )
    img_src = tag.get_attribute("xxx")
    if img_src:
        return tag
    return

sms_btn = WebDriverWait(driver, 30, 0.5).until(func)
sms_btn.click()

time.sleep(250)
driver.close()
# 示例3：全局配置
# 后续找元素时，没找到时则等待10去寻找（一旦找到则继续）
driver.implicitly_wait(30)

driver.get('https://passport.bilibili.com/login')

sms_btn = driver.find_element(
    By.XPATH,
    # '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
    '//*[@id="xxxxxxxxxapp"]/div[2]/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()
print("找到了")
time.sleep(250)
driver.close()
