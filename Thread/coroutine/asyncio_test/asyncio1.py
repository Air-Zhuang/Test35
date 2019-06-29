import asyncio
import time

async def get_html(url):
    print("==========start get url==========")
    print(url)
    await asyncio.sleep(1)                                  #不能用time.sleep()
    print("==========end get url==========")

# if __name__ == '__main__':
#     '''执行一个任务'''
#     start_time=time.time()
#     loop=asyncio.get_event_loop()                               #定义事件循环
#     loop.run_until_complete(get_html("https://www.baidu.com"))  #类似多线程里面的join(),运行完指定的协程,关闭loop
#     print(time.time()-start_time)
#     print()

if __name__ == '__main__':
    '''执行多个任务,wait'''
    start_time=time.time()
    loop=asyncio.get_event_loop()
    tasks=[get_html("https://www.baidu.com") for i in range(4)]
    loop.run_until_complete(asyncio.wait(tasks))        #接受一个可迭代对象
    print(time.time()-start_time)

# # if __name__ == '__main__':
#     '''执行多个任务,gather'''
#     '''gather时比wait更高一层的功能抽象'''
#     start_time = time.time()
#     loop=asyncio.get_event_loop()
#     task1=[get_html("https://www.baidu.com") for i in range(2)]
#     task2=[get_html("https://www.taobao.com") for i in range(2)]
#     loop.run_until_complete(asyncio.gather(*task1,*task2))
#     print(time.time() - start_time)