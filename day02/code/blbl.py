import json

import requests

res = requests.get(
    url="https://api.bilibili.com/x/member/web/account?web_location=333.33",
    headers={
        "Cookie": "buvid3=5D0FE722-A57B-BC75-390E-76EF549C2D2608650infoc; b_nut=1710181308; i-wanna-go-back=-1; b_ut=7; b_lsid=AEDB6DE3_18E2EBFD9BC; bsource=search_bing; _uuid=76915CFC-77E9-9F102-3557-D2A6B3217D1208871infoc; enable_web_push=DISABLE; buvid4=481C1801-77DD-AB4A-1AA6-686C7851F4E609034-024031118-MBmq4Uc9by63ScyjvfRO8g%3D%3D; buvid_fp=1f99ffb9546947a065bc82eb4af76b35; home_feed_column=5; browser_resolution=1920-408; PVID=1; FEED_LIVE_VERSION=V_SIDE_TO_FEED; header_theme_version=CLOSE; SESSDATA=a0429d6d%2C1725733925%2Ccecf7%2A32CjC-laXb86nRjwbYYuYj-9twhmjr-7qSryW6i254YLFM2h0oRkkSz8yvHdnMFVSaoI4SVmxRa2FkUXdhbTFBTFVPaEZLQnJPcXh0dFpTcmNqTmlHMWp1U2NHTFVHcWhXN2lPbllHcV80UmhtUC0xbDNzdEJUYjBrVm1sd05XZGo2RHU2U3luaW5RIIEC; bili_jct=89fa274e41687ebf843308ffbb281e3e; DedeUserID=342595067; DedeUserID__ckMd5=05541e3f1842f4d0; sid=6lvjeu99; bp_video_offset_342595067=907638134281338884; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA0NDExMzYsImlhdCI6MTcxMDE4MTg3NiwicGx0IjotMX0.WeLPhiTMNtdQX3jaYwhIDWvWS-HTCWvVVxyGHzl3yZQ; bili_ticket_expires=1710441076",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://account.bilibili.com/"
    }
)
data_dict = json.loads(res.text)
pin_lint = data_dict["data"]
print(pin_lint)
for key, value in pin_lint.items():
    print(key, value)
