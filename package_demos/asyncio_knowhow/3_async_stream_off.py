import asyncio
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

# Async function that sends a request and waits for the full response
async def stream_from_endpoint(client, endpoint_name, **kwargs):
    response = await client.chat.completions.create(**kwargs) # stream=False is default
    print(f"\nFrom {endpoint_name}:\n{response.choices[0].message.content}\n")

async def main():
    # Initialize async clients for different models and endpoints
    client_openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))   # OpenAI-hosted model
    client_mistral = AsyncOpenAI(  # GitHub-hosted Mistral model
        base_url="https://models.github.ai/inference",
        api_key=os.getenv("GITHUB_TOKEN")
    )
    client_grok = AsyncOpenAI(  # GitHub-hosted Grok model
        base_url="https://models.github.ai/inference",
        api_key=os.getenv("GITHUB_TOKEN")
    )

    # Define prompt parameters for each request
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
    
    # Run all API calls concurrently — each one awaits the full response before printing
    await asyncio.gather(
        stream_from_endpoint(client_grok, "GitHub Grok model", **params_grok),
        stream_from_endpoint(client_mistral, "GitHub Mistral model", **params_mistral),
        stream_from_endpoint(client_openai, "OpenAI GPT model", **params_openai)        
    )

if __name__ == "__main__":
    load_dotenv(override=True)  # Load API keys and env vars from .env file
    asyncio.run(main())
