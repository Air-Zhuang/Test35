import asyncio
import time

sem=asyncio.Semaphore(3)

async def get_html(url):
    async with sem:
        print("==========start get url==========")
        print(url)
        await asyncio.sleep(1)                                  #不能用time.sleep()
        print("==========end get url==========")

if __name__ == '__main__':
    '''执行多个任务,wait'''
    start_time=time.time()
    loop=asyncio.get_event_loop()
    tasks=[get_html("https://www.baidu.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))        #接受一个可迭代对象
    print(time.time()-start_time)