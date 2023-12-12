#!/usr/bin/env python3
"""
Run time using using asynco.gather
"""


from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time()
    task = [async_comprehension() for i in range(4)]
    await gather(*task)
    end_time = time()
    return end_time - start_time
