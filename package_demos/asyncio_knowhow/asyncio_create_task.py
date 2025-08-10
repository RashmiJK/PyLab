import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    # Create tasks to run concurrently
    task1 = asyncio.create_task(say_after(2, "Hello"))
    task2 = asyncio.create_task(say_after(1, "World"))

    print("Tasks started")
    # Do other things here while the tasks run...

    # Await the tasks to get their result (wait until they finish)
    #await task1
    #await task2
    print("Both tasks finished")
    await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())