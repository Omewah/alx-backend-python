#!/usr/bin/env python3
"""Async Comprehension with Python"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random num and return 10 random num using async comp"""
    return [number async for number in async_generator()]
