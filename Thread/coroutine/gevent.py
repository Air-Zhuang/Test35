'''
gevent和asyncio
https://www.aliyun.com/jiaocheng/444330.html
之前是没有选择,很多人选择了Gevent,而现在明确的有了更正统的、正确的选择:asyncio。所以建议大家放弃Gevent,拥抱asyncio。
'''

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
