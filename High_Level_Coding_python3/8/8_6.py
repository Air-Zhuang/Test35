# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/27 18:19'

'''
如何使用多进程
使用标准库中multiprocessing.Process，它可以启动子进程执行任务，
操作接口，进程间通信，进程间同步等都与Threading.Thread类似
'''

from multiprocessing import Process
from multiprocessing import Queue,Pipe
import time
from threading import Thread

# q=Queue()
#
# def f(q):
#     print('start'
#     print(q.get()
#     print('end'
# def g(c):
#     c.send(c.recv()*2)
#
# p=Process(target=f,args=(q,))
# c1,c2=Pipe()
# p2=Process(target=g,args=(c2,))
#
# if __name__ == '__main__':
#     p.start()
#     time.sleep(2)
#     q.put(100)
#     time.sleep(2)
#     p2.start() 
#     c1.send(55)
#     print(c1.recv()

def isArmstrong(n):
    a,t=[],n
    while t>0:
        a.append(t % 10)
        t/=10
    k=len(a)
    return sum(x**k for x in a)==n
def findArmstrong(a,b):
    print(a,b)
    res=[k for k in range(a,b) if isArmstrong(k)]
    print('%s ~ %s: %s' % (a,b,res))
def findByThread(*argslist):
    workers=[]
    for args in argslist:
        worker=Thread(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()
def findByProcess(*argslist):
    workers=[]
    for args in argslist:
        worker=Process(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()
if __name__ == '__main__':
    start=time.time()
    findByProcess((20000000,25000000),(25000000,30000000))  #用多进程
    # findByThread((20000000,25000000),(25000000,30000000)) #用多线程
    print(time.time()-start)




