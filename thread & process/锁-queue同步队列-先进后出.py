#LifoQueue先进后出队列
''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9
在FIFO队列中，第一个添加的任务是第一个被检索的。
在LIFO队列中，最后添加的条目是第一个被检索（像堆栈一样操作）。
在优先级队列中，条目保持排序（使用heapq模块），并且首先检索最低值的条目。
'''
import queue

lifoque = queue.LifoQueue()
lifoque.put('hello1')
lifoque.put('hello2')
lifoque.put('hello3')
print(lifoque.qsize())
print(lifoque.get())
print(lifoque.get())
print(lifoque.get())

'''
class queue.LifoQueue（maxsize = 0 ）

LIFO队列的构造器。 maxsize是一个整数，用于设置可放入队列的项目数的上限。
一旦达到此大小，插入将会阻塞，直到队列项被消耗。如果 maxsize小于或等于零，
队列大小是无限的。

'''