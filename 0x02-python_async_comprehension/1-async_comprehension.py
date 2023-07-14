#!/usr/bin/env python3
"""Collects 10 random numbers using an async comprehensing/async_generator"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehensing"""
    return [number async for number in async_generator()]
