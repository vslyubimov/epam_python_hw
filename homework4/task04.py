from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
            given n, return list
            :param n: int
            :return: list

            >>> fizzbuzz(5)
            ['1', '2', 'fizz', '4', 'buzz']

            >>> fizzbuzz(10)
            ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']

            >>> fizzbuzz(1)
            ['1']
            """

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
