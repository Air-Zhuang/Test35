import asyncio
import aiohttp
import aiomysql
import re
from pyquery import PyQuery

stopping=False
waitting_queue=asyncio.Queue()
seen_urls=set()

async def fetch_http(url,session,method):
    try:
        async with session.get(url) as resp:
            if resp.status in [200,201]:
                if method=="json":
                    data = await resp.json()
                    return data
                else:
                    data = await resp.text()
                    return data
    except Exception as e:
        print("!!!!Exception:",e)

'''获取详情,每0.5秒取一个url爬取详情页'''
async def article_handler(url,session,pool):
    html=await fetch_http(url,session,"text")
    seen_urls.add(url)
    pq=PyQuery(html)
    title=pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql="insert into chaping_table(post_url,reason) values('{}','{}')".format(url,title)
            await cur.execute(insert_sql)

async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            url=await waitting_queue.get()
            print("parse:{}".format(url))
            if url.startswith('https://mjzj.com'):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url,session,pool))
                    await asyncio.sleep(0.5)
            waitting_queue.task_done()

'''获取url,每4秒爬一次接口页,添加到待爬取队列'''
def extract_url(s):
    ma = re.search(r'data-detatil-url="(.*?)"><', s)
    return ma.group(1)

async def extract_urls(url,session):
    original_url_list =await fetch_http(url,session,"json")
    print("len:",len(original_url_list))
    for i in range(len(original_url_list)):
        waitting_queue.put_nowait(extract_url(original_url_list[i]))
    await asyncio.sleep(4)

async def gene_urls(start_page):
    page=start_page
    start_url = "https://mjzj.com/web-api/reviewer-exposure/views?page=" + str(page) + "&market=美国"
    async with aiohttp.ClientSession() as session:
        await extract_urls(start_url,session)
    await gene_urls(start_page+1)

'''启动函数'''
async def main(loop):
    pool=await aiomysql.create_pool(host='127.0.0.1',port=3306,user='root',password='123456',db='chaping',loop=loop,charset='utf8',autocommit=True)

    asyncio.ensure_future(gene_urls(1))
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()