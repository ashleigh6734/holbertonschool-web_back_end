#!/usr/bin/env python3

"""
Docstring for python_async_function.1-concurrent_coroutines.py
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order.
    
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each call.
        
    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = []
    # Create n coroutines/tasks
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = []
    # asyncio.as_completed yields the futures as they finish (not in order of submission)
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
