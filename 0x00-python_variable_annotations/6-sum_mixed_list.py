#!/usr/bin/env python3
"""
    `typing` module: Type hints for readable, maintainable code
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
            The mixed list of integers and floats.

    Returns:
        float: The sum of the mixed list.

    """
    return float(sum(mxd_lst))
