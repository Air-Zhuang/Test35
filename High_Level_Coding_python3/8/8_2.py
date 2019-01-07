# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/26 18:25'

'''
如何进行线程之间的通讯
使用标准库中的Queue.Queue,他是一个线程安全的队列
'''

from threading import Thread
from collections import deque
from queue import Queue #这是一个线程安全的队列
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\test\\8_2.txt"

# q=deque() #在这样使用是线程不安全的

class DownThread(Thread):
    def __init__(self,n,queue):
        Thread.__init__(self)
        self.n=n
        self.queue=queue
    def handle(self,n):
        a = n + 2
        return a
    def run(self):
        data=self.handle(self.n)
        print('Download',data)
        # q.append(data)  #在这样使用是线程不安全的
        self.queue.put((data,))  #使用queue的输入是元祖

class ConvertThread(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue=queue
    def handletwo(self,m):
        with open(path,'wb+') as f:
            f.write(m)
    def run(self):
        while True:
            data=self.queue.get()
            print('Convert',data)
            if data==-1:    #使循环停下
                break
            self.handletwo(str(data[0]))

q=Queue()
dThreads=[DownThread(i,q) for i in range(1,11)]
cThreads=ConvertThread(q)
for i in dThreads:
    i.start()
cThreads.start()

for t in dThreads:
    t.join()
print('Main thread\n')

q.put((-1,))  #使循环停下