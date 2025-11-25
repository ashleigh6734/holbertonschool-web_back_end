#!/usr/bin/env python3

import asyncio
import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator

async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, waits 1 second each time asynchronously,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
