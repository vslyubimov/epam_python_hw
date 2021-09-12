from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    counter = 0
    for item in product(a, b, c, d):
        if sum(item) == 0:
            counter += 1
    return counter
