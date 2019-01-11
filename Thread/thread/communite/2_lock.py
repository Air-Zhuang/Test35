'''
线程同步
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
使用 Threading 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：
多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。
经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。

python多线程中Lock()与RLock()锁:
https://blog.csdn.net/comprel/article/details/72798354
1.threading.Lock() 加载线程的锁对象，是一个基本的锁对象，一次只能一个锁定，其余锁请求，需等待锁释放后才能获取
2.threading.RLock() 多重锁，在同一线程中可用被多次acquire。如果使用RLock，那么acquire和release必须成对出现，
    调用了n次acquire锁请求，则必须调用n次的release才能在线程中释放锁对象
缺点：
    1、用锁会影响性能
    2、锁会引起死锁,RLock()避免了一定的死锁,所以一般用RLock()
'''

import threading
import time

class myThread (threading.Thread):
    def __init__(self, name, counter):
        super(myThread, self).__init__(name=name)
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        threadLock.acquire()    # 获取锁，用于线程同步
        print_time(self.name,0.5,self.counter)
        threadLock.release()    # 释放锁，开启下一个线程

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

'''创建锁对象'''
threadLock = threading.RLock()

thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")
print()

'''==============================================================================='''

l=[]
def aaa(lock):
    lock.acquire()      #加锁
    for i in range(4):
        time.sleep(0.1)
        l.append('a')
    lock.release()      #释放
def bbb(lock):
    lock.acquire()
    for i in range(4):
        time.sleep(0.1)
        l.append('b')
    lock.release()
def ccc(lock):
    lock.acquire()
    for i in range(4):
        time.sleep(0.1)
        l.append('c')
    lock.release()

lock=threading.RLock()
t1=threading.Thread(target=aaa,args=(lock,))
t2=threading.Thread(target=bbb,args=(lock,))
t3=threading.Thread(target=ccc,args=(lock,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(l)