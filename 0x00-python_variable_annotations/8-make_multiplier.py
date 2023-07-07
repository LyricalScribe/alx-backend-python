#!/usr/bin/env python3
from typing import Callable
"""Function takes and return a function"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
  
