#!/usr/bin/env python
#coding:utf8

import time
import threading

def run(num):  #子线程运行函数
    print('---starting',num)
    time.sleep(2)
    print('---done',threading.current_thread().name)
def main():  #主线程运行函数
    print('开启主线程')
    for i in range(4): #在主线程中运行4个子线程
        t1 = threading.Thread(target=run,args=(i,))
        t1.start()
        print('启动线程',t1.getName())
    t1.join()
    print('结束主线程')
m = threading.Thread(target=main,args=())
m.setDaemon(True) #设置主线程为守护线程
m.start()
m.join(timeout=3) #等待3秒后主线程退出，不管子线程是否运行完
print('------end')

'''
通过Thread.setDaemon(false)设置为用户线程；
通过Thread.setDaemon(true)设置为守护线程。
如果不设置次属性，默认为用户线程。

主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),
这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，
就不管子线程B是否完成,一并和主线程A退出.这就是setDaemon方法的含义，
这基本和join是相反的。此外，还有个要特别注意的：
必须在start() 方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。

'''
