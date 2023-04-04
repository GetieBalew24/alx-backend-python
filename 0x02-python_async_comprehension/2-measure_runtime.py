#!/usr/bin/env python3
''' Run time for four parallel comprehensions
    execute async_comprehension four times in 
    parallel using asyncio.gather
'''
import asyncio
import time
from importlib import import_module as find


async_comprehension = find('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Run time for four parallel comprehensions to Executes 
        async_comprehension 4 times & measures the total execution time.
    '''
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
