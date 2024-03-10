import requests
import json

url ="https://api.huaban.com/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations,rec_topic_material"
res = requests.get(
    url=url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
)

# print(res.text)
data_dict = json.loads(res.text)
pin_list = data_dict["pins"]
for item in pin_list:
    print(item['user']['username'], item['raw_text'])
