
import asyncio

async def worker():
    asyncio.sleep(2)
    print('worker job')
    return 10

def task_callback(future):
    print('task_callback')
    print('result:{}'.format(future.result()))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print('after create loop')
    task = loop.create_task(worker())
    print('after create task')
    task.add_done_callback(task_callback)
    print('after add done callback')
    loop.run_until_complete(task)
    print('finished')