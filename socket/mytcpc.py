import cv2
from socket import *
from time import ctime, sleep
import threading
import numpy as np

tcpPort = "0"
tcpIp = ""
threads = []

class udpbroadcast:
    def __init__(self):
        # 全局参数配置
        self.encoding = "utf-8"  # 使用的编码方式
        self.broadcastPort = 22222  # 广播端口

        # 创建广播接收器
        self.recvSocket = socket(AF_INET, SOCK_DGRAM)
        self.recvSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.recvSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.recvSocket.bind(('', self.broadcastPort))

        # 创建广播发送器
        self.sendSocket = socket(AF_INET, SOCK_DGRAM)
        self.sendSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    def send(self):
        """发送广播"""

        print("UDP发送器启动成功...")
        while True:
            sendData = str(tcpPort)
            self.sendSocket.sendto(sendData.encode(self.encoding), ('255.255.255.255', self.broadcastPort))
            print("【%s】%s:%s" % (ctime(), "我", sendData))

            sleep(1)
        self.sendSocket.close()

    def recv(self,isrunning,flag):
        """接收广播"""
        global tcpIp
        global tcpPort

        print("UDP接收器启动成功...")
        while True:
            if not isrunning:
                break
            flag.wait()

            # 接收数据格式：(data, (ip, port))
            recvData = self.recvSocket.recvfrom(1024)
            tcpIp = recvData[1][0]
            tcpPort = recvData[0]
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
        mudpbroadcast = udpbroadcast()
        mudpbroadcast.recv(self.__running.isSet(),self.__flag)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        print(self.__flag, self.__running)
        self.__flag.set()  # 将线程从暂停状态恢复, 如果已经暂停的话
        self.__running.clear()  # 设置为False


class tcpsocket:
    def __init__(self):
        global tcpIp
        global tcpPort
        print("接收到的tcpPort：", tcpPort)
        self.dest_addr = (tcpIp, int(tcpPort))

        # 1.创建套接字socket
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.connflag=False


    def tcpsendrecv(self,isrunning,flag):

        cv2.namedWindow('img')
        while True:
            if tcpPort != "0" and not self.connflag:
                self.dest_addr = (tcpIp, int(tcpPort))
                # 2.连接服务器
                print("接收到的dest_addr：", self.dest_addr)
                self.tcp_socket.connect(self.dest_addr)
                self.connflag=True

            if self.connflag:
                if not isrunning:
                    break
                flag.wait()

                # 3. 接收/发送数据
                #send_data = input("请输入要发送的数据：")
                send_data ="1"
                self.tcp_socket.send(send_data.encode("utf-8"))
                print("send_data",send_data)

                # 接收服务器发送的数据
                recv_data_size=self.tcp_socket.recv(1024)
                recv_data_size=int(recv_data_size.decode("utf-8"))
                print(recv_data_size)
                recv_data = self.tcp_socket.recv(recv_data_size)
                #print(recv_data.decode("utf-8"))
                print(len(recv_data))
                while len(recv_data)<recv_data_size:
                    recv_data0 = self.tcp_socket.recv(recv_data_size)
                    recv_data=recv_data+recv_data0


                recv_databuf = np.frombuffer(recv_data, dtype=np.uint8)

                if len(recv_data)!=0:
                    imde = cv2.imdecode(recv_databuf, 1)
                    print(imde.shape)
                    print("imshow........")
                    cv2.imshow('img', imde)
                    k = cv2.waitKey(1)
                    if k == ord('q'):
                        self.sendData = "0"
                        break

            sleep(1)
        # 4. 关闭套接字socket
        self.tcp_socket.close()
        cv2.destroyAllWindows()


class tcpsocketThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(tcpsocketThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        print('running thread: ', self.getName())
        mtcpsocket = tcpsocket()
        mtcpsocket.tcpsendrecv(self.__running.isSet(),self.__flag)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):

        self.__flag.set()  # 将线程从暂停状态恢复, 如果已经暂停的话
        self.__running.clear()  # 设置为False



class doThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        print('running thread: ', self.getName())
        global threads
        global tcpPort
        t1=threads[0]
        t2 = threads[1]

        while True:
            if tcpPort == "0":
                #print("-----hello-----")
                t1.resume()
                t2.pause()
            else:
                #print("-----hello2-----")
                t1.pause()
                t2.resume()
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


    t1 = udpbroadcastThread()
    threads.append(t1)
    t2 = tcpsocketThread()
    threads.append(t2)
    t3 = doThread()
    threads.append(t3)

    for t in threads:
        #t.setDaemon(True)
        t.start()
    #threads_join(threads)



