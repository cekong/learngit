#CBV视图
from flask import Flask,url_for,views
#-----------------------------------------------------
app=Flask(__name__)               #装饰器

def auth(func):
    print('我在上面')
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner
#--------------------------------------------------------
class IndexView(views.MethodView):  #CBV视图
    methods=['GET']               #视图类的方法  #允许的http请求方法（改CBV只允许GET方法）
    decorators = [auth,]          #给类添加装饰器  #每次请求过来都加auth装饰器

    def get(self):
        return 'Index.GET'
    def post(self):
        return 'Index.POST'

app.add_url_rule('/index/',view_func=IndexView.as_view(name='name1')) #(name='name1'反向生成url别名


if __name__ == '__main__':
    app.run(debug=True)


'''
在flask框架中使用视图函数或者类的方式

FBV不用多提及，更多的时候用的是FBV

CBV用到了类装饰器，原理和FBV大致相同

简单的业务逻辑使用FBV会更简单

如果写接口CBV更合适，get或者post方法可以直接定义到不同的方法流，省略if，else判断
'''
