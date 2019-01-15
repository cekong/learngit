''''''
'''
定义蓝图
'''
from flask import Blueprint


web=Blueprint('web',__name__)


from my_flask_register_login.register_login.web import register
from my_flask_register_login.register_login.web import login
