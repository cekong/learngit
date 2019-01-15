''''''
'''
https://coding.imooc.com/learn/list/194.html  第二章
https://git.imooc.com/coding-194/coding-194
'''
from flask import Flask,make_response



app=Flask(__name__)
app.config.from_object('my_flask_test_1_config')#导入配置文件

@app.route("/hello/") #将url 规则和试图函数绑定
def hello():
    #基于类的视图（即插视图）
    # content-type=text/html （默认）网页格式
    # content-type=application/json json格式
    headers={
        'content-type':'text/plain',#文本格式
        'location':'http://baidu.com'#301表示重定向，转到百度网页
    }
    '''重定向'''
    # response=make_response('hello,你好',301)
    response = make_response('hello,你好', 200)
    response.headers=headers
    return response

    # return 'hello,你好',200,headers

# app.add_url_rule('/hello/',view_func=hello)#将url 规则和试图函数绑定




if __name__ == '__main__':
    # app.run(debug=True) #debug=True开启调试模式
    app.run(debug=app.config['DEBUG']) #导入配置文件中的值
    # app.run(host='0.0.0.0', port=5001)#host='0.0.0.0'指定IP,使外网也可以访问
    # app.run()


''' 
路由注册方式：
1.@app.route("/hello/")
2.app.add_url_rule('/hello/',view_func=hello)
'''
'''
如果需要设置响应头就需要借助make_response()方法
response = make_response(render_template('index.html'))

response是flask.wrappers.Response类型

response.delete_cookie('key')

response.set_cookie('key', 'value')

response.headers['X-Something'] = 'A value'

return response

'''