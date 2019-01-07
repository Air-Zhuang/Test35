'''
使用os.fork实现多进程编写
'''

import os,time

print("程序开始执行：")
pid=os.fork()
print(id(pid))
time.sleep(0.5)

if pid<0:
    print("创建进程失败")
elif pid==0:
    #获取当前进程的PID
    print("这是新的进程",os.getpid())
    #获取父进程的PID
    print("父进程PID",os.getpid())
else:
    print("这是原有进程")