#!/usr/bin/env python3
"""to kv with annotations import Typing"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv with annotations"""
    return (k, v*v)
