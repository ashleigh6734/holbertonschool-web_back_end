#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of wait_n.
"""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): Number of coroutines to launch.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: The average time per task (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
