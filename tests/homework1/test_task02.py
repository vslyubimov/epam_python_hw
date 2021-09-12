from homework1.task02 import check_fibonacci

check1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
check2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
check3 = [4, -5, 9, -14]
check4 = []
check5 = [0, 1]
check6 = [55, 66]
check7 = [3, 5, 8, 13, 21, 34]


def test_task_02_positive():
    assert check_fibonacci(check1)


def test_task_02_negative():
    assert not check_fibonacci(check2)


def test_task_02_random_numbers():
    assert not check_fibonacci(check3)


def test_task_02_empty():
    assert not check_fibonacci(check4)


def test_task_02_two_first_elements():
    assert check_fibonacci(check5)


def test_task_02_two_random_elements():
    assert not check_fibonacci(check6)


def test_task_02_in_the_middle():
    assert check_fibonacci(check7)
