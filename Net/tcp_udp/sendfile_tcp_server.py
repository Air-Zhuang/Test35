from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(("localhost", 9998))
sockfd.listen(1)
connfd, addr = sockfd.accept()

with open("file/1.jpeg", "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        connfd.send(data)

    print("数据已发送")

connfd.close()
sockfd.close()
