''''''
'''
核心对象初始化
https://coding.imooc.com/lesson/194.html#mid=12772


templates（模板文件）和 static（静态文件）都是flask默认的文件夹
如果想修改路径，app = Flask(__name__,template_folder='',static_folder='')
'''

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from app.models.book import db
from app.libs.limiter import Limiter

login_manager = LoginManager()
mail = Mail()
limiter = Limiter()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 导入配置文件
    app.config.from_object('app.setting')  # 导入配置文件
    register_blueprint(app) # 蓝图与核心对象关联

    db.init_app(app) # db与核心对象关联
    with app.app_context():
        db.create_all()#创建数据库
    #### db.drop_all()#删除库

    login_manager.init_app(app)# login_manager与核心对象关联
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)# mail与核心对象关联
    return app

def register_blueprint(app): #把蓝图注册到app上
    from app.web.book import web
    app.register_blueprint(web)