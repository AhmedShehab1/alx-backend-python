#!/usr/bin/env python3

"""
0-async_generator
"""
from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous Generator Function
    Yields:
        Iterator[AsyncGenerator[float, None]]: float
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

