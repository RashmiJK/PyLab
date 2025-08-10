import inspect
import asyncio

# Define a coroutine using async def
async def greet():
    print("Hello")

if __name__ == "__main__":
    # Check if greet is a coroutine function
    print(inspect.iscoroutinefunction(greet)) 

    # Call the function to get a coroutine object
    cor_obj = greet()

    # Check if the object is a coroutine
    print(inspect.iscoroutine(cor_obj))

    # Actually run the coroutine
    asyncio.run(cor_obj)