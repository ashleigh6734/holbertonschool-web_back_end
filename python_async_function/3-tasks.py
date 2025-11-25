#!/usr/bin/env python3

"""
Docstring for python_async_function.3-tasks.py
"""


import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task that runs wait_random with the
    specified max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The created asyncio Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
