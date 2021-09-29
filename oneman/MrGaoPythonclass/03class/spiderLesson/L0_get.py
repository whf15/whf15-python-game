import requests

# 百度首页搜索案例

# url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%B8%87%E9%97%A8%E5%A4%A7%E5%AD%A6&fenlei=256&rsv_pq=ea79102e00017d8c&rsv_t=0434eAqshv2OlIu%2FTBOUSVkNrZ4o2Bvd8wFI7OgNROn7lstUm%2Bj1icRPt8U&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=13&rsv_sug1=9&rsv_sug7=101'
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%B8%87%E9%97%A8%E5%A4%A7%E5%AD%A6&fenlei=256&rsv_pq=ea79102e00017d8c&rsv_t=0434eAqshv2OlIu%2FTBOUSVkNrZ4o2Bvd8wFI7OgNROn7lstUm%2Bj1icRPt8U&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=13&rsv_sug1=9&rsv_sug7=101'
header = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

res = requests.get(url=url, headers=header)

res.encoding = 'utf-8'

print(res.text)

with open('aaa.html', 'a',encoding='utf-8') as add:
    add.write(res.text)
