from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
def hello():
    return 'Hello Everyone'

@app.route('/user/<username>/')
def show_user_profile(username):
    return username

@app.route('/index/')
def index():
    return render_template('hello.html')

@app.route('/login/')
def login():
    pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('show_user_profile', username='John')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
