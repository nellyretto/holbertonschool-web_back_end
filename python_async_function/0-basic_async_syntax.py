#!/usr/bin/env python3

"""
Module for generating random delays.

Provides a coroutine to wait for a random delay between 0
and a specified maximum.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Waits for a random delay between 0 and max_delay seconds
    and returns the delay.

    Args:
      max_delay: The maximum delay in seconds. Defaults to 10.

    Returns:
      The actual delay in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
