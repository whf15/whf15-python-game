import requests
import json

#百度翻译案例
# url = 'https://fanyi.baidu.com/sug'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
# }
#
# data = {
#     'kw': 'good'
# }
#
# res = requests.post(url=url, data=data, headers=header).json()
# for x in res['data']:
#
#     print(x)
#

#搜狗翻译案例
url = 'https://fanyi.sogou.com/reventondc/suggV3'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

data = {
'from': 'auto',
'to': 'zh-CHS',
'client': 'wap',
'text': 'practice',
'uuid': '34ae1795-72a7-465d-b8ba-2e8eb4645ad2',
'pid': 'sogou-dict-vr',
'addSugg': 'on',
}

res = requests.post(url=url, data=data, headers=header).json()
print(type(res))
print(res)

