import asyncio

async def get_html(sleep_times):
    print("==========start get url==========")
    await asyncio.sleep(sleep_times)
    print("==========end get url {}s==========".format(sleep_times))

if __name__ == '__main__':
    '''实现Ctrl+C停止任务'''
    task1=get_html(2)
    task2=get_html(1)
    task3=get_html(3)
    tasks=[task1,task2,task3]
    loop=asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:              #按Ctrl+C时触发取消任务
        all_tasks=asyncio.Task.all_tasks()      #获取所有的task
        for task in all_tasks:                  #取消所有的任务
            print("任务取消:",task.cancel())
        loop.stop()
        loop.run_forever()                      #不这么写抛异常
    finally:
        loop.close()