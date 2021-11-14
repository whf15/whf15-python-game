from app import app

# 行装饰器，在作为参数的URL和函数之间创建一个关联
@app.route('/')
@app.route('/index')
def index():
    return "Hello,world! My name is whf15"