import ddddocr

ocr = ddddocr.DdddOcr(show_ad=False)
with open("D:/vs/projects/seleniumTestJunit/dayproject/webcrawlerprojects/day06/img", mode="rb") as f:
    body = f.read()
code = ocr.classification(body)
print(code)