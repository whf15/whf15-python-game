from flask import (Flask,request,
                send_from_directory,render_template,
                redirect,url_for)
import pymysql
import pymysql.cursors
from config import db,app
from models import BlogPost
#在config.py中已经初始化过
# app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World! Whf15'

@app.route('/hello/<name>')
def hello_Whf15(name=None):
    return 'Hello : '+ name

@app.route('/getpost/<int:postid>')
def postId(postid):
    return 'Hello : '+ str(postid)

@app.route('/files/<path:filename>')
def getdownload(filename):
    return send_from_directory("download",filename)

@app.route('/template/<name>')
def template_hello(name=None):
    return render_template("mytest.html",user=name)
    # 方法一.在该py文件的同级目录下,建立templates文件夹,将test.html文件放入其中.

#外部链接的跳转
@app.route('/redirect')
def redirect_test():
    # return redirect("/hello")
    return redirect(url_for("hello_world"))

#捕捉异常404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

#connect db
@app.route("/db/<name>")
def get_db_connect(name):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="whfoxxx1999",
        db="sakila",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sakila.actor limit 10;")
        result = cursor.fetchall()
        return render_template("actorlist.html",actor=result)

    return render_template("404.html"),404


@app.route("/posts")
def list_blog():
    posts = db.session.query(BlogPost).all()
    return render_template("mypost.html",posts=posts)

if __name__ == '__main__':
    app.run()
