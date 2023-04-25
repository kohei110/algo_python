# https://qiita.com/maueki/items/8f1e190681682ea11c98

import asyncio
import time

async def hello_world(n):
    time.sleep(1)
    print("{}: hello world".format(n))

async def call_hello_world1():
    print('first_hello_world 1')
    await hello_world(1)

async def call_hello_world2():
    print('first_hello_world 2')
    await hello_world(2)

loop = asyncio.get_event_loop()
loop.create_task(call_hello_world1())
loop.run_until_complete(call_hello_world2())