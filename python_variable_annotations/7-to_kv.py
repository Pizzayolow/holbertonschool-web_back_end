#!/usr/bin/env python3
from typing import Union, Tuple
"""to kv with annotations import Typing"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv with annotations"""
    return (k, v*v)
