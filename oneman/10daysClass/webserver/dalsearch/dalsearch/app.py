from flask import Flask, request, render_template
import pymysql
import pymysql.cursors
import json

app = Flask(__name__)
db =  pymysql.connect(host='localhost',
                    user='seuser',
                    password='se!@#$',
                    db='dalsearch',
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
@app.route('/')
def hello_world():
    return render_template('layout.html')


@app.route('/search')
def search_result(methods=['GET']):
    keywords = request.args.get('q', '')
    if keywords:
        with db.cursor() as cursor:
            q_sql = "SELECT * FROM dalsearch.document_page where pagecontent like '%{key}%'".format(key=keywords);
            cursor.execute(q_sql)
            result = cursor.fetchall()

        return render_template('result.html', search = result)


if __name__ == '__main__':
    app.run()
