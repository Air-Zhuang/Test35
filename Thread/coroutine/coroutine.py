'''
协程四个状态
等待开始执行
解释器正在执行
在yield表达式处暂停
执行结束
'''
# def simple_coroutine():
#     print('-> coroutine started')
#     x=yield
#     print('-> coroutine received')
#
# my_coro=simple_coroutine()
# print(my_coro)
# print(1)
# next(my_coro)
# print(2)
# try:
#     my_coro.send(42)
# except StopIteration as e:
#     print(e)

'''gevent'''
import gevent
def foo(a,b):
    print("a=%d,b=%d" % (a,b))
    gevent.sleep(2)
    print("Running foo again")
def bar():
    print("Running int bar")
    gevent.sleep(3)
    print("Running bar again")

#生成协程
f=gevent.spawn(foo,1,2)
g=gevent.spawn(bar)
print('=====================')
gevent.joinall([f,g])
print('%%%%%%%%%%%%%%%%%%%%%')

import gevent
from gevent import  monkey
monkey.patch_all()

'''利用协程实现并发tcp服务器'''
from socket import *
from time import ctime

def handler(connfd):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(ctime().encode())
    c.close()

def server(port):
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",port))
    sockfd.listen(5)
    while True:
        connfd,addr = sockfd.accept()
        print("Connect from ",addr)
        # handler(connfd)
        gevent.spawn(handler,connfd)


if __name__ == "__main__":
    server(8888)
