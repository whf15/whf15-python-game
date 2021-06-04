from config import db
from models import User

# create database and data table create
db.create_all()

# insert data
db.session.add(User("whf15","whfoxxx1999@163.com","whfoxxx1999"))
db.session.add(User("whfoxxx","1211368233@qq.com","whfoxxx1999"))
db.session.add(User("whfo","1211368233@qq.com","whfoxxx1999"))

db.session.commit()