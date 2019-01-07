from socket import *
from FileLibrary import FileLibrary
filelib=FileLibrary()

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

while True:
    message='''请输入对应指令前的编号执行指令
    1、查看服务器文件库中所有普通文件
    2、下载 格式:2 下载的文件全名 新文件名
    3、上传 格式:3 上传的文件全名 新文件名
    4、退出
    >>
    '''
    #消息发送接收
    request = input(message)
    if not request:
        break
    sockfd.send(request.encode())
    response = sockfd.recv(1024*1024)
    if request.startswith("2"):
        filename = request.decode().split(" ")[2]
        filelib.writefile(filename,response)
        continue
    print("服务器:",response.decode())

#关闭套接字
sockfd.close()