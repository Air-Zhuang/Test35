'''
用于线程池和进程池编程(顶层的包,高度封装)

主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
当一个线程完成的时候我们主线程能立即知道
futures可以让多线程和多进程编码接口一致
'''

from concurrent.futures import ProcessPoolExecutor,as_completed
import time

def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    with ProcessPoolExecutor(3) as exector:
        all_task=[exector.submit(fib,(num)) for num in range(25,35)]
        start_time=time.time()
        for i in as_completed(all_task):
            res = i.result()
            print("exe result:{}".format(res))
        print(time.time()-start_time)
    print()
