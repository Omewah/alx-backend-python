#!/usr/bin/env python3
"""A script that returns a mixed list as the sum of floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function takes mixed list as arguments and returns their sum"""
    return sum(mxd_lst)
