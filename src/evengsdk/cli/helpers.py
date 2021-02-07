# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import html
from typing import Dict, List


def to_human_readable(
    obj: Dict,
    keys: List[str] = []
) -> str:
    """Generate human readable output for passed object

    Args:
        obj (dict): Object to format
        keys (list[str]): list of keys to print output for

    Returns:
        str: formatted string output
    """
    keys_to_drop = set(obj) - set(keys) if keys else set()
    for key in keys_to_drop:
        del obj[key]

    for key, val in obj.items():
        if isinstance(val, str):
            escaped_val = html.unescape(val)
            yield f'  {key}: {escaped_val}'
        elif isinstance(val, int):
            yield f'  {key}: {val}'


def thread_executor(func, items):
    futures = list()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for future in executor.map(func, items):
            futures.append(future)
    return futures
