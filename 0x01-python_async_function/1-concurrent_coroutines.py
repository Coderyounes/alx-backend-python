#!/usr/bin/env python3
""" Documentation """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for random delays and returns a sorted list of the delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: A sorted list of the delays.
    """
    alldelays = []
    for _ in range(n):
        data = await wait_random(max_delay)
        alldelays.append(data)
    return sorted(alldelays)
