
import time
import asyncio

async def abc():
    asyncio.sleep(2)
    print('haha')

async def bcd():
    print('afafafafa')

loop = asyncio.get_event_loop()
begin = time.time()
loop.run_until_complete(asyncio.wait([abc(),bcd()]))
end = time.time()
print('spend time:{}'.format(end-begin))