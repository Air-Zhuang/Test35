'''
为什么用协程：
1、回调模式编码复杂度高
2、同步编程的并发性不高
3、多线程编程需要解决线程间同步,使用Lock会降低性能

协程可以使用单线程的编程模式,使一个线程在多个不同的函数中来回切换
协程(可以暂停的函数)
'''

'''
协程四个状态：
1、等待开始执行
2、解释器正在执行
3、在yield表达式处暂停
4、执行结束
'''

'''原生协程'''
# async def downloader(url):
#     return "air"
#
# async def download_url(url):
#     html=await downloader(url)
#     return html
#
# corn=download_url("https://www.baidu.com")
# corn.send(None)

'''gevent'''
import gevent
def foo(a,b):
    print("a=%d,b=%d" % (a,b))
    gevent.sleep(1)
    print("Running foo again")
def bar():
    print("Running int bar")
    gevent.sleep(2)
    print("Running bar again")

#生成协程
f=gevent.spawn(foo,1,2)
g=gevent.spawn(bar)
print('=====================')
gevent.joinall([f,g])
print('%%%%%%%%%%%%%%%%%%%%%')
