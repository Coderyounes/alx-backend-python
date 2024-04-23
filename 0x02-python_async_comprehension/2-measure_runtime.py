#!/usr/bin/env python3
""" Documentation """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension
    function by running it 4 times concurrently.

    Returns:
        The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
