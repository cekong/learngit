# -*- coding: UTF-8 -*-
from flask import render_template, request,flash
from my_flask_register_login.register_login.test_form import LoginForm
from . import web
from my_flask_register_login.register_login.models import dbRegister_Form



@web.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()     #实例化 form验证类
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate(): #判断是否验证成功？
            user=dbRegister_Form.query.filter_by(name=form.name.data).first()
            if not user:
                flash('无效的用户名')
            elif user.check_password(form.pwd.data):
                flash('登录成功')
                print('用户提交数据通过格式验证，提交的值为：', form.data)
            else:
                flash('无效的密码')
        else:
            print(form.errors)
        return render_template('login.html', form=form)


