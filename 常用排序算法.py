''''''
'''
https://coding.imooc.com/learn/list/182.html
第5章 基于python常问排序算法 
'''
'''----------------排序----------------'''
a=[0,10,99,55,16,23,66]

'''#从小到大'''
print(sorted(a))

a.sort()
print(a)


'''#从大到小'''
print(sorted(a,reverse=True))

a.sort(reverse=True)
print(a)

print('------------冒泡排序------------')
'''----------------冒泡排序----------------'''
def bubble_sort(lists):
    #获取数组长度
    count=len(lists)-1
    #n个元素遍历n次
    for index in range(count,0,-1):
        #第i个和第i+1个对比
        for sub_index in range(index):
            #大的元素冒上去
            if lists[sub_index]>lists[sub_index+1]:
                lists[sub_index],lists[sub_index+1]=lists[sub_index+1],lists[sub_index]
    return lists
alist=[0,10,99,55,16,23,66]
print(bubble_sort(alist))

print('------------快速排序------------')
'''----------------快速排序----------------'''
'''挑一个元素作为基准key，所有小于key的元素放左边，
所有大于key的元素放右边，分别递归调用左侧列表和右侧列表'''
def quick_sort(lists,left,right):
    #递归过程中，发现left和right一致时，停止递归，直接返回列表
    if left>=right:
        return lists
    #定义游标
    low=left
    high=right
    #取参考标志，最左边的元素
    key=lists[low]
    while low<high:
        #从最右侧向左，依次和标志元素对比，如果右侧的元素大于标志元素
        while low<high and lists[high]>=key:
            #右侧减1
            high-=1
        #否则low赋high值
        lists[low]=lists[high]

        # 从最左侧向右，依次和标志元素对比，如果左侧的元素小于标志元素
        while low<high and lists[low]<=key:
            #左侧加1
            low+=1
        #否则low赋high值
        lists[high]=lists[low]

    #最后给high位置赋值
    lists[high]=key

    #处理左侧元素
    quick_sort(lists,left,low-1)
    #处理右侧元素
    quick_sort(lists, low+1, right)
    return lists

alist=[0,10,99,55,16,23,66]
print(quick_sort(alist,0,6))

print('------------堆排序------------')
'''----------------堆排序----------------'''
def heap_sort(lists):
    def sift_down(start,end):
        '''最大堆调整'''
        root=start
        print("root %d start %d end %d"%(root,start,end))
        while True:
            # 从root开始对最大堆调整
            child=2*root+1
            print("child index:",child)

            #终止条件，子索引值超过数组最大长度
            if child>end:
                break

            #确定最大的子节点的索引值
            if child+1 <=end and lists[child]<lists[child+1]:#如果左边小于右边
                child+=1#设置右边为大

            #子节点最大值和根节点交换
            if lists[root]<lists[child]:
                lists[root],lists[child]=lists[child],lists[root]
                root=child
            else:
                break
    print("------------创建最大堆------------")
    #创建最大堆
    for start in range((len(lists)-2)//2,-1,-1):
        print("--->loop start",start)
        sift_down(start,len(lists)-1)
        print(lists)

    print("------------排序过程------------")
    #堆排序
    for end in range(len(lists)-1,0,-1):
        #首尾交换
        lists[0],lists[end]=lists[end],lists[0]
        #剩余重新堆排序
        sift_down(0,end-1)
        print(lists)
    return lists
alist=[10,99,5,55,16,23,66]
print(heap_sort(alist))

print('------------二分查找------------')
'''----------------二分查找----------------'''
'''(查找某一个数)'''
def binary_search(arr,start,end,hkey):
    if start>end:
        return -1
    mid=start+(end-start)//2
    if arr[mid]>hkey:
        return binary_search(arr,start,mid-1,hkey)
    if arr[mid]<hkey:
        return binary_search(arr,mid+1,end,hkey)
    return mid
alist=[10,99,5,55,16,23,66]
alist=sorted(alist)
print(alist)
print('位置在：',binary_search(alist,0,6,66))

print('------------素数------------')
'''----------------素数----------------'''
'''0和1不是素数，除了1和自身外，不能被其他自然数整除的数'''

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
for i in range(0,100):
    if is_prime(i):
        print(i)




