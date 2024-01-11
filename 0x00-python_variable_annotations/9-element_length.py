#!/usr/bin/env python3
"""A script that returns tuples of lists arguments"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """function takes list as arguments and returns their tuple"""
    return [(i, len(i)) for i in lst]
