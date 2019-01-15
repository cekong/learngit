''''''
"""
http://www.cnblogs.com/zzy-9318/p/9215567.html

"""


from flask import Flask, session, redirect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.secret_key = 'asdfasdfasd'

# 设置数据库链接
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:password@127.0.0.1:3306/test'#用于连接数据的数据库。

# 实例化SQLAlchemy
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'  # session类型为sqlalchemy
app.config['SESSION_SQLALCHEMY'] = db  # SQLAlchemy对象
app.config['SESSION_SQLALCHEMY_TABLE'] = 'session' # session要保存的表名称

Session(app)

db.create_all()


@app.route('/login/')
def login():
    session['username'] = 'john'
    return redirect('/index')


@app.route('/index/')
def index():
    name = session['username']
    return name


if __name__ == '__main__':
    app.run(debug=True)

