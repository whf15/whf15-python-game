import requests

# 电影评论接口请求
url = 'https://www.1905.com/api/content/index.php'
header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
params = {
'm': 'converged',
'a': 'comment',
'page': '1',
'pagesize': '20',
#'callback': 'successgetall', #坑点
}
res = requests.get(url=url,params=params,headers=header).json()
# print(res)
# print(len(res['info']))
# for x in res['info']:
#
#     print(x['title'], x['description'], x['thumb'], x['url'] ,sep=' ## ')
#
#
res_page = requests.get('https://www.1905.com/video/play/1495921.shtml')
print(res_page.text)