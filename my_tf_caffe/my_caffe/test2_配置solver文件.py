''''''
'''
https://www.imooc.com/learn/1040
https://blog.csdn.net/cham_3/article/details/72141753
'''


from caffe.proto import caffe_pb2

s=caffe_pb2.SolverParameter()
"""定义solver的参数"""

#定义训练网络和测试网络
s.train_net="train.prototxt"
s.test_net.append("test.prototxt")

s.test_interval=100
s.test_iter.append(10)
#最大迭代次数
s.max_iter=1000
#定义学习率
s.base_lr=0.1
# 定义衰减率
s.weight_decay=5e-4
#定义学习率更新方式
s.lr_policy="step"
#定义打印网络的间隔
s.display=10
#定义caffemodel存储的间隔
s.snapshot=10
#定义caffemodel存储的位置
s.snapshot_prefix="model"
#定义网络优化的方式
s.type="SGD"
#CPU
s.solver_mode=caffe_pb2.SolverParameter.CPU
#保存solver文件
with open("net/s.prototxt","w") as f:
    f.write(str(s))