#!/usr/bin/env python3
"""mixed list with annotations"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of mixed list in annotation"""
    return sum(mxd_lst)
