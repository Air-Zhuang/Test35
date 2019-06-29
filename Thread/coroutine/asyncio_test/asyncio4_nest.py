import asyncio

async def compute(x,y):
    print("==========start compute==========")
    print("Compute %s + %s..." % (x,y))
    await asyncio.sleep(1)
    print("==========stop compute==========")
    return x+y

async def print_sum(x,y):
    print("==========start print_sum==========")
    #原理：return x+y执行完成之后抛出一个StopIteration,被await截获,使程序重新进入到print_sum()
    result=await compute(x,y)
    print("%s + %s = %s" % (x,y,result))
    print("==========stop print_sum==========")

if __name__ == '__main__':
    '''协程嵌套'''
    loop=asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1,2))
    loop.close()