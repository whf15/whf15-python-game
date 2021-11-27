from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # 用户与其动态之间关系的高级视图，一般relationship字段处于‘一’
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # 用于在调试时打印用户实例
    def __repr__(self):
        return '<User {}>'.format(self.username)

# 表示用户发表的动态
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post{}>'.format(self.body)