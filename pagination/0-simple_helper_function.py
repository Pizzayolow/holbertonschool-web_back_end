#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    '''return a tuple with start and end size'''
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)
