'''
signal.signal(signum,handler)
功能：处理信号
参数：signum 要处理的信号
      handler 信号的处理方法
      SIG_DEL 表示使用默认的方法处理
      SIG_IGN 表示忽略这个信号
      func 传入一个函数表示用指定函数处理
            def func()
'''

import signal
from time import sleep

signal.alarm(5)

#使用默认方法处理信号
# signal.signal(signal.SIGALRM,signal.SIG_DFL)

#忽略信号
# signal.signal(signal.SIGALRM,signal.SIG_IGN)

#自定义的方法
def handler(sig,frame):
    if sig==signal.SIGALRM:
        print("接收到时钟信号")
signal.signal(signal.SIGALRM,handler)

while True:
    sleep(2)
    print("等待时钟。。。")