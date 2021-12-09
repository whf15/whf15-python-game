from hashlib import md5
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

    # 粉丝机制
    # followers = db.Table('followers',
    #     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    #     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
    # )
    followers = db.Table('followers',
        db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
    )

    # 更多有趣得个人资料
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    followed = db.relationship(
        # 右侧实体，自引用关系
        'User',
        # 指定用于该关系的关联表
        secondary=followers,
        # 通过关联表关联到左侧实体（关注者）的条件
        primaryjoin=(followers.c.follower_id == id),
        # 通过关联表关联到右侧实体（被关注者）的条件
        secondaryjoin=(followers.c.followed_id == id),
        # 右侧实体如何访问该关系
        backref=db.backref('followers',lazy='dynamic'),
        lazy = 'dynamic'
    )
    # 用于在调试时打印用户实例
    def __repr__(self):
        return '<User {}>'.format(self.username)

 # 密码哈希逻辑，在无d需持久化存储原始密码的条件下执行安全的密码验证
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    # Post.query.join(...).filter(...).order_by(...)
    def followed_posts_test(self):
        return Post.query.join(
                followers,
                (followers.c.followed_id == Post.user_id)
            ).filter(followers.c.follower_id == self.id
            ).order_by(Post.timestamp.desc()
            )
        
    def followed_posts(self):
        followed = Post.query.join(
            followers,
            (followers.c.followers.c.follower_id == Post.user_id)
        ).filter(followers.c.followed_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())
        
    # 头像
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://gravatar.loli.net/avatar/{}?d=identicon&s={}'.format(digest, size)


# 为用户加载功能注册函数，将字符出类型的参数id出入用户加载函数
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# 表示用户发表的动态
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post{}>'.format(self.body)

