import requests
from bs4 import BeautifulSoup


DATAURL = 'https://dzen.ru/profile/editor/id/5e31bdabfc77ce3ea9c698aa'

session = requests.session()

req_headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'sso_checked=1; yandexuid=1195659181613761089; _yasc=0/zYBf5M7jk1quzA3c5a0e4zcmJ4wVbIMlUM65p8Yh3bTQ==; gdpr=0; _ym_uid=1663408155880259737; _ym_d=1663408155; _ym_isad=2; yandex_login=Stiven-holland; Session_id=3:1663408337.5.1.1663408337690:1YaKLg:162.1.2:1|804956398.0.2|705192075.661737.2.2:661737|64:10003828.250730.cHWPX7rHKxzQxeTDmjXVRR7gRfw; ys=udn.cDrQndC40LrQuNGC0LAg0JrRg9C30L7QstC60L7QsiBbc29mdHdhcmVkZWJ1Z10%3D#c_chck.1540771021; mda2_beacon=1663408337705',
    'Host': 'dzen.ru',
    'Referer': 'https://dzen.ru/profile/editor/id/5e31bdabfc77ce3ea9c698aa',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
    'X-Csrf-Token': '0a889679ca21122853d65c6143d289cd957c9f02:1663444370683',
    'X-FP-Token': '1834d02c1f1:e96d5af3ead79a6c:2a08608b:9fbccf2bc607c2792644f6ea5a8cbcabd50d8870',
}

# Authenticate
r = session.post(DATAURL, headers=req_headers, allow_redirects=False)
r2 = session.get(DATAURL)

with open('test.html', 'w', encoding="utf-8") as output_file:
  output_file.write(r2.text)