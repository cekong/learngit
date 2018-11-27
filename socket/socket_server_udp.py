import socket

#创建实例 udp方式
sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#定义绑定ip和port
ip_port=("127.0.0.1",8888)

#绑定监听
sk.bind(ip_port)


#不断循环，不断接收数据
while True:
    print("等待接收数据...")
    #接收数据
    data = sk.recv(1024)
    # 打印数据
    print(data.decode())

