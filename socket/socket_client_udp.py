import socket

#创建实例  udp方式
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#访问服务器端的ip和port
ip_port=("127.0.0.1",8888)

#连接主机
client.connect(ip_port)

#定义一个循环，不断发送消息
while True:
    # 输入发送的消息
    msg_input = input("输入发送的消息:")

    if msg_input=='exit':
        break

    # 消息发送
    client.sendto(msg_input.encode(),ip_port)

# 发送关闭信息
client.close()