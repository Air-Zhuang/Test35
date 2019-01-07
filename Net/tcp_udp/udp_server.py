from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("localhost",9999))

while True:
    data,addr=sockfd.recvfrom(1024)
    print("Receive from %s:%s" % (addr,data.decode("utf-8")))
    sockfd.sendto("收到你的消息".encode(),addr)

sockfd.close()
