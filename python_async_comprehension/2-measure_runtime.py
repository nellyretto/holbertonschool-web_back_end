#!/usr/bin/env python3

"""
Measures the runtime of concurrently executing the async_comprehension
function four times.

Imports:
    - asyncio: For asynchronous programming with coroutines.
    - time: To measure elapsed time.
    - async_comprehension: Imported from '1-async_comprehension', it's an
    asynchronous function to be timed.

Function:
    - measure_runtime: Asynchronously calculates and returns the time
    taken to run async_comprehension four times concurrently.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time to execute async_comprehension four times concurrently.

    Records the start and end times, then returns the elapsed time in seconds.
    """

    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()

    return end_time - start_time
