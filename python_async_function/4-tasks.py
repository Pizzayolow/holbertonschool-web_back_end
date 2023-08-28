#!/usr/bin/env python3
"""basic async"""

import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return a asynchrone with gather"""
    coros = [wait_random(max_delay) for i in range(n)]
    list = await asyncio.gather(*coros)
    return sorted(list)
