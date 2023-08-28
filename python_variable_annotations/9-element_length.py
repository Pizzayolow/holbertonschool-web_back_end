#!/usr/bin/env python3
"""duck type"""
from typing import Union, List, Dict, Tuple, Callable, Sequence, Iterable


def element_lenght(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck from an iterable"""
    return [(i, len(i)) for i in lst]
