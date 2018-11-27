''''''
'''服务端'''
import socket

#创建实例
sk=socket.socket()

#定义绑定ip和port
ip_port=("127.0.0.1",9999)

#绑定监听
sk.bind(ip_port)

#最大连接数
sk.listen(5)

#不断循环，不断接收数据
while True:
    #提示信息
    print("正在等待接收数据......")
    #等待连接数据
    conn,address=sk.accept()
    #一直使用当前连接进行数据接收
    #直到结束标志出现
    while True:
        #打开文件等待数据写入
        with open("file","ab") as f:#以二进制格式打开一个文件用于追加。
            #接收数据
            data=conn.recv(1024)
            #接收到退出指令
            if data==b'quit':
                break
            #写入 文件
            f.write(data)
        #接收成功的标志
        conn.send('success'.encode())
    #文件全部接收完成
    print("文件接收完成")
#关闭连接
sk.close()