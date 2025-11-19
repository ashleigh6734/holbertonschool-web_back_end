#!/usr/bin/env python3
"""
Module 8-make_multiplier
Provides a type-annotated function that returns a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and multiplier
    """
    def multiplier_function(x: float) -> float:
        """Multiply x by multiplier and return the result."""
        return x * multiplier

    return multiplier_function
