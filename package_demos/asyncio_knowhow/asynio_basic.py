import asyncio
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.high:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        self.current += 1
        return self.current-1

async def main():
    async for num in Counter(1, 4):
        print(num)  # prints 1, 2, 3 at 1-second intervals

if __name__ == "__main__":
    asyncio.run(main())

