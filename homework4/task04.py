from typing import List


def fizzbuzz(n: int) -> List[str]:
    result_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result_list.append('fizz buzz')
        elif i % 3 == 0:
            result_list.append('fizz')
        elif i % 5 == 0:
            result_list.append('buzz')
        else:
            result_list.append(str(i))
    return result_list
