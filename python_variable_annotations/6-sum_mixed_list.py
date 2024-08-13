#!/usr/bin/env python3


"""import form List use

Returns:
    _type_: _description_
"""

from typing import Union, List

mix = Union[int, float]


def sum_mixed_list(mxd_lst: List[mix]) -> float:

    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[int, float]): A list containing integers and floats.

    Returns:
        float: The sum of the elements in the mixed list.

    Examples:
        >>> sum_mixed_list([1, 2, 3.5, 4.2])
        10.7
        >>> sum_mixed_list([5, 6, 7])
        18.0
    """
    return sum(mxd_lst)
