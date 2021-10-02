import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

#互联网数据资讯
url = 'http://www.199it.com/archives/category/service/3g/page/5'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

res = requests.get(url=url, headers=header)
res.encoding='utf-8'
# print(res.text)

# TODO 正则
patt = '<div class="post-img"><div itemprop="image" itemscope="" itemtype=".*?" class="post-thumb"><a href="(.*?)" title="(.*?)"><img itemprop="url" src="(.*?)" class="attachment-post-thumbnail wp-post-image" alt=".*?"></a> <meta itemprop="width" content="228"><meta itemprop="height" content=".*?"></div></div>'
res1 = re.findall(pattern=patt,string=res.text, flags=re.S)
# print(res1)
# for x in res1:
#     print(x[0],x[1],x[2])
#


#TODO bs4+lxml

soup = BeautifulSoup(markup=res.text,features='lxml')
res_2 = soup.find_all(name='article',attrs={'class':'newsplus'})
# print(res_2)
# print(len(res_2))
# for x in res_2:
#     # print(x.find_all(name='a'))
#     # print(x.find_all(name='a'))
#     print(x.find_all(name='a')[0].attrs['href'])
#     print(x.find_all(name='a')[0].attrs['title'])
#     # print(len(x.find_all(name='a')))

#TODO etree+xpath


tree = etree.HTML(res.text)   #必须要指定 解析器为HTML解析器

res_3_titles_links = tree.xpath('//*[@id="content"]/article//div[@itemprop="image"]/a')

# print(res_3_titles_links)
# print(len(res_3_titles_links))
#
# for x in res_3_titles_links:
#     titles = x.xpath('@title')
#     links = x.xpath('@href')
#     print(titles[0], links[0])
#
