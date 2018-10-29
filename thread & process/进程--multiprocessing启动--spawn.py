''''''
'''
multiprocessing支持三种启动流程的方式：

spawn：
父进程启动一个新鲜的Python解释器进程。
子进程只会继承运行进程对象run()方法所必需的资源。
特别是父进程中不必要的文件描述符和句柄将不会被继承。
与使用fork或forkserver相比，使用此方法启动进程相当慢。

fork：
父进程使用os.fork()fork来解释Python。子进程在开始时与父进程有效地相同。
父进程的所有资源都由子进程继承。请注意，安全分叉多线程的过程是有问题的。

forkserver：
当程序启动并选择forkserver启动方法时，启动一个服务器进程。从那时起，
无论何时需要一个新的进程，父进程都连接到服务器并请求它分叉一个新的进程。
fork服务器进程是单线程的，所以它是安全的使用os.fork()。
没有不必要的资源被继承。

请注意，与一个上下文相关的对象可能与另一个上下文的进程不兼容。
特别是，使用fork上下文创建的锁不能被传递给使用spawn或forkserver启动方法启动的进程 。

想要使用特定启动方法的库应该可以get_context()用来避免干扰库用户的选择。
'''

import multiprocessing as mp
import time

def foo(q):
    for i in range(10):
        q.put('python%s'%i)
        time.sleep(1)
    #q.put('context')
if __name__ == '__main__':
    '''两种写法'''
    '''set_start_method()不能在程序中使用多次'''

    mp.set_start_method('spawn')  # 设置启动进程方式
    q = mp.Queue()  # 创建队列对象
    p = mp.Process(target=foo, args=(q,))  # 启动一个进程，传递运行函数和参数
    p2 = mp.Process(target=foo, args=(q,))

    '''get_context()获取上下文对象'''
    # ext = mp.get_context('spawn')
    # q = ext.Queue()
    # p = ext.Process(target=foo,args=(q,))
    # p2 = ext.Process(target=foo,args=(q,))

    ''' ------------------------- '''

    p.start()
    p2.start()
    for i in range(10):
        print(q.get())
    p.join()
    p2.join()