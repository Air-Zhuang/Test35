'''
. 司机和售票员
 * 创建父子进程 分别表示司机和售票员
 * 当售票员捕捉到SIGINT信号ctrl+c，给司机发送SIGUSER1信号，此时司机打印“老司机开车了”
   当售票员捕捉到SIGQUIT信号ctrl+\，给司机发送SIGUSER2信号，此时司机打印："车速有点快，系好安全带"
   当司机捕捉到SIGTSTP信号ctrl+z，给售票员发送SIGUSER1,此时售票员打印“到站了请下车”
 * 到站后，售票员先下车（子进程先退出），然后司机下车
'''

import signal
from time import sleep
import multiprocessing as mp
import os

q = mp.Queue()
def handler_SIGALRM(sig,frame):#ctrl+c
    global q
    if sig==signal.SIGINT:
        q.put(1)
def handler_SIGQUIT(sig,frame):#ctrl+\
    global q
    if sig==signal.SIGQUIT:
        q.put(2)
def handler_SIGTSTP(sig,frame):#ctrl+z
    global q
    if sig==signal.SIGTSTP:
        q.put(3)
def drive(q):
    for i in range(20):
        sleep(0.5)
        print("===========================在开车")
        if not q.empty():
            q.get()
            res = q.get()
            if res==1:
                print("老司机开车了")
            elif res==2:
                print("车速有点快，系好安全带")
            else:
                print("到站了请下车")

signal.alarm(30)
signal.signal(signal.SIGINT, handler_SIGALRM)
signal.signal(signal.SIGQUIT, handler_SIGQUIT)
signal.signal(signal.SIGTSTP, handler_SIGTSTP)
p2=mp.Process(target=drive,args=(q,))
p2.start()
p2.join()