''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9
Lock锁是同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据，
如一个场所内只有3把椅子给人坐，那么只允许3个人，其它人则排队，
只有等里面的人出来后才能进去。
'''
import threading,time
class mythreading(threading.Thread): #写一个类方法继承hreading模块
    def run(self):  #运行线程的函数，函数名必须是run名称
        semaphore.acquire()  #获取信号量锁
        print('running the thread:',self.getName())
        print(1)
        time.sleep(2)
        semaphore.release()  #释放信号量锁

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(3) #创建信号量对象，只运行3个进程同时运行
    for i in range(20):
        t1 = mythreading()
        t1.start()
    t1.join()        #阻断线程等待执行完后再执行后续代码
    print('---end')