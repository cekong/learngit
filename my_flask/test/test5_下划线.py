''''''
'''
https://blog.csdn.net/tcx1992/article/details/80105645?models=timeline 
Python中下划线的5种含义
'''



class A(object):
    def __method(self):
        print("I'm a method in A")
    def method(self):
        self.__method()

a = A()
a.method()

class B(A):
    def __method(self):
        print("I'm a method in B")


b = B()
b.method()

b._B__method()