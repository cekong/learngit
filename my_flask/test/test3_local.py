''''''
'''
多线程 要唯一标识,线程隔离
使用字典
request={thread_key1:Request1,thread_key2:Request2,...}
flask中使用werkzeug库中的local实现线程隔离
local使用字典的方式实现线程隔离
localstack封装了local，实现了线程隔离的栈结构
'''

import threading
import time
from werkzeug.local import Local


'''使用local，新线程不影响主线程，实现了线程隔离'''
class A:
    b=1

my_obj=Local()
my_obj.b=1

def worker():
    my_obj.b=2
    print('worker:',my_obj.b)


new_t=threading.Thread(target=worker)
new_t.start()
time.sleep(1)

print('主线程:',my_obj.b)#主线程


'''新线程影响了主线程'''

# class A:
#     b=1
# my_obj=A()
#
# def worker():
#     my_obj.b=2
#     print('worker:',my_obj.b)
#
# new_t=threading.Thread(target=worker)
# new_t.start()
# time.sleep(1)
#
# print('主线程:',my_obj.b)#主线程