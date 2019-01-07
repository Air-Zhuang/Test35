from threading import Thread,Lock
import time

l=[]
def aaa(lock):
    lock.acquire()
    for i in range(4):
        time.sleep(0.1)
        l.append('a')
    lock.release()
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

if __name__ == '__main__':
    lock=Lock()
    t1=Thread(target=aaa,args=(lock,))
    t2=Thread(target=bbb,args=(lock,))
    t3=Thread(target=ccc,args=(lock,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(l)