'''
Queue:
    非线程安全
    协程间的通讯比较容易，可以声明一个全局变量list来实现，但是当需要限制长度的时候就需要使用asyncio.Queue来实现
'''

import asyncio
import random
import time


async def worker(name, queue):
    while True:
        sleep_for = await queue.get()
        await asyncio.sleep(sleep_for)
        queue.task_done()
        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    queue = asyncio.Queue()

    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        # queue.put_nowait(sleep_for)   #put_nowait不需要加await
        await queue.put(sleep_for)

    tasks = []
    for i in range(3):
        task = asyncio.ensure_future(worker(f'worker-{i}', queue))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()          #等到所有queue的操作完成
    total_slept_for = time.monotonic() - started_at

    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())