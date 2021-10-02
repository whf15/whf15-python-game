import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
#证监会
url = 'http://eid.csrc.gov.cn/1011/index_1.html'
header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

res = requests.get(url=url, headers=header)
res.encoding='utf-8'
# print(res.text)

#TODO 正则

patt = r'<td width="100px;"><a style=".*?" onclick=".*?">(.*?)</a></td>.*?<td width="150px;">(.*?)</td>.*?<td width="400px;"  onclick="downloadPdf1(.*?);">'
res_1 = re.findall(pattern=patt, string=res.text, flags=re.S)

# print(res_1)
# for  x in res_1:
#     print(x)
# for x in res_1:
#     print(x)
#     print(x[0],x[1])
#     print( eval(x[2])[0] )
#     print( eval(x[2])[1] )

# temp = "('http://static.sse.com.cn/disclosure/listedinfo/announcement/c/2020-12-31/600623_20201231_2.pdf','关于收到政府补助的公告','2020-12-31','1011','pdf')"
#
# temp_1 = eval(temp)
# print(temp_1)
# print(temp_1[0])



#TODO bs4 lxml
soup = BeautifulSoup(markup=res.text, features='lxml')
res_2 = soup.select('.m-table2 tr')
print(len(res_2))
#过程说明
# for x in res_2:
#     print('*'*100)
#     print(x)
#     print('#'*100)

# for index, x in enumerate(res_2):
#     print(index,'**********',x)
#     lower_level = x.select('td')
#     print('&'*100)
#     print(lower_level)
#
#
# for x in res_2[1:len(res_2)]:  #注意这里的列表提取长度
#     print('**********')
#     td_level = x.select('td')
#     # print(td_level)
#     stock_id = td_level[0].select('a')[0].text #股票代码
#     abbr_name = td_level[1].text
#     report = td_level[2].attrs['onclick'] #需要正则处理或split切割 这个属性值
#     # print(stock_id, abbr_name, report)
#     report = report.split("'")
#     print(report)
#     title = report[3]
#     pdf = report[1]
#
#     print(stock_id,abbr_name,title,pdf)


#TODO etree+xpath
tree = etree.HTML(res.text)
# print(res.text)
res_3 = tree.xpath('//*[@id="txt"]/table/tr')
# for x in res_3[1:len(res_3)]:
#     # print(x)
#     td = x.xpath('./td') #锁定每一行td
#     # print(td)
#     # print('8'*100)
#     stock_id = td[0].xpath('./a')[0].text  # 股票代码
#     abbr_name =td[1].text
#     report = td[2].xpath('@onclick')
#     report = report[0].split("'")
#     title = report[3]
#     pdf = report[1]
#     print(stock_id,abbr_name,title,pdf)
#
