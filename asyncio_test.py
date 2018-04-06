import asyncio
import time

async def sub():
    n = 1
    for i in range(1,100):
        n *= i
    time.sleep(3)
    return n

async def uper():
    res = await sub()
    print(res)

if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(uper())
    t2 = time.time()
    print(t2-t1)

