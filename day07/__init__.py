import json


json_data = '''
{
  "logs": "[{\"action\":\"impress\",\"json\":{\"mspm\":\"619df35ce51b6b383f5fafdb\",\"page\":\"mainpage\",\"module\":\"nav_bar\",\"target\":\"friends\",\"reddot\":\"1\",\"mainsite\":\"1\"}}]",
  "csrf_token": "534c3a0c31c8f8f6a6204182c9e705b1"
}
'''

data_str = json.dumps(json_data)  # 将字典转换为 JSON 字符串
data = json.loads(data_str)  # 解析 JSON 字符串为 Python 对象
print(data)
# print(json_data)