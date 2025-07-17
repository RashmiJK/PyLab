#! /usr/bin/env python3

import asyncio

async def countonetwo():
    print("One")
    await asyncio.sleep(3)
    print("Two")

async def countthreefour():
    print("Three")
    await asyncio.sleep(1)
    print("four")

async def countfivesix():
    print("Five")
    await asyncio.sleep(2)
    print("Six")


async def main():
    # Instead of asyncio.gather, if w use await for each function call,
    # the functions will run sequentially, not concurrently.
    await asyncio.gather(countonetwo(), countthreefour(), countfivesix())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    e = time.perf_counter()
    print(f"{__file__} executed in {e - s:.2f} seconds")