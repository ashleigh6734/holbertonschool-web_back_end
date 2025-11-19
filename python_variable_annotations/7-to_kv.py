#!/usr/bin/env python3
"""
Module 7-to_kv
returns a tuple with a string and the square of a number.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string and the second
    element is the square of an int or float, represented as a float.

    Args:
        k (str): The string key
        v (Union[int, float]): The integer or float value

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of v
    """
    return (k, float(v ** 2))
