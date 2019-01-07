from threading import Thread
from datetime import datetime
import time

class MyThread(Thread):
    def __init__(self,target,args,kwargs):
        super(MyThread,self).__init__()
        self._args=args
        self._kwargs=kwargs
        self._target=target
    # def run(self):
    #     self.target(*self.args,**self.kwargs)


def player(song,sec):
    for i in range(2):
        print(song,datetime.now())
        time.sleep(sec)

t=MyThread(target=player,args=['热热'],kwargs={'sec':2})
t.start()
t.join()