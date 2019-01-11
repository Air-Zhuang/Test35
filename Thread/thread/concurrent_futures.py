'''
用于线程池和进程池编程(顶层的包,高度封装)

主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
当一个线程完成的时候我们主线程能立即知道
futures可以让多线程和多进程编码接口一致
'''

from concurrent.futures import ThreadPoolExecutor,as_completed,wait
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return str(times)                           #使用线程池可以获取返回值


'''基本用法'''
exector=ThreadPoolExecutor(max_workers=2)       #创造最大进程数为2的线程池
task1=exector.submit(get_html,(0.5))            #传参必须这么写,不知道原因
task2=exector.submit(get_html,(0.3))
task3=exector.submit(get_html,(0.4))

print("task3任务已取消:",task3.cancel())         #取消任务(任务必须还未开始执行)
print("task1任务已完成：",task1.done())          #判断任务是否已执行完(立即执行，不会被上面的代码阻塞)
time.sleep(1)
print("task1任务已完成：",task1.done())
print("task1返回值：",task1.result())            #可以获取任务的返回值
print()

'''获取已经完成的task的返回'''
urls=[2,1,3]
all_task=[exector.submit(get_html,(i)) for i in urls]
wait(all_task)                                  #等待某个任务执行完成,必须传iterable
print("main")
for i in as_completed(all_task):
    res=i.result()
    print("返回值为:",res)
print()


'''通过executor获取已经完成的task的返回'''
for i in exector.map(get_html,urls):
    print("返回值为:", i)
print()

'''with'''
def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)

with ThreadPoolExecutor(3) as exector:
    all_task=[exector.submit(fib,(num)) for num in range(25,35)]
    start_time=time.time()
    for i in as_completed(all_task):
        res = i.result()
        print("exe result:{}".format(res))
    print(time.time()-start_time)
print()
