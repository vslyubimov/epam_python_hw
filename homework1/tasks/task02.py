from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    for element in range(2, len(data)):
        if data[element] == data[element - 1] + data[element - 2]:
            continue
        else:
            return False
    return True

