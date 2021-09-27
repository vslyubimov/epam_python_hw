import homework1.task02 as task2


def test_task_02_version_1_positive():
    check1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert task2.check_fibonacci_version_1(check1)


def test_task_02_version_1_negative():
    check2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert not task2.check_fibonacci_version_1(check2)


def test_task_02_version_1_random_numbers():
    check3 = [4, -5, 9, -14]
    assert not task2.check_fibonacci_version_1(check3)


def test_task_02_version_1_empty():
    check4 = []
    assert not task2.check_fibonacci_version_1(check4)


def test_task_02_version_1_two_first_elements():
    check5 = [0, 1]
    assert task2.check_fibonacci_version_1(check5)


def test_task_02_version_1_two_random_elements():
    check6 = [55, 66]
    assert not task2.check_fibonacci_version_1(check6)


def test_task_02_version_1_in_the_middle():
    check7 = [3, 5, 8, 13, 21, 34]
    assert task2.check_fibonacci_version_1(check7)


# versions 2


def test_task_02_version_2_positive():
    check1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert task2.check_fibonacci_version_2(check1)


def test_task_02_version_2_negative():
    check2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert not task2.check_fibonacci_version_2(check2)


def test_task_02_version_2_random_numbers():
    check3 = [4, -5, 9, -14]
    assert not task2.check_fibonacci_version_2(check3)


def test_task_02_version_2_empty():
    check4 = []
    assert not task2.check_fibonacci_version_2(check4)


def test_task_02_version_2_two_first_elements():
    check5 = [0, 1]
    assert task2.check_fibonacci_version_2(check5)


def test_task_02_version_2_in_the_middle():
    check7 = [3, 5, 8, 13, 21, 34]
    assert task2.check_fibonacci_version_2(check7)
