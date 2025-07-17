# Asynchronous IO (async IO)
* async/await: are keywords in Python that are used to define coroutines
async def
The await keyword can only be used inside an async def function.
asyncio.sleep()
asyncio.gather()

* asyncio: the Python package that provides a foundation and API for running and managing 

* coroutines: a special function that can pause and resume its execution, allowing other code to run during the pause. In Python, coroutines are defined with `async def` and are used for asynchronous programming.

* how are generator related to coroutines?

<br>
Concurrency  
Parallelism  
threads
<br>

![](images/async_paradigm.png)

1. What are generators in python? Generator comprehension.
2. What are coroutines and how are they related to generators?
a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time