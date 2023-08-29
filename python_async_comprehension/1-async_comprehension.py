#!/usr/bin/env python3
"""async comprehension"""

import asyncio
import random
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """return a generator with async generator function"""
    return [i async for i in async_generator()]
