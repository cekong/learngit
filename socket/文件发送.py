''''''
'''客户端'''
import socket

#创建实例
client=socket.socket()

#访问服务器端的ip和port
ip_port=("127.0.0.1",9999)

#连接服务器
client.connect(ip_port)

#文件上传#打开文件
with open('socket_client_tcp.py','rb') as f:#使用’rb’按照二进制位进行读取的，
                                            # 不会将读取的字节转换成字符
    #按每一段分割文件
    for i in f:
        #数据上传
        client.send(i)
        # 等待接收完成的标志
        data = client.recv(1024)
        # 判断服务器端是否真正的接收
        if data !=b'success':
            break
# 给服务器端发送结束信号
client.send('quit'.encode())




