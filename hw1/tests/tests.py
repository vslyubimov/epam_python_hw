import pytest

from tasks.task02 import check_fibonacci
from tasks.task03 import find_maximum_and_minimum
from tasks.task04 import check_sum_of_four
from tasks.task05 import find_maximal_subarray_sum


def test_task_02():
    check1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    check2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    check3 = [25, 26, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    assert check_fibonacci(check1)
    assert check_fibonacci(check2)
    assert check_fibonacci(check3)


def test_task_03():
    assert find_maximum_and_minimum("some_file.txt")


def test_task_04():
    a = [2, 4, 6, 8]
    b = [0, -4, 6, 8]
    c = [-2, 0, -12, 8]
    d = [0, 0, 0, -24]

    a1 = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    b1 = [0, 6, -5, 5, 7, 2, 3, 6, 2, 3]
    c1 = [0, 2, 3, 4, 5, 6, 7, 1, 6, 1]
    d1 = [0, 3, -3, 4, 6, 7, 8, 9, 1, 3]

    # check
    assert (check_sum_of_four(a, b, c, d),
            check_sum_of_four(a1, b1, c1, d1), check_sum_of_four(b, b1, c1, d), check_sum_of_four(a, b1, c1, d))


def test_task_05():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    nums_1 = [0, 2, -2, 4, 6, 7, 8, 9, 9, 12, 12, -4, -5, -22, -30]
    k_1 = 2

    nums_2 = [0, 1, 2, 3]
    k_2 = 10
    assert (find_maximal_subarray_sum(nums, k), find_maximal_subarray_sum(nums_1, k_1),
            find_maximal_subarray_sum(nums_2, k_2))
