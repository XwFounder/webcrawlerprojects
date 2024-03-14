
import ddddocr
import requests

res = requests.post(
    url="https://api.ruanwen.la/api/auth/captcha/generate",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://i.ruanwen.la/",
        "Origin":  "https://i.ruanwen.la"
    }
)
res_dict = res.json()
captcha_token = res_dict["data"]["captcha_token"]
captcha_url = res_dict["data"]["src"]

# 访问并获取图片验证码
res = requests.get(captcha_url)
#  识别验证码
ocr = ddddocr.DdddOcr(show_ad=float)
code = ocr.classification(res.content)
print(code)
#  登录验证
res = requests.post(
    url="https://api.ruanwen.la/api/auth/authenticate",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://i.ruanwen.la/",
        "Origin":  "https://i.ruanwen.la",
        "Content-Type": "application/json;charset=UTF-8"
    },
    json={
        "mobile":"123456789",
        "device": "pc",
        "captcha_token": captcha_token,
        "captcha": code,
        "password": "Xw22187",
        "identity": "advertiser"
    }
)
print(res.json())
