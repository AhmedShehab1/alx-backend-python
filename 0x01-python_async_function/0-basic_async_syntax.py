#!/usr/bin/env python3
"""
0-basic_async_syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Simple Asynchronous Coroutine
    Args:
        max_delay (int, optional): Maximum Delay. Defaults to 10.

    Returns:
        float: Random float Value between 0 and max_delay
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
