import sniffio
import asyncio

# Fix for anyio.NoEventLoopError on Windows with Chainlit 2.x + uvicorn
# sniffio loses track of the running library when serving static files;
# this forces it to always report "asyncio" so anyio picks the right backend.
_original_current_async_library = sniffio.current_async_library

def _patched_current_async_library():
    try:
        return _original_current_async_library()
    except sniffio.AsyncLibraryNotFoundError:
        return "asyncio"

sniffio.current_async_library = _patched_current_async_library

import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    response = f"Received: {message.content}"
    await cl.Message(content=response).send()
