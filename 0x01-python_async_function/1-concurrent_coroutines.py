#!/usr/bin/env python3
"""
1-concurrency_coroutines
"""
import asyncio
import importlib
import typing


wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    spawns wait_random n times with the specified max_delay
    Args:
        n (int): number of spawns
        max_delay (int): Maximum Delay

    Returns:
        typing.List[float]: contains the float values returned by wait_random
    """
    res = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return res
