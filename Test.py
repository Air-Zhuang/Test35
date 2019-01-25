import asyncio
import aiomysql

async def db_setup(app, loop):
    pool = await aiomysql.create_pool(**app.config['MYSQL'],loop=loop)
    print("mysql start successfully")       #初始化aiomysql
    return pool

async def setup_db(app, loop):
    app.db = await db_setup(app, loop)

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(setup_db())