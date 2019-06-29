'''
Lock:
    协程因为是单线程，所以一般不需要加锁，但是有需要锁的情况。
    比如下面，当parse_stuff调用get_stuff的时候不希望use_stuff也调用get_stuff。所以可以用asyncio.Lock来实现
'''

from asyncio import Lock
import aiohttp

cache={}
lock=Lock()     #定义锁

async def get_stuff(url):
    async with lock:            #加锁
        if url in cache:
            return cache[url]
        stuff=await aiohttp.request("GET",url)
        cache[url]=stuff
        return stuff

async def parse_stuff():
    stuff=await get_stuff()

async def use_stuff():
    stuff=await get_stuff()
