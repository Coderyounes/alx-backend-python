#!/usr/bin/env python3

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of results from multiple tasks
    that wait for a random amount of time.

    Args:
        max_delay (int): The maximum delay in seconds for each task.

    Returns:
        List: A list of results from the completed tasks.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
