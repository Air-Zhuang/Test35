# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/26 17:14'


'''
使用多线程
python中的线程只适合I/O型的操作
python不能实现真正意义上的并发
'''

from threading import Thread

def handle(n):
    print('handle')
    handletwo(n)

def handletwo(m):
    print('handletwo')
    print(m)

#第一种方法
# t=Thread(target=handle,args=(1,)) #args是一个元祖
# t.start()
# print('main thread\n'   #这里先运行这条主线程

#第二种方法，使用类
class MyThread(Thread):
    def __init__(self,n):
        Thread.__init__(self)
        self.n=n
    def run(self):
        handle(self.n)

# t2=MyThread(1)
# t2.start()
# t2.join() #等待当前线程退出再进行别的线程
# print('main thread\n'

threads=[]
for i in range(1,11):
    t3=MyThread(i)
    threads.append(t3)
    t3.start()
for i in threads:
    i.join()    #依次等待线程的退出

print('main thread\n')
