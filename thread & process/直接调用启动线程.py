#!/usr/bin/env python
#coding:utf8

'''
直接调用启动线程
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label1
'''
import threading  #线程模块
import time

def sayhi(num):  #定义每个线程要运行的函数
    print('running on number',num)
    time.sleep(3)

if __name__ == "__main__":
    t1 = threading.Thread(target=sayhi,args=(33,)) #生成一个线程实例
    t2 = threading.Thread(target=sayhi,args=(22,)) #生成另一个线程实例

    t1.start()  #启动线程
    t2.start()
    print(t1.getName()) #获取线程名
    print(t2.getName())
    t1.join()  #阻塞主线程，等待t1子线程执行完后再执行后面的代码
    t2.join()  #阻塞主线程，等待t2子线程执行完后再执行后面的代码
    print('-----end')

'''
直接调用启动线程
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label1
'''