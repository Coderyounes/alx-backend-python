#!/usr/bin/env python3
""" Documentation"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    nums = []
    async for i in async_generator():
        nums.append(i)
    return nums
