#!/usr/bin/env python3
"""make a multiplier"""
from typing import Union, List, Dict, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return multiplier*multiplier"""
    def multi(x: float):
        """return a square"""
        return x*multiplier
    return multi
