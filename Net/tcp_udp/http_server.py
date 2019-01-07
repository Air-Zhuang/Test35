from socket import *

def handleClient(connfd):
    request=connfd.recv(4096)
    # print(request)
    request_lines=request.splitlines()        #切割bytes文件
    for i in request_lines:
        print(i.decode("utf-8"))

    try:
        f=open("file/index.html")
    except IOError:
        response="HTTP/1.0 404 not found\r\n"
        response+="\r\n"
        response+="====Sorry not found===="
    else:
        response = "HTTP/1.0 200 OK\r\n"
        response += "\r\n"
        response += f.read()
    finally:
        connfd.send(response.encode())      #发送给浏览器

def main():
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8889))
    sockfd.listen(3)
    print("Listen to the port 8889")
    while True:
        connfd,addr=sockfd.accept()

        #处理请求
        handleClient(connfd)
        connfd.close()

if __name__ == '__main__':
    main()


