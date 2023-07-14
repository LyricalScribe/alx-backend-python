#!/usr/bin/env python3
"""an async routine that takes in 2 int arguments"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine executes concurrently"""
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)

