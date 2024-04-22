#!/usr/bin/env python3
""" Documentation """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task
    object that wraps the wait_random function.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task
        object representing the wrapped wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))
