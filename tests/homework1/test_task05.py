from homework1.task05 import find_maximal_subarray_sum


def test_task_05_1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 16


def test_task_05_2():
    nums = [0, 2, -2, 4, 6, 7, 8, 9, 9, 12, 12, -4, -5, -22, -30]
    k = 2
    assert find_maximal_subarray_sum(nums, k) == 24


def test_task_05_3():
    nums = [0, 1, 2, 3]
    k = 4
    assert find_maximal_subarray_sum(nums, k) == 6


def test_task_05_4():
    nums = [1, 4, 7, -10, 6, 1, 1]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 12


def test_task_05_5():
    nums = [1, 3, -1, -3, 5, -3, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 13
