
import sqlite3
import requests
from lxml import etree

conn = sqlite3.connect('cities.db')
c = conn.cursor()

c.execute('''CREATE TABLE cities
             (city_name, city_links)''')
conn.commit()

#注意这个特殊的案例使用xpath 更方便， 同样的数据一个页面出现两次

res = requests.get('http://bj.fang.ke.com/loupan/pg1')
tree = etree.HTML(res.text)
city = tree.xpath('/html/body/div[2]/div[3]//a')
total_city = []
for x in city:
    # print(x.text)
    # print(x.xpath('@href')[0].split('//')[-1])
    # print(x.text,x.xpath('@href')[0])           # bs4 attrs['href']
    total_city.append([x.text, x.xpath('@href')[0].split('//')[-1]])
print(total_city)

c.executemany("INSERT INTO cities VALUES (?,?)",total_city)
conn.commit()




