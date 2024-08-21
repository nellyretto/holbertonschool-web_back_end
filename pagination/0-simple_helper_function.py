#!/usr/bin/env python3


from typing import Tuple


def index_range(page, page_size) -> Tuple:
    """
    Returns the start and end index of a given page in a pagination system.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index of the page.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 10)
        (10, 20)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
