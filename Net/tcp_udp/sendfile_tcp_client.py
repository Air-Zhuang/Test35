from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)
server_addr = ('127.0.0.1', 9998)
sockfd.connect(server_addr)


with open("file/2.jpeg", "wb") as f:
    while True:
        data = sockfd.recv(2048)
        if not data:
            break
        f.write(data)

sockfd.close()
