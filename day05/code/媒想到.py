import hashlib
import requests

data_string = "qwe123456" + "Hq44cyp4mT9Fh5eNrZ67bjifidFhW%fb0ICjx#6gE59@P@Hr8%!WuYBa1yvytq$qh1FEM18qA8Hp9m3VLux9luIYpeYzA2l2W3Z"
obj = hashlib.md5()
obj.update(data_string.encode("utf-8"))
md5_string = obj.hexdigest()
res = requests.post(
    url="https://www.94mxd.com.cn/mxd/user/signin",
    json={
        "email": "22107@163.com",
        "password": md5_string
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": "https://www.94mxd.com.cn/signin",
        "Origin": "https://www.94mxd.com.cn"
    }
)
print(res.text)
print(res.cookies.get_dict())
