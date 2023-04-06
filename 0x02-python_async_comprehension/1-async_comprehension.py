#!/usr/bin/env python3
'''Async Comprehensions to Creates a list of 10 numbers
'''
from typing import List
from importlib import import_module as find


async_generator = find('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' collect 10 random numbers using async comprehensing
    over async_generator and return the 10 random number
    '''
    rand_nums = [nums async for nums in async_generator()]
    return rand_nums[:10]
