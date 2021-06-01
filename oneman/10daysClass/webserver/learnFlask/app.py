from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! Whf15'

@app.route('/hello')
def hello_Whf15():
    return 'Hello Whf15!'

if __name__ == '__main__':
    app.run()
