#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import importlib
import time


async_comprehension = importlib.import_module(
    "1-async_comprehension"
).async_comprehension


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: time taken to execute 4 coroutines asynchronously
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    elapsed = time.perf_counter() - start
    return elapsed

