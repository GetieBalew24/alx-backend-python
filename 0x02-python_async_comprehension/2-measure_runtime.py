#!/usr/bin/env python3
'''Task 2 Executes async_comprehension 4 times
'''
import asyncio
import time
from importlib import import_module as find


async_comprehension = find('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures the  total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
