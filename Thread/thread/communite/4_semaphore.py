'''
semaphore 是用于控制并发数量的锁
    底层实际用Condition()完成的
'''

import threading
import multiprocessing as mp
import time,os

'''===========用于threading===================================='''
class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(1)
        print(self.url)
        self.sem.release()          #信号量加一

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()      #信号量减一
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()

if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()

'''===========用于multiprocessing===================================='''
# sem=mp.Semaphore(3)
# def fun():
#     print("进程%d等待信号量" % os.getpid())
#     sem.acquire()       #信号量减一
#     print("进程%d消耗信号量" % os.getpid())
#     time.sleep(3)
#     sem.release()       #信号量加一
#     print("进程%d添加信号量" % os.getpid())
# if __name__ == '__main__':
#     jobs=[]
#     for i in range(4):
#         p=mp.Process(target=fun)
#         jobs.append(p)
#         p.start()
#     for i in jobs:
#         i.join()
#     print(sem.get_value())
