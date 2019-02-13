
def foo(*args,**kwagrs):
    print('args=',args)
    print('kwargs=',kwagrs)
    print('------------------')

if __name__=='__main__':#用来做输出的
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4,a=1,b=2,c=3)
    foo('a',1,None,a=1,b='2',c=3)#*kwargs用来接收关键字传参其余类型都由*args接收


    