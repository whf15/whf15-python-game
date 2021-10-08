from threading import Thread
import threading
from time import sleep
import sqlite3
from bs4 import BeautifulSoup
import requests
import time
import random


#总页码统计
def total_page_check(link):
    res = requests.get(url = link)
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

# 数据库保存
def data_save(data):
    conn = sqlite3.connect('houseDB.db')
    c = conn.cursor()
    c.executemany("INSERT INTO house_info VALUES (?,?,?,?,?,?,?,?)", data)
    conn.commit()


# 任务分配机制
def task_distribution_policy(total):
    a = total[0:int(len(total)/2)]
    b = total[int(len(total)/2):]
    return a,b
# task1, task2 = task_distribution_policy(total_task)

#总任务量
def task_distribution_deploy(link):
    total_pages = total_page_check(link) # http://XXXXXXXX /pg
    for page in range(total_pages):
        total_task.append(link + '/pg%s'%str(page+1))
    print('任务列表：' ,total_task)
    # print(len(total_task))
    return total_task #返回全部任务列表-所有需要访问的地址


#线程具体任务
def spider(urls):
    for url in urls:
        time.sleep(random.randint(1,4)) #随机延时
        print('@link->>',url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'lxml')
        main_data_list = []
        main_target = soup.select('.resblock-list' )
        for x in main_target:
            temp_list = []

            temp_list.append(current_city)
            #楼盘名字
            estate = x.select('.name')[0].text
            temp_list.append(estate)

            #价格
            try:
                price = x.select('.number')[0].text #3000 10000 价格待定
                temp_list.append(int(price))
            except ValueError:
                temp_list.append(price)

            #楼盘地址
            address = x.select('.resblock-location')[0].text.strip()
            temp_list.append(address)
            #楼盘状态
            condition = x.select('.resblock-name span')[0].text
            temp_list.append(condition)
            #楼盘类型
            types = x.select('.resblock-name span')[1].text
            temp_list.append(types)
            #图
            img_link = x.select('a>img')[0].attrs['data-original']
            temp_list.append(img_link)
            #单位 平米或套
            try:
                unit = x.select('.desc')[0].text
                temp_list.append(unit.strip())
            except IndexError:
                temp_list.append('N/A')
            main_data_list.append(temp_list)

        print(main_data_list)
        print('本页爬取数据量*******',len(main_data_list))
        data_save(main_data_list) #保存数据





if __name__ == '__main__' :
    #读取城市
    conn = sqlite3.connect('cities.db')
    c = conn.cursor()
    cities = c.execute("select * from cities")
    all_city = [x for x in cities] #列表推导
    print(all_city)
    #
    for city in all_city:

        time.sleep(random.randint(5,10))
        total_task =[]
        current_city = city[0]
        link = 'http://' + city[1]
        print('当前城市：*%s*,页面：%s'%(current_city,link))
        all_links = task_distribution_deploy(link)
        task1, task2 = task_distribution_policy(all_links)

        print('任务分配线程 1:',task1)
        print('任务分配线程 2:',task2)


    #多线程启动
        # start = time.time()
        t1 = Thread(target=spider, args=(task1,))
        t2 = Thread(target=spider, args=(task2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        # time_consumed = time.time() - start
        # print(time_consumed)

        print('*****城市%s******任务完成!!!!!!!!!'%current_city)


