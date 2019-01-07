# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/27 15:55'

'''
如何在线程间进行事件通知

线程间的时间通知，可以使用标准库中Threading.Event:
1、等待事件一段调用wait，等待事件。
2、通知事件一端调用set，通知事件
'''

from threading import Event,Thread
import time
from Queue import Queue #这是一个线程安全的队列
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\8_2.txt"

#例
# def f(e):
#     print('f 0'
#     e.wait()    #等待一个事件的通知
#     print('f 1'
# e=Event()
# t=Thread(target=f,args=(e,))
# t.start()
# time.sleep(2)
# e.set()         #通知
# e.clear()       #想继续使用e.wait,需使用clear清理

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
        self.queue.put((data,))  #使用queue的输入是元祖

class ConvertThread(Thread):
    def __init__(self,queue,cEvent,tEvent):
        Thread.__init__(self)
        self.queue=queue
        self.cEvent = cEvent
        self.tEvent = tEvent
    def handletwo(self,m):
        with open(path,'wb+') as f:
            f.write(m)
    def run(self):
        count=0
        while True:
            data=self.queue.get()
            print('Convert',data)
            if data==-1:    #使循环停下
                self.cEvent.set()
                self.tEvent.wait()
                break
            self.handletwo(str(data[0]))
            count+=1
            if count==5:
                self.cEvent.set()

                self.tEvent.wait()
                self.tEvent.clear()
                count=0
class TarThread(Thread):
    def __init__(self,cEvent,tEvent):
        Thread.__init__(self)
        self.cEvent=cEvent
        self.tEvent=tEvent
        self.setDaemon(True)    #设置成守护线程，其他线程结束，自动结束
    def readfile(self):
        with open(path,'rb+') as f:
            print(f.read())
    def run(self):
        while True:
            self.cEvent.wait()
            self.readfile()
            self.cEvent.clear()

            self.tEvent.set()

q=Queue()
dThreads=[DownThread(i,q) for i in range(1,15)]

cEvent=Event()
tEvent=Event()

cThreads=ConvertThread(q,cEvent,tEvent)
tThread=TarThread(cEvent,tEvent)
tThread.start()
for i in dThreads:
    i.start()
cThreads.start()

for t in dThreads:
    t.join()
print('Main thread\n')

q.put((-1,))  #使循环停下

# import tarfile
#
# 压缩文件
# def tarXML(tfname):
#     tf=tarfile.open(tfname,'w:gz')
#     for fname in os.listdir('.'):
#         if fname.endswith('.xml'):
#             tf.add(fname)
#             os.remove(fname)
#     tf.close()
#     if not tf.members:
#         os.remove(tfname)