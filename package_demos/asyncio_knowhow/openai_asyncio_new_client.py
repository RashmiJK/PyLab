import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
from types import GeneratorType
from collections.abc import Iterator, AsyncIterator, AsyncGenerator
import inspect

async def main() -> None:
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = await client.responses.create(
        model="gpt-4o", 
        input="Hello.",
        stream=True
    )
    print(
        "typeof(response):", type(response), "\n",
        " Is Generator: ", isinstance(response, GeneratorType), "\n",
        " Is Iterator: ", isinstance(response, Iterator), "\n",
        "Is awaitable : ", inspect.isawaitable(response),"\n",
        "Is async gen :",inspect.isasyncgen(response),"\n",
        "Is async gen function",inspect.isasyncgenfunction(response), "\n",    
        "Is Async Iterator: ",isinstance(response, AsyncIterator), "\n",
        "Is Async Generator: ",isinstance(response, AsyncGenerator), "\n" 
        )
    #async for event in response:
    #    print(event)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())