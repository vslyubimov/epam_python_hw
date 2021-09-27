from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    return list(map(list, product(*args)))


def combinations_v2(*args: List[Any]) -> List[List]:
    result = [[]]
    for a in args:
        result = [x + [y] for x in result for y in a]
    return result
