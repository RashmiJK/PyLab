from openai import OpenAI
import os
from dotenv import load_dotenv
import json

def chat_sync_stream_off():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # stream=False by default; returns full response at once
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": "Say 'double bubble bath' ten times."}],
    )
    print("Type:", type(response))  # Response object type
    print(json.dumps(response.model_dump(), indent=2))  # Full response as JSON
    print("AI:", response.choices[0].message.content)   # Generated message

if __name__ == "__main__":
    load_dotenv()
    chat_sync_stream_off()
