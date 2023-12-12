#!/usr/bin/env python3
"""
Basic Async Script
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
