#!/usr/bin/env python3
"""Async Comprehension with Python"""

from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes asyn comprehension 4x and measures the total runtime"""
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
