#!/usr/bin/env python3

"""Import libraries for asynchronous
programming, random number generation, and type hinting
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """

    Returns:
        AsyncGenerator[float, None]: _description_

    Yields:
        Iterator[AsyncGenerator[float, None]]: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
