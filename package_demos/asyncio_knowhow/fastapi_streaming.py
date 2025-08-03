from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def sse_generator():
    counter = 1
    while counter < 10:
        yield f"data: Event {counter}\n\n"
        counter += 1
        await asyncio.sleep(2)  # simulate pushing data every 2 seconds

# cmd: fastapi dev fastapi_streaming.py
@app.get('/sse')
async def sse_endpoint():
    return StreamingResponse(sse_generator(), media_type='text/event-stream')
