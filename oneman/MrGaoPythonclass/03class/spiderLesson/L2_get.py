import requests
import json

#头条案例

url = 'https://www.toutiao.com/api/search/content/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

params = {
    'aid': '24',
    'app_name': 'web_search',
    'offset': '100',
    'format': 'json',
    'keyword': ' 泰山',
    'autoload': 'true',
    'count': '20',
    'en_qc': '1',
    'cur_tab': '1',
    'from': 'search_tab',
    'pd': 'synthesis',
    'timestamp': '1608479020632',
}

res = requests.get(url=url, params=params, headers=header)#.json()

# print(res.text)


for x in res.json()['data']:
    print(x)



