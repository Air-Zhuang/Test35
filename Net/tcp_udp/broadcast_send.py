from socket import *
import time

#设置目标地址
dest=('176.140.8.41',9999)
s=socket(AF_INET,SOCK_DGRAM)

#设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    time.sleep(2)
    s.sendto("ssssssssssss".encode(),dest)
s.close()