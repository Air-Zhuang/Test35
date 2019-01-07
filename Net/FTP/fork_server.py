from socket import *
import os,sys
import signal

from FileLibrary import FileLibrary
filelib=FileLibrary()


HOST = ""
PORT = 8888
ADDR = (HOST,PORT)

#处理客户端请求
def client_handler(c):
    try:
        print("处理子进程的请求",c.getpeername())
        while True:
            data = c.recv(1024*1024)
            if not data:
                break
            print(data.decode())
            if data.decode() == "1":
                c.send(filelib.showAll().encode())
            elif data.decode().startswith("2"):
                filename=data.decode().split(" ")[1]
                print(filename)
                filelib.download(c,filename)
            elif data.decode().startswith("3"):
                c.send("上传完成".encode())
            else:
                c.send("收到客户端请求".encode())
    except (KeyboardInterrupt,SystemError):
        sys.exit("客户端退出")
    except Exception as e:
        print(e)
    c.close()
    sys.exit(0)

s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

print("等待%d客户端链接"%os.getpid())

#在父进程中忽略子进程状态改变，子进程退出自动由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("Error:",e)
        continue

    #为客户端创建新的进程，处理请求
    pid = os.fork()

    #子进程处理具体请求
    if pid == 0:
        s.close()
        client_handler(c)

    #父进程或者创建失败都继续等待下个客户端连接
    else:
        c.close()
        continue