from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db,login
from flask_login import UserMixin

# class User(db.Model):
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # 用户与其动态之间关系的高级视图，一般relationship字段处于‘一’
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # 用于在调试时打印用户实例
    def __repr__(self):
        return '<User {}>'.format(self.username)

# 密码哈希逻辑，在无d需持久化存储原始密码的条件下执行安全的密码验证
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# 为用户加载功能注册函数，将字符出类型的参数id出入用户加载函数
@login.user_loader
def load_user(id):
    return Uer.query.get(int(id))
# 表示用户发表的动态
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post{}>'.format(self.body)

