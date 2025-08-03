import os
from openai import OpenAI
from dotenv import load_dotenv
from collections.abc import Iterator
from types import GeneratorType
import json

def chat_sync_stream_on():    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Make a chat request with streaming enabled
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": "Say 'double bubble bath' ten times."}],
        stream=True
    )

    # Check object type and streaming behavior
    print("type:", type(response),
          "| Is Generator?", isinstance(response, GeneratorType),
          "| Is Iterator?", isinstance(response, Iterator), "\n")

    # The response is a custom iterator
    # We can fetch chunks using next() one by one:
    print(response.__next__().choices[0].delta.content)
    print(response.__next__().choices[0].delta.content)
    print(response.__next__().choices[0].delta.content)
    print(response.__next__().choices[0].delta.content)

    # Or loop through remaining streamed chunks using a for-loop
    for event in response:
        print("****" * 20)
        print("Type of chunk:", type(event))
        print("Raw JSON chunk:\n", json.dumps(event.model_dump(), indent=2))
        print("----" * 20)

        if event.choices[0].delta.content:
            print(event.choices[0].delta.content, flush=True)

if __name__ == "__main__":
    load_dotenv()
    chat_sync_stream_on()
