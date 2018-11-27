import socket

#创建实例
client=socket.socket()

#访问服务器端的ip和port
ip_port=("127.0.0.1",8888)

#连接主机
client.connect(ip_port)

#定义一个循环，不断发送消息
while True:
    # 接收主机数据
    data = client.recv(1024)
    # 打印数据
    # 此处的byte数据需要解码
    print(data.decode())
    #输入发送的消息
    msg_input=input("输入发送的消息:")
    #消息发送
    client.send(msg_input.encode())

    data=client.recv(1024)
    print(data.decode())