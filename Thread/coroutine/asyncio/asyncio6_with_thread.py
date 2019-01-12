'''
在协程中集成阻塞io:
    比如集成pymysql就需要另起一个线程
'''

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

async def get_html(url):
    print("==========start get url==========")
    print(url)
    await asyncio.sleep(1.5)
    print("==========end get url==========")

def sleep_times(times):
    time.sleep(times)
    print("阻塞了:",str(times),"秒")

if __name__ == '__main__':
    start_time=time.time()
    loop=asyncio.get_event_loop()
    executor=ThreadPoolExecutor()
    tasks=[]
    tasks.append(get_html("https://www.baidu.com"))         #加入一个协程任务
    for i in range(1,5):
        task=loop.run_in_executor(executor,sleep_times,i)   #将阻塞io的操作放到run_in_executor中执行
        tasks.append(task)                                  #加入阻塞io任务
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time:{}".format(time.time()-start_time))