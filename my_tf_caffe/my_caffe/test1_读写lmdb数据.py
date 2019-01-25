''''''
'''
https://www.imooc.com/learn/1040
'''


import lmdb
import numpy as np
import cv2
import caffe
from caffe.proto import caffe_pb2


def write():
    lmdb_file='lmdb_data'
    batch_size=256
    #打开环境
    # map_size定义最大储存容量，单位是kb
    lmdb_env=lmdb.open(lmdb_file,map_size=int(1e12))
    #建立失误
    lmdb_txt=lmdb_env.begin(write=True)

    for x in range(batch_size):
        data=np.ones((3,64,64),np.uint8)
        label=x
        datum=caffe.io.array_to_datum(data,label)
        keystr="{:0>8d}".format(x)
        lmdb_txt.put(keystr.encode('ascii'),datum.SerializeToString())#进行插入和修改
    #提交更改
    lmdb_txt.commit()

def read():
    lmdb_env=lmdb.open('lmdb_data')
    lmdb_txt=lmdb_env.begin()

    datum=caffe_pb2.Datum()
    for key,value in lmdb_txt.cursor():
        datum.ParseFromString(value)
        label=datum.label
        data=caffe.io.datum_to_array(datum)
        print(label)
        print(data)

if __name__=='__main__':
    write()
    read()