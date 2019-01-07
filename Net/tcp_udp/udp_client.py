from socket import *
from sys import argv

# host=argv[1]
# port=int(argv[2])
host="127.0.0.1"
port=9999
addr=(host,port)

sockfd=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("消息：")
    if not data:
        break
    sockfd.sendto(data.encode(),addr)
    data,addr=sockfd.recvfrom(1024)
    print("从服务器收到：",data.decode())