''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9

threading.Lock() 加载线程的锁对象，是一个基本的锁对象，
一次只能一个锁定，其余锁请求，需等待锁释放后才能获取
threading.RLock() 多重锁，在同一线程中可用被多次acquire。
如果使用RLock，那么acquire和release必须成对出现， 调用了n次acquire锁请求，
则必须调用n次的release才能在线程中释放锁对象。

'''



from threading import Thread,Lock,RLock
import time

class mythread(Thread):
    def __init__(self,number1,number2):
        super(mythread,self).__init__()
        self.number1 = number1
        self.number2 = number2

    def run(self):
        print('开启线程',self.name)
        lock.acquire()
        print('run is:',time.time(),self.number1+self.number2)
        arithmetic(self.number1,self.number2)
        time.sleep(2)
        lock.release()

def arithmetic(avg1,avg2):
    lock.acquire()
    print('arithmetic:',time.time(),avg1+avg2)
    time.sleep(2)
    lock.release()

#创建锁对象时如果使用Lock则会在运行线程2时一直处于等待状态
#如果使用RLock则可正常运行，RLock支持多重锁
lock = RLock()  #创建多重锁

if __name__ == "__main__":
    t1 = mythread(3,4)
    t2 = mythread(5,6)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('程序结束！')
