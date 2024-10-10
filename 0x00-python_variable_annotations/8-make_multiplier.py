#!/usr/bin/env python3
"""
8-make_multiplier.py
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    make_multiplier
    Args:
        multiplier (float): multiplier

    Returns:
        typing.Callable[[float], float]: function that takes a float and
                                         return the product of that float
                                         and the multiplier
    """
    return lambda x: x * multiplier
