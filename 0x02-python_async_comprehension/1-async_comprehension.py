#!/usr/bin/env python3
""" Documentation"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async function that generates a list of floats using async comprehension.

    Returns:
        List[float]: A list of floats generated using async comprehension.
    """
    return [num async for num in async_generator()]
