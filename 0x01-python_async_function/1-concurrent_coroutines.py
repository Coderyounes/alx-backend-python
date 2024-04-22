#!/usr/bin/env python3
""" Documentation """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay (included)
    n times, and returns a list of the resulting delay times.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay time.

    Returns:
        List[float]: A list of the resulting delay times.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
