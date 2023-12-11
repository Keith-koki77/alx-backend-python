#!/usr/bin/env python3

 """
    Measure the total execution time for wait_n(n, max_delay) and return total_time / n.

    Parameters:
    - n (int): Number of times to spawn wait_random.
    - max_delay (int): Maximum delay in seconds.

    Returns:
    - float: Average execution time per call.
"""
from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    return (end_time - start_time) / n
