import asyncio
import time
''' Define a coroutine'''
async def Task(name, delay):
    print(f"Task {name} started execution at {time.strftime('%H:%M:%S')}")
    await asyncio.sleep(10)
    ''' Coroutine is paused for 10 seconds
        Control is returned to the event loop during the delay'''
    end_t = time.strftime('%H:%M:%S')
    print(f'Task {name} completed execution at {end_t}')
    return name, end_t
'''Coroutine execution is coordinated here'''
async def main():
    results = await asyncio.gather(
        Task('A', 3),
        Task('B', 0.5),
        Task('C', 2)
    )
    print('Complete Summary Report')
    for name, t in results:
        print(f"Task {name} completed at {t:.2f} seconds")
    asyncio.run(main())
