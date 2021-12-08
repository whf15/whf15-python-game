from hashlib import md5
from flask import render_template, flash, redirect, url_for,request
from app import app, db
from .forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User
from datetime import datetime

# 行装饰器，在作为参数的URL和函数之间创建一个关联
@app.route('/')
@app.route('/index')
@login_required
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
        posts = posts
    )

# 登录模块
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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template('login.html',
        title = 'Sign In',
        form = form
    )


# 登出模块
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# 注册模块
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/user/<username>")
@login_required
def user(username):
    # first方法的变种，在没有结果的情况下会自动发送404 error给客户端
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]

    return render_template('user.html', user= user, posts = posts)

# 查看显示最后访问时间
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',title='Edit Profile',form = form)

