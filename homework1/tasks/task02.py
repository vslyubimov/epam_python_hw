from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    for element in range(2, len(data)):
        if data[element] == data[element - 1] + data[element - 2]:
            continue
        else:
            return False
    return True

"""
пока не разобрался почему, но если мы имеем:
        else:
            return False
    return True
то тесты от check2 и check3 не работают. А так работает :/
"""