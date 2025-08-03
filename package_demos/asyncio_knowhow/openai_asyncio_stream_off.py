from openai import AsyncOpenAI
import os
import asyncio
from dotenv import load_dotenv

async def main():
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = await client.chat.completions.create(
        model = "gpt-4.1-nano",
        messages=[{"role":"user", "content":"Hello!"}],
    ) # stream is not set; default is false
    print(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    asyncio.run(main())