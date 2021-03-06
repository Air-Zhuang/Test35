'''
尽量用ThreadPoolExecutor进行多线程编程

线程模块：
Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
    threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Threading类来处理线程，Threading类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
'''

import threading
import time
from datetime import datetime

'''==============类================================='''
class myThread(threading.Thread):
    def __init__(self, name, counter):
        super().__init__(name=name)
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        while self.counter:
            time.sleep(0.5)
            print("%s: %s" % (self.name, time.ctime(time.time())))
            self.counter -= 0.5
        print("退出线程：" + self.name)



# 创建新线程
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()  # 如果没有显示的设置thread.setDaemon(True),这条join没卵用，因为默认也会等待子线程退出再退出主线程
thread2.join()
print("退出主线程")
print()

'''==============类================================='''
class MyThread(threading.Thread):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.kwargs=kwargs
        self.args = args
    def run(self):
        self.player(*self.args,**self.kwargs)

    @staticmethod
    def player(song,sec):
        for i in range(2):
            print(song,datetime.now())
            time.sleep(sec)

t=MyThread('air1',sec=0.5)
t.start()
t.join()
print()

'''==============方法================================='''
def player(song,sec):
    for i in range(2):
        print(song,datetime.now())
        time.sleep(sec)

t=threading.Thread(target=player,args=['air2'],kwargs={'sec':0.5})
t.start()
t.join()
print()


