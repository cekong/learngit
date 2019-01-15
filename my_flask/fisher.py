''''''
'''
https://coding.imooc.com/learn/list/194.html  第三章
https://git.imooc.com/coding-194/coding-194
书籍搜索和查询

原则：保证视图函数中代码简洁
'''
from app import create_app

app=create_app()

if __name__ == '__main__':
    # app.run(debug=True) #debug=True开启调试模式
    app.run(debug=app.config['DEBUG'],threaded=True)
    # app.run(host='0.0.0.0', port=5001,debug=app.config['DEBUG'],threaded=True,processes=1)
    '''threaded=True开启多线程    processes=1开启多进程'''
