import time
import hashlib

import requests

# 1.首页
res = requests.get(url="https://bbs.pku.edu.cn/v2/home.php")
cookie_dict = res.cookies.get_dict()

# 2.登录
username = "wupeiqi"
password = "123123"
ctime = int(time.time())
# 通过代码实现MD5,然后通过hashlib 进行转化md5
data_string = f"{password}{username}{ctime}{password}"
#
obj = hashlib.md5()
obj.update(data_string.encode('utf-8'))
md5_string = obj.hexdigest()
#
res = requests.post(
    url="https://bbs.pku.edu.cn/v2/ajax/login.php",
    data={
        "username": username,
        "password": password,
        "keepalive": "0",
        "time": ctime,
        "t": md5_string
    },
    cookies=cookie_dict
)

print(res.text)
