
#在爬取过程中 查重的问题
import sqlite3
conn = sqlite3.connect('myDATA.db')
c = conn.cursor()
#双条件查询 使用 WHERE + AND
res = c.execute("select * from cities  WHERE city_name='安国' AND city_links='ag.fang.ke.com/loupana' ")
print(len([x for x in res]))




