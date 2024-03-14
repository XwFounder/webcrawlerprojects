# 分析：1、查找图片验证码接口信息进行筛选
#  图片验证码url:https://hrtechchina.com/register/authimg
#  $(this).attr('src', '/home/register/authimg?' + Math.random());
import ddddocr
import requests
import random

random_number = random.random()
img_url = "https://hrtechchina.com/register/authimg?" + str(random_number)
print(img_url)
res = requests.get(
    url="https://hrtechchina.com/register/authimg",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://hrtechchina.com/register",
        "Origin": "https://hrtechchina.com"
    }
)
ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)
# 发送短信验证码
smsCode_res = requests.post(
    url="https://hrtechchina.com/register/aveCode",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Origin": "https://hrtechchina.com",
        "Referer": "https://hrtechchina.com/register",
        "Content-Type": "application/json; charset=utf-8"
    },
    json={
        "mobile": "",
        "authimg": code
    }
)
print(smsCode_res.json())

# 注册验证
# register_res = requests.post(
#     url="https://hrtechchina.com/register/register",
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#         "Origin": "https://hrtechchina.com",
#         "Referer": "https://hrtechchina.com/register",
#         "Content-Type": "application/json; charset=utf-8"
#     },
#     json={
#         "mobile": "",
#         "password": "123456",
#         "authcode": "1234"
#     }
#
# )
