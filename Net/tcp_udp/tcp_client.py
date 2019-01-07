from socket import *

sockfd=socket(AF_INET,SOCK_STREAM)

server_addr=('127.0.0.1',9998)
sockfd.connect(server_addr)
print("开始对话：(q退出)")
print()


while True:
    data=input("发送>>")
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    if data.decode("utf-8")=="qq":
        print("客户端关闭：Bye~~")
        break
    print("客户端响应：",data.decode("utf-8"))

sockfd.close()