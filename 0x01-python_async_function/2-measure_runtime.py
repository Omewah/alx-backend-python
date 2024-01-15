#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures and returns the total execution time of wait_n"""
    timestart = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - timestart
    return total_time / n
