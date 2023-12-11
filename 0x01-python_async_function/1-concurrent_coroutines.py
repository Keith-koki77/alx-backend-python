#!/usr/bin/env python3

"""
Asynchronous coroutine that spawns wait_random n times with the specified max_delay.
Parameters:
    - n (int): Number of times to spawn wait_random.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - List[float]: List of delays in ascending order.
"""

import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    queue, array = [], []
    for _ in range(n):
        queue.append(wait_random(max_delay))

    for i in asyncio.as_completed(queue):
        array.append(await i)
    return array
