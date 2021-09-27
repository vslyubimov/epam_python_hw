"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib",
    which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""


from typing import Sequence


def generate_fibonacci(start_from):
    a, b = 0, 1
    while True:
        if a >= start_from:
            yield a
        a, b = b, a + b


def check_fibonacci_version_1(data: Sequence[int]) -> bool:
    """

    :rtype: object
    """
    if data:
        first_element = data[0]
        for a, b in zip(data, generate_fibonacci(first_element)):
            if a != b:
                return False
        return True
    return False


def check_fibonacci_version_2(data: Sequence[int]) -> bool:
    if data:
        for element in range(2, len(data)):
            if data[element] == data[element - 1] + data[element - 2]:
                continue
            else:
                return False
        return True
