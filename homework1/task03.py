from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    max = 1
    min = 1
    with open(file_name) as fi:
        for line in fi:
            if int(line) > max:
                max = int(line)
            elif int(line) < min:
                min = int(line)
            else:
                continue
        a = min, max
        print(a)
        return a
