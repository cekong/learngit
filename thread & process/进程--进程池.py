''''''
'''
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label12
进程池（Pool）

'''




from multiprocessing import Pool
import time

def f(msg):
    print("msg:", msg)
    time.sleep(3)
    print("end")

if __name__ == '__main__':
    with Pool(processes=3) as pool: #设定进程的数量为3，，0、1、2会直接送到进程中执行，
                                    # 当其中一个执行完事后才空出一个进程处理对象3
        for i in range(4):
            msg = "hello %d" % (i)
            pool.apply_async(f, (msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

        print("~~~~~~~~~~~~~~~~~~~~~~")
        pool.close()
        pool.join()  # 调用join之前，先调用close函数，否则会出错。
                     # 执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
        print("Sub-process(es) done.")