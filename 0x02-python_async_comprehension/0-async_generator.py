#!/usr/bin/env python3
'''Task 0 Async Generator to generates a sequence of 10 numbers using the random module
'''
import asyncio
import random
from typing import Generator
# Generator[yield_type, send_type, return_type]


async def async_generator() -> Generator[float, None, None]:
    '''Coroutine that generates a sequence of 10 numbers randmolyby pause its execution at certain points within 5 seconds.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
