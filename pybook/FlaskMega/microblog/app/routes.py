from flask import render_template
from app import app

# 行装饰器，在作为参数的URL和函数之间创建一个关联
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'whf15'} #fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # return "Hello,world! My name is whf15"
    # return '''
    # <html>
    #     <head>
    #         <title>micrblog</title>
    #     </head>

    #     <body>
    #         <h1>Hello, ''' + user['nickname'] + '''</h1>
    #     </body>
    # </html>
    # '''
    return render_template("index.html",
        title = "Home",
        user = user,
        posts = posts
    )