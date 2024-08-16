#!/usr/bin/env python3


"""
This module provides a function to measure the average
execution time of
concurrent coroutines in a single run.

It imports the `wait_n` function from the module
`1-concurrent_coroutines.py`
(assumed location), which is likely responsible for
running coroutines concurrently
with a maximum delay between them.
"""

import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of n concurrently running coroutines.

    Args:
        n (int): The number of coroutines to run concurrently.
        max_delay (int): The maximum delay (in seconds) to introduce between
                         coroutine executions.

    Returns:
        float: The average execution time of the coroutines (in seconds).
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
