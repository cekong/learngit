""""""
"""
Python数据分析-基础技术篇:                
 https://www.imooc.com/learn/843 
https://blog.csdn.net/sinat_17697111/article/details/81534935
"""


import numpy as np
from scipy.integrate import quad,dblquad,nquad   #积分
from scipy.optimize import minimize,root    #优化函数
from pylab import *
from scipy.interpolate import interp1d  #插值
from scipy import linalg as lg   #线性
'''积分integrate'''
def main():
    print(quad(lambda x:np.exp(-x),0,np.inf))
    print(dblquad(lambda t,x:np.exp(-x*t)/t**3,0,np.inf,lambda x:1,lambda x:np.inf))
    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print(nquad(f,[bound_x,bound_y]))


'''最优化函数库optimize--minimize/root'''
def main1():
    def rosen(args):
        a=args
        v=lambda x:a/x[0] +x[0]
        return v
    def con(args):
        xmin,xmax=args
        # eq表示 函数结果等于0 ； ineq 表示 表达式大于等于0
        cons = ({'type': 'ineq', 'fun': lambda x: x[0] - xmin},
                {'type': 'ineq', 'fun': lambda x: -x[0] + xmax})
        return cons
    x0=np.asarray((2))
    args=(1)
    args1=(0.1,2.0)#xmin, xmax
    cons=con(args1)
    res=minimize(rosen(args),x0,method='SLSQP',
                 options={"disp":True},
                 constraints=cons)
    print("rose mini:",res)

    def fun(x):
        return x**2+x*2+1
    sol=root(fun,0.1)
    print("root:",sol.x,sol.fun)


'''插值'''
def main2():
    x=np.linspace(0,1,10)
    y=np.sin(2*np.pi*x)
    li=interp1d(x,y,kind="cubic")
    x_new=np.linspace(0,1,50)
    y_new=li(x_new)
    figure()
    plot(x,y,"r")
    plot(x_new,y_new,"k")
    show()
    print(y_new)
'''线性计算'''
def main3():
    arr=np.array([[1,2],[3,4]])
    print("det:",lg.det(arr))
    print("inv:",lg.inv(arr))
    print("eig:", lg.eig(arr))
    print("lu:",lg.lu(arr))
    print("qr:", lg.qr(arr))
    print("svd:", lg.svd(arr))
    print("schur:", lg.schur(arr))
    b=np.array([6,14])
    print("solve:",lg.solve(arr,b))

if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    main3()

