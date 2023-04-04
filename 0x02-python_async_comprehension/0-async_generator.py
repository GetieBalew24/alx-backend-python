#!/usr/bin/env python3
''' Task 0 Async Generatory
    The coroutine will loop 10 times
    each time asynchronously wait 1 second,then yield a random number between 0 and 10.
    Use the random module.
'''
import asyncio
import random
from typing import Generator
# Generator[yield_type, send_type, return_type]


async def async_generator() -> Generator[float, None, None]:
    ''' Coroutine that generates a sequence of 10 numbers.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
