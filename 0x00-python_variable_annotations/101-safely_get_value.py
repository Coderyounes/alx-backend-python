#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[Any, T] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with
    the given key from the dictionary.
    If the key is not found, returns the default value.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Union[Any, T], optional):
        The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
