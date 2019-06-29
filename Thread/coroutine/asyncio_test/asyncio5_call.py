import asyncio

def callback_func(sleep_times):
    print("sleep {} times".format(sleep_times))

def stoploop(loop):
    loop.stop()

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.call_later(2,callback_func,"later 2")          #延迟两秒执行
    loop.call_later(1,callback_func,"later 1")
    loop.call_later(3,callback_func,"later 3")
    loop.call_soon(callback_func,"soon")                #即刻执行
    now=loop.time()
    loop.call_at(now+3,callback_func,"at")              #指定时间执行,这里的时间是loop时间

    loop.call_later(5,stoploop,loop)                    #停止loop

    loop.run_forever()                                  #因为不是协程,所以不能用run_until_complete