# -*- coding: utf-8 -*-


from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name',__name__) #是否主程序
    print('parent process',os.getppid())  #上层进程号
    print('process id:',os.getpid())  #自身进程号

def f(name):
    info('function f')
    print('hello',name)
if __name__ == '__main__':
    info('main line')  #通过pycharm进程运行函数
    p = Process(target=f,args=('bob',))  #创建进程，调用子进程运行函数
    p.start()#启动进程
    p.join()#等待进程结束
    print('进程结束')
