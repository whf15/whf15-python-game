import requests
import json


#django后台登陆
url = 'http://www.ppcam.cn/admin/login/'
header = {
    'Cookie': 'csrftoken=Yd8BbmTZ0OaOJMRPqa48aCiKfxguB8dAtlPCQ1hFsRr0ZAoFkNG5s16Nh6xy76XY',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

data = {
    'username': 'zhengzheng',
    'password': 'Gaozheng123123',
    'csrfmiddlewaretoken': 'CC6EgnpXZ1ayMosI7DSHS4UgryBN6ipQ7KNFV2NDr4rK2cZy1guEatIjt7SRCg9e',
    'next': '/admin/'
}

# res = requests.post(url=url, data=data, headers=header)
# res.encoding='utf-8'
# print(res.text)
#
#
#
#
#
# #后台内部单独访问演示-
# url = 'http://www.ppcam.cn/admin/PowerAPP/photos/' #http://www.ppcam.cn/admin/PowerAPP/photos/
# res1 = requests.get(url=url)
# print('@@@@@@@@'*10)
# print(res1.text)
#


#session联合登陆


url = 'http://www.ppcam.cn/admin/login/'
header = {
    'Cookie': 'csrftoken=Yd8BbmTZ0OaOJMRPqa48aCiKfxguB8dAtlPCQ1hFsRr0ZAoFkNG5s16Nh6xy76XY',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}

data = {
    'username': 'zhengzheng',
    'password': 'Gaozheng123123',
    'csrfmiddlewaretoken': 'CC6EgnpXZ1ayMosI7DSHS4UgryBN6ipQ7KNFV2NDr4rK2cZy1guEatIjt7SRCg9e',
    'next': '/admin/'
}

sess = requests.Session()

res = sess.post(url=url, data=data, headers=header)
print(res.text)
print('@@@'*10)
url = 'http://www.ppcam.cn/admin/PowerAPP/photos/'
res1 = sess.get(url=url)
print(res1.text)