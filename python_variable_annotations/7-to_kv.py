#!/usr/bin/env python3

"""
import for Union and Tuple use


"""
from typing import Union, Tuple

OR = Union[int, float]


def to_kv(k: str, v: OR) -> Tuple[str, float]:

    """
    Convert the given key-value pair to a tuple.

    Args:
        k (str): The key.
        v (OR): The value.

    Returns:
        Tuple[str, float]: A tuple containing the key and the value.

    """
    return k, v
