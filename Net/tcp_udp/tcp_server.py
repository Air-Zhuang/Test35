'''
recv()  特征
* 如何连接的另一端断开连接，则recv立即返回空子串
* recv是从接受缓冲区取出内容，当缓冲区为空则阻塞
* recv如果一次接受不完缓冲区内容，下次会继续接收

send() 特征
* 如果发送的另外一段不存在则会产生Pipe Broken
* recv是向发送缓冲区发送内容，当缓冲区为满阻塞
'''

from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(("localhost",9998))
sockfd.listen(1)

print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)
print("开始对话：")
print()

while True:
    data = connfd.recv(1024)
    if data.decode("utf-8")=="q":
        connfd.send(b"qq")
        print("服务器关闭，Bye~~")
        break
    print("服务器接收消息：",data.decode("utf-8"))
    connfd.send(b"I have received your message")
connfd.close()

sockfd.close()