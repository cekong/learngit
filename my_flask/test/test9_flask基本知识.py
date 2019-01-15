from flask import Flask, views, url_for,request
from werkzeug.routing import BaseConverter

app = Flask(import_name=__name__)


#给Flask视图加装饰器
#1、定义1个装饰器

def auth(func):
    print('我在上面')
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


app=Flask(__name__)

@app.route('/',methods=['GET'])
@auth #注意如果要给视图函数加装饰器，一点要加在路由装饰器下面，才会被路由装饰器装饰
def first_flask():
    print('ffff')
    print(request.url)  #获取访问url地址
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)

'''
return "字符串" ：响应字符串

return render_template('html模板路径',**{})：响应模板

return redirect('/index.html')：跳转页面
'''


'''
request.method： 获取请求方法

request.json

request.json.get("json_key")：获取json数据 **较常用      

request.argsget('name') ：获取get请求参数   

request.models.get('name') ：获取POST请求参数

request.models.getlist('name_list')：获取POST请求参数列表（多个）

request.values.get('age') ：获取GET和POST请求携带的所有参数（GET/POST通用）

request.cookies.get('name')：获取cookies信息

request.headers.get('Host')：获取请求头相关信息

request.path：获取用户访问的url地址，例如（/，/login/，/ index/）；

request.full_path：获取用户访问的完整url地址+参数 例如(/login/?age=18)

request.script_root： 抱歉，暂未理解其含义；

request.url：获取访问url地址，例如http://127.0.0.1:5000/?age=18；

request.base_url：获取访问url地址，例如 http://127.0.0.1:5000/；

request.url_root

request.host_url

request.host：获取主机地址
'''