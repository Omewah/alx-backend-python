#!/usr/bin/env python3
"""A script that returns tuples of lists arguments"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function takes list as arguments and returns their tuple"""
    return [(i, len(i)) for i in lst]
