#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import importlib
import time


wait_n = importlib.import_module('1-concurrency_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures total execution time for wait_n coroutine
    Args:
        n (int): number of spawns
        max_delay (int): Maximum Delay

    Returns:
        float: total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
