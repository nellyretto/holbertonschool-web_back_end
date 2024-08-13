#!/usr/bin/env python3
"""
import for Callable use
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """Create a multiplier function.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the result of multiplying it by the multiplier.

    """
    def multipllication(x: float) -> float:
        return x * multiplier
    return multipllication
