import asyncio
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
from collections.abc import AsyncIterator

# Asynchronously stream chunks as soon as they're available
async def stream_from_endpoint(client, endpoint_name, **kwargs):
    # Start streaming response (stream=True returns an async iterator)
    response = await client.chat.completions.create(stream=True, **kwargs) 
    print(f"From {endpoint_name}: Is Async Iterator?: {isinstance(response, AsyncIterator)} ")
    # Loop over streamed chunks as they arrive
    async for chunk in response:
        if chunk.choices and len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if delta and hasattr(delta, "content") and delta.content:
                print(f"[{endpoint_name}]:{delta.content} ", end="", flush=True)


async def main():
    # Set up async OpenAI clients for different endpoints/models
    client_openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))   # OpenAI-hosted model
    client_mistral = AsyncOpenAI(  # GitHub-hosted Mistral model
        base_url="https://models.github.ai/inference",
        api_key=os.getenv("GITHUB_TOKEN")
    )
    client_grok = AsyncOpenAI(  # GitHub-hosted Grok model
        base_url="https://models.github.ai/inference",
        api_key=os.getenv("GITHUB_TOKEN")
    )

    # Define prompts for each endpoint
    params_openai = {
        "model": "gpt-4.1-nano",
        "messages": [{"role": "user", "content": "Say 'double bubble bath' ten times."}]
    }
    params_mistral = {
        "model": "mistral-ai/mistral-medium-2505",
        "messages": [{"role": "user", "content": "Say 'deep blue sky, deliciously dreamy delights' five times"}]
    }
    params_grok = {
        "model": "xai/grok-3",
        "messages": [{"role": "user", "content": "Say 'glistening galaxies gracefully glide' seven times"}]
    }
    
    # Launch all streaming coroutines at once: responses will stream and print concurrently
    await asyncio.gather(
        stream_from_endpoint(client_grok, "GitHub Grok model", **params_grok),
        stream_from_endpoint(client_mistral, "GitHub Mistral model", **params_mistral),
        stream_from_endpoint(client_openai, "OpenAI GPT model", **params_openai)        
    )

if __name__ == "__main__":
    load_dotenv(override=True)  # Load API keys and env vars from .env file
    asyncio.run(main())
