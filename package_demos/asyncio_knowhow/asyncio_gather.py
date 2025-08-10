import asyncio

async def say_after(delay, greeting_msg):
    await asyncio.sleep(delay)
    print(greeting_msg)

async def main():
    print("Start")
    # Schedule multiple coroutines concurrently
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World")
    )
    print("End")

if __name__ == "__main__":
    asyncio.run(main())