#!/usr/bin/env python3
"""Function measures the total execution time"""

import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time() - start
    return total_time / n

