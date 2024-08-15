#!/usr/bin/env python3

"""
Module containing the `wait_n` coroutine.

This module provides an asynchronous coroutine named `wait_n` that spawns
multiple instances of the `wait_random` coroutine (imported from the
`0-basic_async_syntax` module) and returns a list of their respective delays
in ascending order.
"""

from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with specified max_delay.

    Returns a list of the delays (float values) in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of the delays in ascending order.
    """

    tasks = []
    delays = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
