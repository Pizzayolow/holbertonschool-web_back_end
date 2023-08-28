#!/usr/bin/env python3
"""measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)"""
import asyncio
import random
import time
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)"""

    async def async_measure():
        """A asynchronous function"""
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        return (end_time - start_time) / n

    return asyncio.run(async_measure())
