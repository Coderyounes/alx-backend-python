#!/usr/bin/env python3
""" Documentation """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the runtime of the wait_n function.

    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int): The maximum delay
        for each call to the wait_n function.

    Returns:
        float: The average runtime of the wait_n function.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
