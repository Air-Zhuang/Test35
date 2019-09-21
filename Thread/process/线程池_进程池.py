'''
用于线程池和进程池编程(顶层的包,高度封装)

主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
当一个线程完成的时候我们主线程能立即知道
futures可以让多线程和多进程编码接口一致
'''

import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed

'''https://www.jianshu.com/p/b9b3d66aa0be'''

def x(a):
    time.sleep(1)
    return "执行结果："+str(a)


threadpool=ThreadPoolExecutor(max_workers=2)

tasks=[threadpool.submit(x,i) for i in range(10)]

for each_task in as_completed(tasks):
    result=each_task.result()
    print(result)

'''======================进程池必须写在main函数中,不然报错======================================'''
# processpool=ProcessPoolExecutor(max_workers=2)
#
# if __name__ == '__main__':
#     tasks = [processpool.submit(x, i) for i in range(10)]
#     for each_task in as_completed(tasks):
#         result=each_task.result()
#         print(result)