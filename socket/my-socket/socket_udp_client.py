''''''
'''
https://www.cnblogs.com/fanweibin/p/5053328.html
'''

from socket import *

HOST = "127.0.0.1"
PORT = 8080

s = socket(AF_INET,SOCK_DGRAM)
s.connect((HOST,PORT))
while True:
        message = input('send message: ')
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(data)
s.close()