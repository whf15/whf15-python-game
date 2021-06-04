from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://root:whfoxxx1999@localhost/test?charset=utf8"

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)