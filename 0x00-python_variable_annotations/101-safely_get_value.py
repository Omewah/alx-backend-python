#!/usr/bin/env python3
"""A script that returns the default values for a dictionary"""

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Using a key to retrieve the default value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
