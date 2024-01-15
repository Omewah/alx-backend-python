#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay"""
    wait_delay = random.uniform(0, max_delay)
    await asyncio.sleep(wait_delay)
    return wait_delay
