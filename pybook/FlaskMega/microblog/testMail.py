from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=465,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'whfoxxx1999@163.com',
    MAIL_PASSWORD = 'KCGUTJTQTMAVCFDT',
    # MAIL_pass = 'KCGUTJTQTMAVCFDT',
    MAIL_DEBUG = True
)

mail = Mail(app)

@app.route('/')
def index():
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='whfoxxx1999@163.com', recipients=['1211368233@qq.com'])
# msg.body 邮件正文 
    msg.body = "This is a first email"
# msg.attach 邮件附件添加
# msg.attach("文件名", "类型", 读取文件）
    mail.send(msg)
    print("Mail sent")
    return "Sent"

if __name__ == "__main__":
    app.run()