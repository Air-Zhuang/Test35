import asyncio
from functools import partial

async def get_html(url):
    print("==========start get url==========")
    await asyncio.sleep(1)
    print("==========end get url==========")
    return "air"

def callback_email(message,future):
    '''add_done_callback()返回一个future类型，所以必须有future这个参数'''
    print(message)

if __name__ == '__main__':
    '''获取返回值'''
    loop=asyncio.get_event_loop()
    task=asyncio.ensure_future(get_html("https://www.baidu.com"))       #将协程扔进loop
    # task=loop.create_task(get_html("https://www.baidu.com"))          #两种方式效果一样
    task.add_done_callback(partial(callback_email,"send a email"))      #设置函数运行完成时触发的回调函数
    loop.run_until_complete(task)       #join()
    print(task.result())                #返回值,必须在run_until_complete之后
