import ddddocr
import requests

res = requests.get(url="https://console.zbox.filez.com/captcha/create/reg?_t=1701511836608")

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)