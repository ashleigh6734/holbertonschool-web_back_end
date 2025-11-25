#!/usr/bin/env python3

"""
Module for 0-async_generator.py
"""


import asyncio


async def async_generator():
    """
    Asynchronous generator that yields numbers 0 to 9 with a 1 second delay.

    Yields:
        int: The next number in the sequence from 0 to 9.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield i
