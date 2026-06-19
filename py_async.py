import asyncio

async def wait_for_time(time):
    await asyncio.sleep(time)

asyncio.run(wait_for_time(3))