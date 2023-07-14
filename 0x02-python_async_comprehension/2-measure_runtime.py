#!/usr/bin/env python3
"""Execute async_comprehension asychronously"""


from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime and returns it"""
    start = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time() - start
