#!/usr/bin/env python3
"""mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, str]]) -> float:
    """return the sum of a mixed list"""
    return sum(mxd_lst)
