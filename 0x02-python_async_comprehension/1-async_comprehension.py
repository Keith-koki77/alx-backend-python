#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers
using async
"""

import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension():
    return [i async for i in async_generator()]
