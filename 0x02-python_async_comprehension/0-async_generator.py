#!/usr/bin/env python3
""" Documnetation """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields
    random floating-point numbers between 0 and 10.

    Yields:
        float: Random floating-point number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
