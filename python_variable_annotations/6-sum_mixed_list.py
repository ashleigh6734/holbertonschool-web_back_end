#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Provides a type-annotated function to sum a list containing integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats

    Returns:
        float: The sum of all numbers in mxd_lst
    """
    return float(sum(mxd_lst))
