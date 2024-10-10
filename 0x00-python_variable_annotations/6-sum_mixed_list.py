#!/usr/bin/env python3
"""
6-sum_mixed_list.py
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float, int]]) -> float:
    """
    returns sum of mxd_lst as float
    Args:
        mxd_lst (typing.List[typing.Union[float, int]]): mxd_lst

    Returns:
        float: _description_
    """
    return sum(mxd_lst)
