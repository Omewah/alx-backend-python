#!/usr/bin/env python3
"""Async Comprehension Python with Python"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random number after looping 10x"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
