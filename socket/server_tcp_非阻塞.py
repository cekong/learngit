import socketserver
'''
可以多客户端进行s连接
'''
#定义一个类
class mysever(socketserver.BaseRequestHandler):
    #首先执行setup,再执行handle，最后执行finish
    #如果handle方法出现报错，则会跳过
    #setup和finish方法无论如何都会执行
    def setup(self):
        pass

    def handle(self):
        #定义连接变量
        conn=self.request
        #发送消息
        msg="hello!"
        conn.send(msg.encode())
        #进入循环，不断接收客户端的消息
        while True:
            data=conn.recv(1024)
            print(data.decode())
            if data==b'exit':
                break
            conn.send(data)
        conn.close()
    def finish(self):
            pass

if __name__=="__main__":
    #创建多线程实例
    s=socketserver.ThreadingTCPServer(("127.0.0.1",8888),mysever)
    #开启异步多线程，等待连接
    s.serve_forever()
