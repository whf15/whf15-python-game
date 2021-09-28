import requests
import json

#百度图片下载
url = 'https://image.baidu.com/search/acjson'
header = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Host': 'image.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
 }

params = {
    'tn': 'resultjson_com',
    'logid': '12529618415259269141',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'queryWord': '德牧',
    'cl': '2',
    'lm': '-1',
    'ie': 'utf - 8',
    'oe': 'utf - 8',
    'adpicid': '',
    'st': '-1',
    'z': '',
    'ic': '',
    'hd': '',
    'latest': '',
    'copyright': '',
    'word': '德牧',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '0',
    'istype': '2',
    'qc': '',
    'nc': '1',
    'fr': '',
    'expermode': '',
    'force': '',
    'pn': '10',
    'rn': '10',
    'gsm': '78',
}

res = requests.get(url=url, params=params, headers=header).json()
for x in res['data']:
    print(x)
    if len(x) == 0:
        pass
    else:
        print(x['thumbURL'])
        img = requests.get(url=x['thumbURL']).content
        filename = x['thumbURL'].split('/')[-1]
        with open('images/%s'%filename,'wb') as w:
            w.write(img)
