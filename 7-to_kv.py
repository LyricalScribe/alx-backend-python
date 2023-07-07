#!/usr/bin/env python3
from typing import Union, Tuple
"""function to return a tuple"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, v ** 2)
  
