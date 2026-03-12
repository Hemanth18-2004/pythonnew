import asyncio
import time

async def Job(name, delay):
    start = time.time()
    print(f'Job {name} started')
    await asyncio.sleep(delay)
    end = time.time()
    tt = round(end-start, 2)
    print(f'Job {name} executed in {tt} seconds')
    return name, tt
