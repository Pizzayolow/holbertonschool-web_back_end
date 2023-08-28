#!/usr/bin/env python3
"""return a tuple str and a squared of int or float"""
from typing import Union, List, Dict, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple str and a squared of int or float"""
    return(k, v*v)
