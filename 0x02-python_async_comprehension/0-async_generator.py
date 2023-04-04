#!/usr/bin/env python3
'''Async Generator to generates a sequence of 10 numbers
'''
import asyncio
import random
from typing import Generator
# Generator[yield_type, send_type, return_type]


async def async_generator() -> Generator[float, None, None]:
    '''Coroutine that prints a sequence of 10 random numbers using random module.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
