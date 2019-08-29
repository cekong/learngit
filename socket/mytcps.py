import cv2
from socket import *
from time import ctime, sleep
import threading

tcpPort = "10102"   # 广播端口
tcp_recv_data=""
class udpbroadcast:
    def __init__(self):
        # 全局参数配置
        self.encoding = "utf-8"  # 使用的编码方式
        self.broadcastPort = 22222   # 广播端口

        # 创建广播接收器
        self.recvSocket = socket(AF_INET, SOCK_DGRAM)
        self.recvSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.recvSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.recvSocket.bind(('', self.broadcastPort))

        # 创建广播发送器
        self.sendSocket = socket(AF_INET, SOCK_DGRAM)
        self.sendSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)



    def send(self,isrunning,flag):
        """发送广播"""
        global tcpPort
        print("UDP发送器启动成功...")
        while True:
            if not isrunning:
                break
            flag.wait()
            sendData=str(tcpPort)
            self.sendSocket.sendto(sendData.encode(self.encoding), ('255.255.255.255', self.broadcastPort))
            print("【%s】%s:%s" % (ctime(), "我", sendData))

            sleep(1)
        self.sendSocket.close()

    def recv(self):
        """接收广播"""

        print("UDP接收器启动成功...")
        while True:
            # 接收数据格式：(data, (ip, port))
            recvData = self.recvSocket.recvfrom(1024)

            print("【%s】[%s : %s] : %s" % (ctime(), recvData[1][0], recvData[1][1], recvData[0].decode(self.encoding)))

            sleep(1)

class udpbroadcastThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(udpbroadcastThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        print('running thread: ', self.getName())
        mudpbroadcast=udpbroadcast()
        mudpbroadcast.send(self.__running.isSet(),self.__flag)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如果已经暂停的话
        self.__running.clear()  # 设置为False

class tcpsocket:
    def __init__(self):
        global tcpPort
        # 1.创建套接字
        self.tcp_server_socket = socket(AF_INET, SOCK_STREAM)
        # 2.绑定端口
        addr = ("", int(tcpPort))
        self.tcp_server_socket.bind(addr)
        self.cap = cv2.VideoCapture('ex2.mp4')
        self.connflag=False

    def tcpsendrecv(self,isrunning,flag):
        global tcp_recv_data
        while True:
            if not self.connflag:
                # 3.监听链接
                self.tcp_server_socket.listen(128)
                # 4.接收别人的连接
                # client_socket用来为这个客户端服务
                client_socket, client_addr = self.tcp_server_socket.accept()
                print(client_addr)
                self.connflag=True
            if self.connflag:
                if not isrunning:
                    break
                flag.wait()
                # 5.接收对方发送的数据
                recv_data = client_socket.recv(1024)
                tcp_recv_data=recv_data.decode("utf-8")
                # print("接收到的数据：%s" % recv_data.decode("utf-8"))

                # 6.给对方发送数据
                # client_socket.send("hahaha".encode("utf-8"))
                if recv_data == b'1':
                    ret, fra = self.cap.read()
                    print(ret)
                    if ret:
                        _, sendData = cv2.imencode('.jpg', fra)
                        print(sendData.size)
                        print(fra.size)
                        client_socket.send(str(sendData.size).encode("utf-8"))
                        client_socket.send(sendData)


        # 7.关闭套接字
        client_socket.close()
        self.tcp_server_socket.close()
        self.cap.release()


class tcpsocketThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(tcpsocketThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        print('running thread: ', self.getName())
        mtcpsocket=tcpsocket()
        mtcpsocket.tcpsendrecv(self.__running.isSet(),self.__flag)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False
class doThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        print('running thread: ', self.getName())
        global threads
        global tcpPort
        global tcp_recv_data
        t1=threads[0]
        t2 = threads[1]

        while True:
            # print("t3:",tcp_recv_data)
            if tcp_recv_data == "":
                #print("-----hello1-----")
                t1.resume()
            else:
                #print("-----hello2-----")
                t1.pause()
            sleep(1)

def threads_join(threads):
    # 令主线程阻塞，等待子线程执行完才继续，使用这个方法比使用join的好处是，可以ctrl+c kill掉进程
    for t in threads:
        while 1:
            if t.isAlive():
                sleep(10)
            else:
                break

if __name__ == "__main__":
    threads = []
    t1 = udpbroadcastThread()
    threads.append(t1)
    t2 = tcpsocketThread()
    threads.append(t2)
    t3 = doThread()
    threads.append(t3)


    for t in threads:
        # t.setDaemon(True)
        t.start()
    # threads_join(threads)