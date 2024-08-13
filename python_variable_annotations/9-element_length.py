#!/usr/bin/env python3

"""
import for typing use
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given list.

    Args:
        lst (Iterable[Sequence]): The list of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains an element
        from the input list and its length.

    """
    return [(i, len(i)) for i in lst]
