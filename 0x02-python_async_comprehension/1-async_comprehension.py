#!/usr/bin/env python3

"""
1-async_comprehension
"""
from typing import List
import importlib

async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random floats using async comprehensing
    Returns:
        AsyncGenerator[List, None]: list of floats
    """
    return [rand_num async for rand_num in async_generator()]
