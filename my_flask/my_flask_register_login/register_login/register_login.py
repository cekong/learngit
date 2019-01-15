# -*- coding: UTF-8 -*-


from flask import Flask

from my_flask_register_login.register_login.web.register import web
from my_flask_register_login.register_login.models import db
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:password@127.0.0.1:3306/register_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='124896214'
#设置这一项是每次请求结束后都会自动提交数据库中的变动

db.init_app(app) # db与核心对象关联
app.register_blueprint(web)





if __name__ == '__main__':
    app_ctx = app.app_context()
    with app_ctx:
        db.create_all()
    app.run(debug=True)
