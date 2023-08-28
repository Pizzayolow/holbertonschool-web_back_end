#!/usr/bin/env python3
"""kv"""
from typing import Union, List, Dict, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return(k, v*v)
