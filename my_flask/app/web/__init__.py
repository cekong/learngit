''''''
'''
定义蓝图
'''
from flask import Blueprint
from flask import render_template


web=Blueprint('web',__name__)

@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404
'''
flask中响应错误的处理及errorhansdler的应用
https://blog.csdn.net/rytyy/article/details/78947045
'''

#保证book.py等文件可以被执行
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import test