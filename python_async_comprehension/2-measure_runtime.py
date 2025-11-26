#!/usr/bin/env python3
"""Module for async Comprehensions"""
import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that runs async_comprehension four times in parallel
    using asyncio.gather, measures total runtime, and returns it.
    """
    start = time.perf_counter()

    # Run four async_comprehension coroutines concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end = time.perf_counter()
    return end - start
