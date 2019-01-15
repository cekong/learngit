#FBV视图
from flask import Flask,url_for,views
#-----------------------------------------------------
app=Flask(__name__)               #装饰器



'''方式一'''
# @app.route('/index/',endpoint='xx') #endpoint=路由别名
# def index():
#     url_for('xx')
#     return "Index"

'''方式二'''
def index():
    url_for('xx')
    return "Index"

app.add_url_rule('/index/',endpoint='xx',view_func=index)

if __name__ == '__main__':
    app.run(debug=True)

