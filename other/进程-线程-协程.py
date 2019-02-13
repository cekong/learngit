''''''
'''进程'''
from multiprocessing import Process
def foo(i):
    print("this is a process",i)
for i in range(5):
    p=Process(target=foo,args=(i,))
    p.start()


'''线程'''
import threading
def show(i):
    print("this is a threading", i)
for i in range(5):
    t = threading.Thread(target=show, args=(i,))
    t.start()


'''协程'''
import gevent
def foo():
    print("start foo")
    gevent.sleep(2)
    print("end foo")
def bar():
    print("start bar")
    gevent.sleep(0)
    print("end bar")
# foo()
# bar()
gevent.joinall([gevent.spawn(foo),gevent.spawn(bar)])