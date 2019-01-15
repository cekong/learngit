''''''
'''
测试代码
https://coding.imooc.com/lesson/194.html#mid=12617
 
应用上下文 对象 Flask APPContext
请求上下文 对象 Request RequestContext

'''
from flask import Flask,current_app,request


app=Flask(__name__)


ctx=app.app_context()
ctx.push()
a=current_app
d=a.config['DEBUG']
print(d)
ctx.pop()

'''简化上述语句'''
# with app.app_context():
#     a=current_app
#     d=a.config['DEBUG']



'''
可以对实现了上下文协议的对象使用with语句
其中类中需要定义上下文管理器__enter__ __exit__ ，才可以使用with语句


例如：对于数据库
连接数据库，释放数据库
例如：对于文件
打开文件，关闭文件

'''

class A:
    def __enter__(self):
        print('connect')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('proces exception')
        else:
            print('no exception')
        print('close')
        return False

    def query(self):
        print('query data')

with A() as obj_A:

    obj_A.query()


'''
可以对实现了上下文协议的对象使用with语句
其中类中需要定义上下文管理器__enter__ __exit__ ，才可以使用with语句

也可以使用@contextmanager，此时不用定义__enter__ __exit__，也可以使用with语句
'''
from contextlib import contextmanager

@contextmanager
def query():
    yield  #必须添加
    print('query a data')

with query():
    pass

class B:
    @contextmanager
    def query(self):
        yield  #必须添加
        print('query b data')
obj_B=B()
with obj_B.query():
    pass


'''
contextmanager
https://coding.imooc.com/lesson/194.html#mid=12682
'''

from contextlib import contextmanager

@contextmanager
def book_mark():
    print('《',end='')
    yield
    print('》',end='')
with book_mark():
    print('红楼梦',end='')