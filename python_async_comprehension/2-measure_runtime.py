#!/usr/bin/env python3
"""measure time between gathers"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure time"""
    n = 4
    start_time = time.time()
    coros = [async_comprehension() for i in range(n)]
    await asyncio.gather(*coros)
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time)
