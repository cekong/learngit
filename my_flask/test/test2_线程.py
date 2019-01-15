''''''
'''
线程
https://coding.imooc.com/lesson/194.html#mid=12625
进程：分配资源
线程：利用cpu执行代码

异步编程
更加充分的利用CPU的性能优势

锁
细粒度锁：程序员主动加的锁
粗粒度锁：python解释器上的锁 GIL
由于GIL，多核cpu只执行一个线程


多线程
https://coding.imooc.com/lesson/194.html#mid=12628
IO密集型的程序：例如，查询数据库、请求网络资源、读写文件
cpu密集型程序：例如，圆周率的计算、视频的解码

IO密集型程序主要过程为等待结果
所以Python多线程常使用在在IO密集型程序

flask多线程
https://coding.imooc.com/lesson/194.html#mid=12629
使用webserver开启flask多线程
'''


import threading
import time

def worker():
    print('子线程')
    t=threading.current_thread()
    time.sleep(8)
    print(t.getName())



new_t=threading.Thread(target=worker)
new_t.start()


print('主线程')
t=threading.current_thread()
print(t.getName())#主线程