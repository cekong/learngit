'''
继承式调用启动线程
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label1
'''
'''
继承式调用启动线程
https://www.cnblogs.com/zhangxinqi/p/8284687.html#_label1
'''
#!/usr/bin/env python
#coding:utf8

import threading,time

class mythreading(threading.Thread): #写一个类方法继承threading模块
    def __init__(self):
        #threading.Thread.__init__(self)   #金典类重写父类方法
        super(mythreading,self).__init__() #重写父类属性
        self.name = self.name.split('d')[1]


    def run(self):  #运行线程的函数，函数名必须是run名称
        super(mythreading,self).run()
        print('starting on threading',self.name)
        time.sleep(5)
if __name__ == '__main__':
    #t1 = mythreading(1)   #通过类创建线程
    #t2 = mythreading(2)
    #t1.start()   #启动进程
    #t2.start()
    ttr = []
    for i in range(10):     #启动十个线程
        t = mythreading()
        ttr.append(t)
        t.start()
        t.setName('hehe-{}'.format(i))   #修改线程名
        print(t.getName())   #获取线程名

    for item in ttr:
        item.join()    #阻断线程等待执行完后再执行后续代码

    print('-----end')