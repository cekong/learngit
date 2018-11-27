''''''
'''
https://www.cnblogs.com/patrick0715/p/5875995.html
    在发送之前先告诉接受数据端我要发送数据的字节大小
    接收数据端收到数据后回复给数据发送端一个确认消息
    数据发送端收到确认信息后,发送数据
    数据接收端循环接受数据,直到数据接受完成,收到完整数据包

'''
import socket
ip_port=('127.0.0.1',9999)

s=socket.socket()

s.connect(ip_port)

while True:
    send_data=input('send message >>:').strip()


    if send_data=='exit':break
    if len(send_data)==0:continue
    s.send(bytes(send_data,encoding='utf8'))

    ready_tag=s.recv(1024)
    ready_tag=str(ready_tag,encoding='utf8')
    if ready_tag.startswith('Ready'):
        msg_size=int(ready_tag.split('|')[-1])
        print(msg_size)
    start_tag='Start'
    s.send(bytes(start_tag,encoding='utf8'))

    recv_size=0
    recv_msg=b''

    while recv_size < msg_size:
        recv_data=s.recv(1024)
        recv_msg+=recv_data
        recv_size+=len(recv_data)

    print(str(recv_msg,encoding='utf8'))


s.close()