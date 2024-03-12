import requests
from bs4 import BeautifulSoup

# res = requests.post(
#     url="https://passport.china.com/logon",
#     data={
#         "userName": "18975732620",
#         "password": "18975732620Wlp"
#     },
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#         "Referer": "https://passport.china.com/logon",
#         "Origin": "https://passport.china.com",
#         "X-Requested-With": "XMLHttpRequest"
#     }
# )
# 获取cookie信息
# cookie_dict = res.cookies.get_dict()
cookie_dict={'CHINACOMID': '3c76b363-9228-4e39-b07f-6660943b8e728', 'CP_USER': 'FKBo6w-aaDHWwabUadHVbwmZitclewQBzIpsuaQNIsL1ScepDkVBfKuhsWkgBos%2FWaYsYpIpoO8MMVq%2FMzPv0nEtwtcqq5gvsmf5heVgMBna256tsjJWvQOtNIEqA25zi-Uc3Mfh9kg8qzaEGqQNdZ9MIXu029WzR5uzckxvNkGjDm6IT59F-cemjgD0Axbd79GLteRP%2F8O5yDsfrY5yuar-AYo3fcMqmlLJ6WjemIAiC44IuLq2ow%3D%3D', 'CP_USERINFO': '4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D', 'bindMobile': '"1@189*****620"', 'china_variable': 'jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza', 'lastlogindate': '2024-03-13', 'lastloginip': '113.102.239.76', 'lastlogintime': '"01:51:37"', 'nickname': 'china_1419xhgb16791140', 'SESSION_COOKIE': '118'}

# print(cookie_dict)
res = requests.get(
    url="https://passport.china.com/main",
    cookies=cookie_dict
)
# print(res.text)
soup=BeautifulSoup(res.text, features="html.parser")
tags = soup.find(attrs={"id": "usernick"})
print(tags.text)
print(tags.attrs['title'])