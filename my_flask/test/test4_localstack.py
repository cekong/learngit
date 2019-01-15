''''''
'''
https://coding.imooc.com/lesson/194.html#mid=12634
https://coding.imooc.com/lesson/194.html#mid=12635

flask中使用werkzeug库中的local实现线程隔离
local使用字典的方式实现线程隔离
localstack封装了local，实现了线程隔离的栈结构

以线程ID号作为key的字典->Local->LocalStack

使用线程隔离的意义：
使当前线程能够正确引用到他自己所创建的对象，而不引用到其他线程所创建的对象

flask中request、sesion、g是线程隔离的对象


'''

import threading
import time
from werkzeug.local import LocalStack

'''---栈基本知识---'''
s=LocalStack()
s.push(1)#向栈顶推入1
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
# s.top#取出栈顶元素，不会删除栈顶元素
# s.pop()#取出栈顶元素，并删除栈顶元素
s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
'''----------------'''


'''使用LocalStack，实现线程隔离'''
mystack=LocalStack()
mystack.push(1)
print('主线程',mystack.top) #1

def worker():
    print('新线程push前',mystack.top) #None
    mystack.push(2)
    print('新线程push后', mystack.top) #2

new_t=threading.Thread(target=worker)
new_t.start()
time.sleep(1)

print('主线程:',mystack.top)#主线程  #1

'''主线程和新线程实现了线程隔离'''