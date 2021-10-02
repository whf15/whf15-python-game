import requests
import re
from bs4 import BeautifulSoup
#电影评论 静态请求
url = 'https://www.1905.com/pinglun/'
res = requests.get(url)
res.encoding = 'utf-8'
# print(res.text)

#电影评论的
soup = BeautifulSoup(res.text,'lxml')
# info = soup.find_all(name='div',attrs={'class':'comment-list'})[0].find_all('li')


info = soup.select('.comment-list >ul li')

for li in info:
    # print(li)
    print('*'*100)

    title = li.select('li>a')[0].attrs['title']
    print(title)
    detail_page_link = li.select('li>a')[0].attrs['href']
    print(detail_page_link)
    img = li.select('li>a>img')[0].attrs['src']
    print(img)
    abstract_text = li.select('li > .list-txt >.txt-abstract')[0].text
    print(abstract_text)
    print(title, detail_page_link, img, abstract_text)


