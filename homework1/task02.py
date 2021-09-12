from typing import Sequence


def generate_fibonacci(start_from):
    a, b = 0, 1
    while True:
        if a >= start_from:
            yield a
        a, b = b, a + b


def check_fibonacci(data: Sequence[int]) -> bool:
    if data:
        first_element = data[0]
        for a, b in zip(data, generate_fibonacci(first_element)):
            if a != b:
                return False
        return True
    return False
