import asyncio
import time


async def main():

    print("Tim")
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(0.5)

    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(10)


start = time.time()
asyncio.run(main())
print(time.time() - start)
