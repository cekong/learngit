''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label12

multiprocessing 支持两种进程之间的通讯通道：
 Queue（队列）
 
 Pipes（管道）
'''


from multiprocessing import Process,Pipe,Queue

def Pipe_f(parent,child):
    parent.send('parent.send1') #父链接写入数据
    parent.send('parent.send2')
    child.send('child.send1')  #子链接写入数据
    child.send('child.send2')
    parent.close()  #关闭管道
    child.close()

def Queue_f(q):
    q.put([42, None, 'hello'])
    q.put('python')
    q.put('python3')


if __name__ == '__main__':
    parent_conn, child_conn = Pipe() #创建父和子管道连接
    p = Process(target=Pipe_f, args=(parent_conn,child_conn))
    p.start()
    print(parent_conn.recv())   #从父链接收的数据是从子链接写入的数据
    print(parent_conn.recv())
    print(child_conn.recv())    #从子链接收的数据是从父链接写入的数据
    print(child_conn.recv())
    p.join()

    q = Queue()  # 创建队列对象
    p = Process(target=Queue_f, args=(q,))  # 新进程
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    print(q.get())
    print(q.get())
    p.join()

