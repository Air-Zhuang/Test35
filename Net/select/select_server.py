from select import select
from socket import *

#创建套接字作为我们关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
'''
rlist 列表 存放我们监控等待处理的IO事件
wlist 列表 存放我们要主动处理的IO事件             (不常用)
xlist 列表 存放如果发生异常需要我们处理的IO事件    (不常用)    
timeout 数据 超时时间
'''
rlist=[s]
wlist=[]
xlist=[]

while True:
    #提交检测我们关注的IO等待IO发生
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr=rs[0].accept()
            print("Connect from",addr)
            rlist.append(c) #添加到关注列表
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                r.send(b'Receive your message')
    for w in ws:
        w.send(b'Receive your message')
        w.remove(w)