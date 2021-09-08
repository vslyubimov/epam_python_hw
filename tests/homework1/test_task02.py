from homework1.task02 import check_fibonacci


check1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
check2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
check3 = [25, 26, 3]


def test_task_02_Positive():

    assert check_fibonacci(check1)


def test_task_02_Negative():

    assert not check_fibonacci(check2)
"""
доделаю код с 2 и менее элементами для этой проверки
def test_task_02_Negative_two_elements():
    assert not check_fibonacci(check3)
"""