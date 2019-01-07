'''
https://blog.csdn.net/zhiyuan_2007/article/details/48807761
python线程join的正解
几个事实

1 python 默认参数创建线程后，不管主线程是否执行完毕，都会等待子线程执行完毕才一起退出，有无join结果一样

2 如果创建线程，并且设置了daemon为true，即thread.setDaemon(True), 则主线程执行完毕后自动退出，不会等待子线程的执行结果。而且随着主线程退出，子线程也消亡。

3 join方法的作用是阻塞，等待子线程结束，join方法有一个参数是timeout，即如果主线程等待timeout，子线程还没有结束，则主线程强制结束子线程。

4 如果线程daemon属性为False， 则join里的timeout参数无效。主线程会一直等待子线程结束。

5 如果线程daemon属性为True， 则join里的timeout参数是有效的， 主线程会等待timeout时间后，结束子线程。
    此处有一个坑，即如果同时有N个子线程join(timeout），那么实际上主线程会等待的超时时间最长为 N ＊ timeout， 因为每个子线程的超时开始时刻是上一个子线程超时结束的时刻。
'''

import threading, time


def doThreadTest():
    print('start thread time:', time.strftime('%H:%M:%S'))
    time.sleep(10)
    print('stop thread time:', time.strftime('%H:%M:%S'))


threads = []
for i in range(3):
    thread1 = threading.Thread(target=doThreadTest)
    '''如果把    thread1.setDaemon(True) 注释掉， 运行结果为'''
    thread1.setDaemon(True)

    threads.append(thread1)

for t in threads:
    t.start()

for t in threads:
    t.join(timeout=1)
print('stop main thread')
