from flask import render_template, flash, redirect, url_for
from app import app
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

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

@app.route('/login', methods = ['GET', 'POST'])
# @app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # flash('Login request for user {}, remember_me={}'.format(
        #     form.username.data,form.remember_me.data
        # ))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html',
        title = 'Sign In',
        form = form
    )



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))