""""""
"""
Python数据分析-基础技术篇:
 https://www.imooc.com/learn/843
"""
import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
def main():
    lst=[[1,2],[2,3]]
    print(type(lst))
    nplst=np.array(lst)
    print(type(nplst))
    nplst1=np.array(lst,dtype=np.float)
    print(nplst1.shape)
    print(nplst1.ndim)
    print(nplst1.dtype)
    print(nplst1.itemsize)
    print(nplst1.size)
    a=np.arange(1,11).reshape([2,-1])
    print(a)

    a=np.array([
        [[1,2,3,4],
         [5,6,7,8]],
        [[1, 2, 3, 4],
         [5, 6, 7, 8]],
        [[1, 2, 3, 4],
         [5, 6, 7, 8]],
    ])
    print(a.sum(axis=0))
    print(a.sum(axis=1))
    print(a.sum(axis=2))
    print(a.sum())
    print(a.max())
    print(np.matmul(a,a))
    print(np.split(a,3))
    print(np.poly1d([2,1,3]))
    a=np.array([[1,2],[3,4]])
    print(inv(a))
    print(det(a))
    print(eig(a))
    print(a.transpose())
    b=np.array([[5],[7]])
    print(solve(a,b))


def main1():
    x=np.linspace(-np.pi,np.pi,256,endpoint=True)
    c,s=np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="cos")
    plt.plot(x, s,"r*",label="sin")
    plt.title("sin & cos")
    ax=plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_position(("data",0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
               [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="green",edgecolor="None",alpha=0.2))
    plt.legend(loc="upper left")
    plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color="yellow",alpha=0.25)
    t=1
    plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")
    plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",
                 xytext=(+10,+30),textcoords="offset points",
                 arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2")
                 )
    plt.grid()
    # plt.axis([-1,1,-0.5,1])
    plt.show()

def main2():
    """散点图"""
    fig=plt.figure()
    sfig=fig.add_subplot(3,3,1)
    n=128
    x=np.random.normal(0,1,n)
    y=np.random.normal(0,1,n)
    t=np.arctan2(y,x)
    # plt.axes([0.025,0.025,0.95,0.95])  #axes是创建坐标轴
    sfig.scatter(x,y,s=75,c=t,alpha=0.5)
    plt.xlim(-1.5,1.5),plt.xticks([])
    plt.ylim(-1.5,1.5),plt.yticks([])
    plt.axis() #axis是设定xy范围
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()
    """柱状图"""
    sfig=fig.add_subplot(3,3,2)
    n=10
    x=np.arange(n)
    y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
    y2=(1-x/float(n))*np.random.uniform(0.5,1.0,n)

    sfig.bar(x,+y1,facecolor="#9999ff",edgecolor="white")
    sfig.bar(x,-y1,facecolor="#ff9999",edgecolor="white")
    for a,b in zip(x,y1):
        plt.text(a+0.4,b+0.05,'%.2f' %b,ha='center',va='bottom')
    for a,b in zip(x,y2):
        plt.text(a+0.4,-b-0.05,'%.2f' %b,ha='center',va='top')

    # plt.show()

    """饼状图"""
    sfig=fig.add_subplot(3,3,3)
    n=20
    z=np.ones(n)
    print(z)
    z[-1]=2
    print(z)
    plt.pie(z,explode=z*0.05,colors=['%f' %(i/float(n)) for i in range(n)],
            labels=['%.2f' %(i/float(n)) for i in range(n)])
    plt.gca().set_aspect("equal")
    plt.xticks([]),plt.yticks([])
    # plt.show()

    """极坐标图"""
    sfig=fig.add_subplot(3,3,4,polar=True)
    n=20
    theta=np.arange(0.0,2*np.pi,2*np.pi/n)
    radii=10*np.random.rand(n)
    plt.polar(theta,radii)
    # plt.plot(theta,radii)
    # plt.show()
    """热图"""
    sfig=fig.add_subplot(3,3,5)

    data=np.random.rand(3,3)
    cmap=cm.Blues
    map=plt.imshow(data,interpolation="nearest",cmap=cmap,
                   aspect="auto",vmin=0,vmax=1)
    """3D图"""
    sfig=fig.add_subplot(3,3,6,projection="3d")
    sfig.scatter(1.1,3,s=100)
    """热力图"""
    sfig=fig.add_subplot(3,1,3)
    def f(x,y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    n=256
    x=np.linspace(-3,3,n)
    y=np.linspace(-3,3,n)
    x,y=np.meshgrid(x,y)
    plt.contour(x,y,f(x,y),8,alpha=0.75,cmap=plt.cm.hot)
    plt.savefig("fig.jpg")
    plt.show()
    










if __name__ == '__main__':
    # main()
    # main1()
    main2()