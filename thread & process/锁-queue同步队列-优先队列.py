#PriorityQueue按数据大小取最小值优先
'''PriorityQueue按数据大小取最小值优先'''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9
在FIFO队列中，第一个添加的任务是第一个被检索的。
在LIFO队列中，最后添加的条目是第一个被检索（像堆栈一样操作）。
在优先级队列中，条目保持排序（使用heapq模块），并且首先检索最低值的条目。
'''


import queue

pque = queue.PriorityQueue()  #优先级的队列
pque.put(7)   #先存入队列
pque.put(5)
pque.put(3)
print('size=',pque.qsize())
print(pque.get())  #取出最小值的数据
print(pque.get())
print(pque.get())



'''
class queue.PriorityQueue（maxsize = 0 ）

优先队列的构造函数。 maxsize是一个整数，用于设置可放入队列的项目数的上限。
一旦达到此大小，插入将会阻塞，直到队列项被消耗。如果 maxsize小于或等于零，
队列大小是无限的。

'''

