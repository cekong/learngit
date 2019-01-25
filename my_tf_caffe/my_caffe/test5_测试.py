import caffe
import numpy as np


deploy="/home/deepl/Documents/wb/my_tf_caffe/my_caffe/net/lenet_deploy.prototxt"  #测试网络的文件

model=""  #训练得到的model文件

net=caffe.Net(deploy,model,caffe.TEST)

net.blobs['data'].data[...]=np.ones((3,28,28),np.uint8)

net.forward()

prob=net.blobs["prob"].data[0]

print(prob)