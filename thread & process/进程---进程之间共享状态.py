''''''
'''
 进程之间共享状态
 (1)可以使用value或将数据存储在共享内存映射中Array
 multiprocessing.Value（typecode_or_type，* args，lock = True ）
 返回从共享内存分配的对象.
 如果锁是True（默认），则会创建一个新的递归锁对象来同步对该值的访问。
 如果锁是一个Lock或一个RLock对象，那么将用于同步访问值。
 如果锁是False那么访问返回的对象将不会被锁自动保护，因此它不一定是“过程安全的”。
 
 (2)Server process（服务器进程）
 通过Manager()控制一个服务器进程来返回管理器对象，该进程持有Python对象，
 并允许其他进程使用代理来操作它们。
 manager()将支持的类型： list，dict，Namespace，Lock， RLock，Semaphore，
 BoundedSemaphore， Condition，Event，Barrier， Queue，Value和Array。
 
'''


from multiprocessing import Process, Value, Array, Manager
def f_1(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = i*i
def f_2(d,l,i):
    d[i] = i+1  #每个进程添加字典元素
    l.append(i)  #每个进程启动后将列表添加数据i
    print('i=',i,'   d=',d,'   l=',l)

if __name__ == '__main__':

    '''(1)'''
    num = Value('d', 0.0)  #d表示一个双精度浮点数
    arr = Array('i', range(10)) #i表示符号整数
    p = Process(target=f_1, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])
    print('-------------------------------')
    '''(1)'''

    '''(2)'''
    manager = Manager()
    d = manager.dict()
    l = manager.list()
    pro_list = []
    for i in range(5):  # 启动5个进程
        p = Process(target=f_2, args=(d, l, i))
        p.start()
        pro_list.append(p)  # 将进程都添加到列表
    for j in pro_list:
        j.join()  # 等待每个进程执行完成
    print(d)  # 打印字典数据为5个进程操作的后的数据，实现进程间的数据共享
    print(l)
    '''(2)'''



