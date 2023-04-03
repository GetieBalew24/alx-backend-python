#!/usr/bin/env python3
'''Task 0.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay of number between 0 and 10
    using asynchronous coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
