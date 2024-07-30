#!/usr/bin/env python3
"""sum of list in annotation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list in annotation"""
    total: int = 0
    for num in input_list:
        total += num
    return total