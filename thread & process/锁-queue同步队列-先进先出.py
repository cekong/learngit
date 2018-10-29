''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9
在FIFO队列中，第一个添加的任务是第一个被检索的。
在LIFO队列中，最后添加的条目是第一个被检索（像堆栈一样操作）。
在优先级队列中，条目保持排序（使用heapq模块），并且首先检索最低值的条目。
'''

# Queue先进先出队列
import queue


def show(q, i):
    if q.empty() or q.qsize() >= 1:
        q.put(i)  # 存队列
    elif q.full():
        print('queue not size')


que = queue.Queue(5)  # 允许5个队列的队列对象
for i in range(5):
    show(que, i)
print('queue is number:', que.qsize())  # 队列元素个数
for j in range(5):
    print(que.get())  # 取队列
print('......end')

'''
class queue.Queue（maxsize = 0 ）
FIFO队列的构造器。 maxsize是一个整数，用于设置可放入队列的项目数的上限。
一旦达到此大小，插入将会阻塞，直到队列项被消耗。如果 maxsize小于或等于零，
队列大小是无限的。

Queue.qsize（）返回队列的大小
'''