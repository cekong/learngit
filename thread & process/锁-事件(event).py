''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9
python线程的事件用于主线程控制其它线程的执行，事件主要提供了三个方法：
event.wait  线程阻塞
event.set   将全局对象“Flag”设置为False
event.clear 将全局对象"Flag"设置为True
事件处理的机制：全局定义了一个“Flag”，默认为“False”，
如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，
如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
'''

#!/usr/bin/env python
#coding:utf8

import threading
def show(event):
    print('start')
    event.wait()  #阻塞线程执行程序
    print('done')
event_obj = threading.Event()  #创建event事件对象
for i in range(10):
    t1 = threading.Thread(target=show,args=(event_obj,))
    t1.start()
    inside = input('>>>:')
    if inside == '1':
        event_obj.set() #当用户输入1时，set全局Flag为True,线程不再阻塞，打印"done"
    event_obj.clear() #将Flag设置为False