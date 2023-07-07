#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""Function to give element length"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns parameters"""
    return [(i, len(i)) for i in lst]
  
