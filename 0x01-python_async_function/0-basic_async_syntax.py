#!/usr/bin/env python3
"""async coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    """async coroutine that takes in an integer argument"""
    await asyncio.sleep(delay)
    return delay
