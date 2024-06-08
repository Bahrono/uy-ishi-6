import asyncio
import time
from datetime import datetime


async def asyncio_task(id):
    print(f'Asyncio Task {id} started at {datetime.now().time()}')
    await asyncio.sleep(1)
    print(f'Asyncio Task {id} completed at {datetime.now().time()}')

async def main_asyncio():
    tasks = []
    for i in range(8):
        tasks.append(asyncio.create_task(asyncio_task(i)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main_asyncio())
    print(f'All asyncio tasks completed in {time.time() - start_time} seconds')



async def async_task(id):
    print(f'Async Task {id} started at {datetime.now().time()}')
    await asyncio.sleep(1)
    print(f'Async Task {id} completed at {datetime.now().time()}')

async def main_async():
    tasks = []
    for i in range(8):
        tasks.append(async_task(i))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main_async())
    print(f'All async tasks completed in {time.time() - start_time} seconds')
