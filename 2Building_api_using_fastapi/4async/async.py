import time
from timeit import default_timer as timer
import asyncio


async def run_task(name, sec):

    print(f"{name} started at {timer()}")

    await asyncio.sleep(sec)
    print(f"{name} ended at {timer()}")


async def main():

    start = timer()
    await asyncio.gather(
        run_task("task1", 2), run_task("task2", 1), run_task("task3", 3)
    )

    print(f"Total time taken is {timer() - start:.2f}")


asyncio.run(main())
