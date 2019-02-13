''''''
'''
https://www.imooc.com/video/15003
'''
import pandas as pd
import numpy as np
import datetime
from pylab import *

'''数据结构series & DataFrame'''
def main():
    s=pd.Series([i*2 for i in range(1,11)])
    print(s)
    print(type(s))

    df = pd.DataFrame(np.random.randn(8, 6), index=pd.date_range('01/01/2018', periods=8), columns=list('ABCDEF'))
    print("df:\n",df)
    print("df['A']['2018-01-01']:\n",df['A']['2018-01-01'])
    print("df[:3]:\n",df[:3])
    print("df['20180101':'20180104']:\n",df["20180101":"20180104"])
    print("df.loc[20180101:20180104,[B,D]]:\n",df.loc["20180101":"20180104",["B","D"]])
    print("df.iloc[1:3,2:4]:\n",df.iloc[1:3,2:4])
    print("df[df.A>0][df.B<0]:\n",df[df.A>0][df.B<0])


    df=pd.DataFrame({"A":1,"B":pd.Timestamp("20190104"),"C":pd.Series(1,index=list(range(4))),
    "D":np.array([3]*4,dtype="float32"),"E":pd.Categorical(["police","student","teacher","doctor"])})
    print("df:\n",df)

'''基本操作'''
def main1():
    df = pd.DataFrame(np.random.randn(8, 6), index=pd.date_range('01/01/2019', periods=8), columns=list('ABCDEF'))
    print("head3:\n",df.head(3))
    print("tail:\n", df.tail(3))
    print("index:\n", df.index)
    print("values:\n", df.values)
    print("T:\n", df.T)
    print("sort:\n",df.sort_values("C"))
    print("sort:\n", df.sort_index(axis=1,ascending=False)) #ascending 降序
    print(df.describe())

    '''set'''
    s=pd.Series(list(range(10,18)),index=pd.date_range("20190101",periods=8))
    df["F"]=s
    df.at["20190101","A"]=0
    df.iat[1,1]=1
    df.loc[:,"D"]=np.array([4]*len(df))
    print(df)
    df2=df.copy()
    df2[df2>0]=-df2
    print(df2)

'''缺失值处理'''
def main2():
    dates=pd.date_range('01/01/2019', periods=8)
    df = pd.DataFrame(np.random.randn(8, 6), index=dates, columns=list('ABCDEF'))
    df1=df.reindex(index=dates[:4],columns=list("ABCD")+["G"])
    print(df1)
    df1.loc[dates[0]:dates[1],"G"]=1
    print(df1)
    print(df1.dropna())
    print(df1.fillna(value=3))

"""pandas表统计与整合"""
def main3():
    dates = pd.date_range('01/01/2019', periods=8)
    df = pd.DataFrame(np.random.randn(8, 6), index=dates, columns=list('ABCDEF'))
    print(df)
    print("mean:\n",df.mean())
    print("var:\n",df.var()) #方差
    s=pd.Series([1,2,4,np.nan,5,7,8,10],index=dates)
    print("s:\n", s)
    print("s.shift(2):\n", s.shift(2)) #移动2个数
    print("s.diff():\n", s.diff()) #相邻两数的差值
    print("s.value_counts():\n",s.value_counts()) #统计数字出现的个数
    print(df.apply(np.cumsum)) #累加
    print(df.apply(lambda x:x.max()-x.min()))

    pieces=[df[:3],df[-2:]]
    print(pd.concat(pieces))

    left=pd.DataFrame({"key":["x","y"],"value":[1,2]})
    right=pd.DataFrame({"key":["x","z"],"value":[3,4]})
    print("left:\n",left)
    print("right:\n",right)
    print(pd.merge(left,right,on="key",how="outer"))

    df1=pd.DataFrame({"A":["a","b","c","b"],"B":list(range(4))})
    print(df1)
    print(df1.groupby("A").sum())


    #透视表
    df2=pd.DataFrame({'A':['one','one','two','three']*6,
    'B':['a','b','c']*8,
    'C':['foo','foo','foo','bar','bar','bar']*4,
    'D':np.random.randn(24),
    'E':np.random.randn(24),
    'F':[datetime.datetime(2019,i,1) for i in range(1,13)]+
                      [datetime.datetime(2019,i,15) for i in range(1,13)]})
    print('-----------------')
    print(df2)
    print(pd.pivot_table(df2,values="D",index=["A","B"],columns=["C"]))

'''时间序列、绘图'''
def main4():
    t=pd.date_range("20190101",periods=10,freq="S")
    print(t)

    ts=pd.Series(np.random.randn(100),index=pd.date_range("20190101",periods=100))
    ts=ts.cumsum()

    '''文件'''
    ts.to_csv("test.csv")
    ts.to_excel("test.xlsx")
    ts_csv=pd.read_csv("test.csv")
    ts_csv.plot()
    show()


if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    # main3()
    main4()

