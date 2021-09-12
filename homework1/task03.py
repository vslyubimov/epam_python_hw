from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    max_value = 1
    min_value = 1
    with open(file_name) as fi:
        for line in fi:
            if int(line) > max_value:
                max_value = int(line)
            elif int(line) < min_value:
                min_value = int(line)
            else:
                continue
        result = min_value, max_value
    return result
