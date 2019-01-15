#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, Request, render_template

app = Flask(__name__, template_folder='templates')
app.debug = True


@app.before_first_request  #第1个请求到来执行
def before_first_request1():
    print('before_first_request1')


@app.before_request #中间件2
def before_request1():
    Request.nnn = 123
    print('before_request1')  #不能有返回值，一旦有返回值在当前返回


@app.before_request
def before_request2():
    print('before_request2')



@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404



@app.route('/')
def hello_world():
    return "Hello World"





@app.after_request #中间件 执行视图之后
def after_request1(response):
    print('after_request1:', response)
    return response


@app.after_request #中间件 执行视图之后 先执行 after_request2
def after_request2(response):
    print('after_request2:', response)
    return response

if __name__ == '__main__':
    app.run()