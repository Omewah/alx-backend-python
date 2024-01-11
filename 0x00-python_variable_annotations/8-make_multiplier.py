#!/usr/bin/python3
"""A script that returns the multiplier of floats"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function takes float as arguments and returns their multiplier"""

    def multiplier_function(x: float) -> float:
        """The input of the float is multiplied by the multiplier"""
        return x * multiplier

    return multiplier_function
