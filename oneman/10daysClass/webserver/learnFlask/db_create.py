from config import db
from models import User,BlogPost

# create database and data table create
db.create_all()

# insert data
db.session.add(User("whf15","whfoxxx1999@163.com","whfoxxx1999"))
db.session.add(User("whfoxxx","1211368233@qq.com","whfoxxx1999"))
db.session.add(User("whfo","1211368233@qq.com","whfoxxx1999"))

db.session.add(BlogPost("Good","I\'m good."))
db.session.add(BlogPost("Well","I\'m well."))
db.session.add(BlogPost("Excellent","I\'m excellent."))
db.session.add(BlogPost("Okay","I\'m okay."))
db.session.add(BlogPost("postgres","we setup a local postgres instance."))


db.session.commit()