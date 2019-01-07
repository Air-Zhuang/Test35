import multiprocessing as mp
import time

def th1():
    time.sleep(2)
    print("th1")
def th2():
    time.sleep(3)
    print("th2")
def th3():
    time.sleep(4)
    print("th3")

if __name__ == '__main__':
    things=[th1,th2,th3]
    process=[]

    for th in things:
        p=mp.Process(target=th)
        process.append(p)
        p.start()

    #循环回收进程
    for i in process:
        i.join()
