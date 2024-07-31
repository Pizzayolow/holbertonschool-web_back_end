#!/usr/bin/env python3
from typing import Union
"""to kv with annotations"""


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """to kv with annotations"""
    return k, v*v