import base64

import ddddocr
import requests
import cv2
import numpy as np
import requests


bg_bytes = requests.get("https://static.geetest.com/captcha_v4/e70fbf1d77/slide/0af8d91d43/2022-04-21T09/bg/33a8f24a9b234a599036569c9e54a76a.png").content
b64_string = base64.b64encode(bg_bytes).decode('utf-8')
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图
data = {"username": "自己账号", "password": "自己密码", "typeid": 33, "image":b64_string }
res = requests.post("http://api.ttshitu.com/predict", json=data)
data_dict = res.json()
distance = data_dict['data']['result']
print(distance)
# {"success":true,"code":"0","message":"success","data":{"result":"136","id":"ztAkFAn1RvOJGsFhiAPuWg"}}