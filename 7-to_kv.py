#!/usr/bin/env python3
"""
7-to_kv.py
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    returns a tuple
    Args:
        k (str): string k
        v (typing.Union[int, float]): number v

    Returns:
        typing.Tuple[str, float]: tuple
    """
    return (k, v)
