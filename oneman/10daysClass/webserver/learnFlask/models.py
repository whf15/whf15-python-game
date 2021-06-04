from config import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(128))

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password