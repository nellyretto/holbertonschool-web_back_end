#!/usr/bin/env python3

"""
importing for floor
"""
import math
"""
2. Basic annotations - floor
"""


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to a given number.

    Args:
        n (float): The number to be rounded down.

    Returns:
        float: The largest integer less than or equal to `n`.
    """
    return math.floor(n)
