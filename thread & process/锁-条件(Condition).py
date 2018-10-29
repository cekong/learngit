''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label9
使得线程等待，只有满足某条件时，才释放N个线程
'''
import threading
def condition_func():
    ret = False
    inp = input('>>>:')
    if inp == '1':
        ret = True
    return ret

def run(n):
    con.acquire() #条件锁
    con.wait_for(condition_func) #判断条件
    print('running...',n)
    con.release() #释放锁
    print('------------')

if __name__ == '__main__':
    con = threading.Condition() #建立线程条件对象
    for i in range(10):
        t = threading.Thread(target=run,args=(i,))
        print('start')
        t.start()
        t.join()
    print('退出程序')