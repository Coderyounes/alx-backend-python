#!/usr/bin/env python3
from typing import List
"""
    `typing` module: Type hints for readable, maintainable code
"""

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all the numbers in the input list.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all the numbers in the input list.
    """
    return float(sum(input_list))