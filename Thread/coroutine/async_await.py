'''
为什么用协程：
1、回调模式编码复杂度高
2、同步编程的并发性不高
3、多线程编程需要解决线程间同步,使用Lock会降低性能

协程可以使用单线程的编程模式,使一个线程在多个不同的函数中来回切换
协程(可以暂停的函数)
'''

'''原生协程'''
async def downloader(url):
    return "air"

async def download_url(url):
    html=await downloader(url)
    return html

corn=download_url("https://www.baidu.com")
corn.send(None)
