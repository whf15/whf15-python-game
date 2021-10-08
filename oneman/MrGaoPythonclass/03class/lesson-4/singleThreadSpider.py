import sqlite3
from bs4 import BeautifulSoup
import requests
import time

conn = sqlite3.connect('houseDB.db')
c = conn.cursor()
# Create table
# c.execute('''CREATE TABLE house_info
#              (city, estate, price, address, condition, type ,img ,unit)''')
# conn.commit()

current_city = '北京'

#图下载
def photo_download(link):
    img = requests.get(link).content
    with open('images/%s.jpg'%link.split('/')[-1], 'wb') as w:
        w.write(img)

#数据库保存
def data_save(data):
    c.executemany("INSERT INTO house_info VALUES (?,?,?,?,?,?,?,?)", data)
    conn.commit()

#总页码统计
def total_page_check():
    res = requests.get(url = 'http://bj.fang.ke.com/loupan/pg1')
    soup = BeautifulSoup(res.text, 'lxml')
    total = soup.select('.page-box')[0].attrs['data-total-count']
    #判断为整数
    total_info = int(total) / 10
    if str(total_info).split('.')[-1] == '0':
        total_page = int(total) / 10
    else:
        total_page = int(total) / 10 + 1

    print('总数据量',total)
    return  int(total_page)

#主爬虫
def main_spider(totalpage):
    for page in range(1,totalpage+1):
        url = 'http://bj.fang.ke.com/loupan/pg%s/'%page
        print('@link->>',url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'lxml')
        main_data_list = []
        main_target = soup.select('.resblock-list') #list[1,2,3]
        for x in main_target:
            temp_list = []

            temp_list.append(current_city)

            estate = x.select('.name')[0].text
            temp_list.append(estate)

            price = x.select('.number')[0].text
            temp_list.append(price)

            address = x.select('.resblock-location')[0].text.strip()
            temp_list.append(address)

            condition = x.select('.resblock-name span')[0].text
            temp_list.append(condition)

            types = x.select('.resblock-name span')[1].text
            temp_list.append(types)

            img_link = x.select('a>img')[0].attrs['data-original']
            temp_list.append(img_link)
            photo_download(img_link)

            unit = x.select('.desc')[0].text

            temp_list.append(unit.strip())

            main_data_list.append(temp_list)

        print(main_data_list)

        print('本页爬取数据量*******',len(main_data_list))
        data_save(main_data_list)


if __name__ == '__main__' :
    print(total_page_check())

    start = time.time()

    total_page = total_page_check()
    main_spider(total_page)

    time_consumed = time.time() - start
    print('耗时:--->>',time_consumed)
