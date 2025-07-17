import asyncio
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI  # hypothetical import for AsyncOpenAI client

async def stream_from_endpoint(client, endpoint_name, **kwargs):
    print(f"Start streaming from {endpoint_name}")
    stream = await client.chat.completions.create(stream=True, **kwargs)
    async for chunk in stream:
        print(f"[{endpoint_name}]: {chunk.choices[0].delta.content}", end='', flush=True)
    print(f"\nDone streaming from {endpoint_name}")

async def main():
    client1 = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))  
    client2 = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # Define parameters for both endpoints as needed
    params1 = {"model": "gpt-4o", "messages": [{"role": "user", "content": "What's the weather?"}]}
    params2 = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Tell me a joke."}]}
    
    # Run both streaming coroutines concurrently
    await asyncio.gather(
        stream_from_endpoint(client1, "endpoint1", **params1),
        stream_from_endpoint(client2, "endpoint2", **params2)
    )

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    asyncio.run(main())
