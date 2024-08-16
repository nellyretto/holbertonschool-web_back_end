#!/usr/bin/env python3
"""
This module defines an asynchronous function `task_wait_n` that executes
multiple asynchronous tasks concurrently and returns a list of their
delays.

**Functions:**

    task_wait_n(n: int, max_delay: int) -> List[float]
        Spawns `n` tasks, each calling `task_wait_random` with a maximum
        delay of `max_delay` seconds. Waits for all tasks to complete
        and returns a list of the delays returned by each task.

**Dependencies:**

    typing: For type hinting.
    asyncio: For asynchronous programming.
    task_wait_random: An imported function from the '3-tasks' module.

**Usage:**

    To use this module, import the `task_wait_n` function and call it with
    the desired number of tasks and maximum delay.
"""

from typing import List
import asyncio

# Import task_wait_random from the '3-tasks' module
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` tasks, each calling `task_wait_random` with a maximum
    delay of `max_delay` seconds. Waits for all tasks to complete
    and returns a list of the delays returned by each task.

    Args:
        n: The number of tasks to spawn.
        max_delay: The maximum delay for each task in seconds.

    Returns:
        A list of the delays returned by each task.
    """

    tasks = []
    delays = []

    for _ in range(n):
        # Create a task and append it to the list of tasks
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Wait for all tasks to complete and gather their results
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
