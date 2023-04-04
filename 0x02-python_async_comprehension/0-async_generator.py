#!/usr/bin/env python3
""" Task 0 Async Generator to generate a sequence of 10 random numbers.
    The coroutine will loop 10 times
    each time asynchronously wait 1 second,then yield a random number between 0 and 10.
    Use the random module.
"""
import asyncio
import random
from typing import Generator
# Generator[yield_type, send_type, return_type]


async def async_generator() -> Generator[float, None, None]:
    """ a coroutine that generates a sequence of 10 numbers using random function.
         pause its execution at certain points within 5 sceconds, save its current state
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
