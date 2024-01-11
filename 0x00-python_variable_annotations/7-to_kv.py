#!/usr/bin/python3
"""A script that returns tuples from strings/floats"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function takes string/float as arguments and returns the tuple"""
    return k, float(v ** 2)
