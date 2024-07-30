#!/usr/bin/env python3
"""sum of list in annotation"""


def sum_list(input_list: list) -> float:
    """sum of list in annotation"""
    total: int = 0
    for num in input_list:
        total += num
    return total