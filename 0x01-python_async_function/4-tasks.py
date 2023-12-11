#!/usr/bin/env python3
"""More into tasks"""
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    delay_list, an_list = [], []
    for i in range(n):
        delay_task = task_wait_random(max_delay)
        delay_task.add_done_callback(lambda x: delay_list.append(x.result()))
        an_list.append(delay_task)
    for an in an_list:
        await an
    return delay_list
