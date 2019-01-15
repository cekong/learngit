# -*- coding: UTF-8 -*-
''''''
'''
模型层

'''
from sqlalchemy import Column,String
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy() #实例化

# 注册表单
class dbRegister_Form(db.Model):
    __tablename__ = 'Register'
    name = Column(String(50),primary_key=True)
    _pwd = Column('pwd',String(100))

    @property  # 数据读取
    def pwd(self):
        return self._pwd

    @pwd.setter  # 数据写入
    def pwd(self, raw):
        self._pwd = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._pwd, raw)



def save_to_mysql(myform):
    reg_form = dbRegister_Form()
    reg_form.name = myform.name.data
    reg_form.pwd = myform.pwd.data

    db.session.add(reg_form)  # 准备把对象写入数据库之前，先要将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称事物
    db.session.commit()  # #提交会话到数据库