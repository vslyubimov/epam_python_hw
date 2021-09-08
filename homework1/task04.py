from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    counter = 0
    for i in range(0, len(a)):
        if a[i] + b[i] + c[i] + d[i] == 0:
            counter += 1
        else:
            continue
    return counter
