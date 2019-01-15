''''''
'''
url_for
https://www.cnblogs.com/c-x-a/p/8821293.html

Flask Web中的 url_for 函数
https://blog.csdn.net/dengfan666/article/details/78320188#
'''

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    login_url = url_for('login')
    print(login_url)
    return redirect(login_url)
    return u'这是首页'


@app.route('/login/')
def login():
    return u'这是登陆页面'

@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return  u'这是发布问答的页面'
    else:
        return  redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)