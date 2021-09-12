from homework1.task05 import find_maximal_subarray_sum

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

nums_1 = [0, 2, -2, 4, 6, 7, 8, 9, 9, 12, 12, -4, -5, -22, -30]
k_1 = 2

nums_2 = [0, 1, 2, 3]
k_2 = 10


def test_task_05_1():
    assert find_maximal_subarray_sum(nums, k) == 16


def test_task_05_2():
    assert find_maximal_subarray_sum(nums_1, k_1) == 24


def test_task_05_3():
    assert find_maximal_subarray_sum(nums_2, k_2) == 6
