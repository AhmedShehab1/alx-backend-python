#!/usr/bin/env python3
"""
4-tasks
"""
import asyncio
import importlib
import typing


task_wait_random = importlib.import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    spawns wait_random n times with the specified max_delay
    Args:
        n (int): number of spawns
        max_delay (int): Maximum Delay

    Returns:
        typing.List[float]: contains the float values returned by wait_random
    """
    res = await asyncio.gather(
                            *(task_wait_random(max_delay) for _ in range(n))
                            )
    return res
