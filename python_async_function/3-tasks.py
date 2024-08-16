#!/usr/bin/env python3

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random

"""
Imports the `wait_random` function from the module '0-basic_async_syntax'.
This function is assumed to be defined in a separate file and
returns a random delay.
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Defines an asynchronous task that calls the `wait_random` function.

    Args:
        max_delay (int): The maximum delay in seconds for
        the `wait_random` function.

    Returns:
        asyncio.Task: An asyncio Task object representing the
        asynchronous operation.

    This function creates an asyncio Task object that executes
    the `wait_random` function
    with the given `max_delay`. The `wait_random` function is
    expected to return a random
    delay within the specified maximum.
    """
    return asyncio.create_task(wait_random(max_delay))
