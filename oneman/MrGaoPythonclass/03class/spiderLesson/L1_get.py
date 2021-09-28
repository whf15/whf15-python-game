import requests

#百度首页搜索案例
url = 'https://www.baidu.com/s'

header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

params = {
    "wd": "万门大学",
    'rsv_sug1': '10',
    'rsv_sug7': '101',
}

res = requests.get(url=url,params=params, headers=header)

res.encoding = 'utf-8'
print(res.text)

with open('index.html','a') as add:
    add.write(res.text)

