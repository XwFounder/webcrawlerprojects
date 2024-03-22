import base64
import requests
from hashlib import md5

file_bytes = open('bg.png', 'rb').read()

res = requests.post(
    url='http://upload.chaojiying.net/Upload/Processing.php',
    data={
        'user': "wupeiqi",
        'pass2': md5("qwe123..".encode('utf-8')).hexdigest(),
        'codetype': "9501",
        'file_base64': base64.b64encode(file_bytes)
    },
    headers={
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
)

res_dict = res.json()
print(res_dict)