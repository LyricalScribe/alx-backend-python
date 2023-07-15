#!/usr/bin/env python3
"""async_generator that takes no arguments"""

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Coroutine will loop 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
