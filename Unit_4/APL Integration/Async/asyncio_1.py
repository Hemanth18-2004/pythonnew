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
