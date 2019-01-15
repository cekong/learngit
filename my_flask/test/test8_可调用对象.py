''''''
'''
可调用对象
https://coding.imooc.com/lesson/194.html#mid=13472


判断python对象是否可调用的三种方式及其区别
https://www.cnblogs.com/shenbuer/p/7969560.html

Python中把类的实例变成一个可调用对象(__call__)
https://blog.csdn.net/tcx1992/article/details/80523005

'''

class A():
    def __call__(self):
        print('A')
        return object()

class B():
    def run(self):
        print('B')
        return object()

def func():
    print('func')
    return object()


def main(callable):
    callable()
    pass


main(A())
B.run(0)
main(func)
func()
try:
    main(B())
except Exception as e:
    print(e)
