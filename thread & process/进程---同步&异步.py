''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label12
pool.apply#创建同步进程
pool.apply_async#创建异步进程
'''

from multiprocessing import Pool,freeze_support
import time
def foo(n):
    time.sleep(1)
    print(n*n)

def back(arg):
    print('exec done:',arg)

if __name__ == '__main__':

    pool = Pool(5)   #创建进程池，同时2个进程运行
    for i in range(10):
        # pool.apply(func=foo, args=(i,))  #创建同步进程
        #创建异步进程，传递函数和参数，在函数执行完后执行callback，并将函数foo的结构返回给callback
        pool.apply_async(func=foo,args=(i,),callback=back)
    pool.close() #此处必须是先关闭进程再join，，关闭pool，使其不在接受新的任务。
    pool.join()
    print('end')