# https://github.com/pawelsalawa/sqlitestudio/releases
import sqlite3

conn = sqlite3.connect('my_data.db')

c = conn.cursor()

# # 创建表
# c.execute('''CREATE TABLE info
#              (name, age, school)''')
# conn.commit()

#
# c.execute('ALTER TABLE info ADD date')
# conn.commit()

#多数据添加
# infomation = [
#              ['mike4', 40, 'wanmen' ],
#              ['mike2', 20, 'wanmen' ],
#              ['mike1', "30", '' ],
#              ['mike1', "45", 'wanmendaxue' ]
#             ]
# c.executemany('INSERT INTO info VALUES (?,?,?)', infomation)
# conn.commit()

#单数据添加
# name = 'hike'
# age = 50
# school = 'wanmendaxue'
# c.execute('INSERT INTO info VALUES("%s","%s","%s")'%(name,age,school))
# conn.commit()

# #数据查询

# for row in c.execute('SELECT * FROM info'):
#     print(row)


##带条件查询
# for row in c.execute('SELECT * FROM info WHERE age>30'):
#     print(row)
