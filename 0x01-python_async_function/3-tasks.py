#!/usr/bin/env python3
"""
3-tasks
"""
import asyncio
import importlib


wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns a asyncio.Task
    Args:
        max_delay (int): Max delay

    Returns:
        asyncio.Task: asyncio Task
    """
    return asyncio.Task(wait_random(max_delay))
