#!/usr/bin/env python3
from typing import Union, Tuple
"""
    `typing` module: Type hints for readable, maintainable code
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair to a tuple where the value is squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The value,
            which can be either an integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return (k, v * v)
