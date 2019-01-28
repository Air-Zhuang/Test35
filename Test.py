import asyncio
import aiohttp


async def fetch():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("https://www.instagram.com/explore/locations/?__a=1", data={'page': 1}, ssl=False) as resp:
                if resp.status in [200, 201]:
                    data = await resp.json()
                    print(data)
                else:
                    print(resp.status)
    except Exception as e:
        print("!!!!Exception:", e)


if __name__ == '__main__':
    loop=asyncio.get_event_loop()                               #定义事件循环
    loop.run_until_complete(fetch())  #类似多线程里面的join(),运行完指定的协程,关闭loop