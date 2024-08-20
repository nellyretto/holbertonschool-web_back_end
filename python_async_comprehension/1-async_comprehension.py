#!/usr/bin/env python3

"""Import the asyncio library for asynchronous programming"""

import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator

"""Return a list of floats generated asynchronously"""


async def async_comprehension() -> List[float]:
    return [num async for num in async_generator()]
