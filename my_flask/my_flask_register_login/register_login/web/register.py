# -*- coding: UTF-8 -*-
''''''
'''用户注册'''

from flask import render_template, request
from my_flask_register_login.register_login.test_form import RegisterForm
from my_flask_register_login.register_login.models import save_to_mysql
from . import web



@web.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm(data={'gender': 1})  #默认值
        return render_template('register.html', form=form)
    else:
        myform = RegisterForm(formdata=request.form)
        if myform.validate():
            save_to_mysql(myform)
            print('用户提交数据通过格式验证，提交的值为：', myform.data)
        else:
            print(myform.errors)
        return render_template('register.html', form=myform)



