''''''
'''
给Flask视图加装饰器
注意:如果要给视图函数加装饰器，一点要加在路由装饰器下面，才会被路由装饰器装饰


'''

from flask import Flask

'''首先定义1个装饰器'''
def auth(func):
    print('我在上面')
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


app=Flask(__name__)

@app.route('/',methods=['GET'])
@auth #注意如果要给视图函数加装饰器，一点要加在路由装饰器下面，才会被路由装饰器装饰
def first_flask():
    print('该我啦')
    return 'Hello World'

if __name__ == '__main__':
    app.run()