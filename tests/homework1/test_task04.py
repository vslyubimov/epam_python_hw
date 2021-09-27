from homework1.task04 import check_sum_of_four

a = [2, 4, 6, 8]
b = [0, -4, 6, 8]
c = [-2, 0, -12, 8]
d = [0, 0, 0, -24]

a1 = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5]
b1 = [0, 6, -5, 5, 7, 2, 3, 6, 2, 3]
c1 = [0, 2, 3, 4, 5, 6, 7, 1, 6, 1]
d1 = [0, 3, -3, 4, 6, 7, 8, 9, 1, 3]

a2 = [0, 0]
b2 = [0, 0]
c2 = [0, 2]
d2 = [0, 0]


def test_task_04_abcd():
    assert check_sum_of_four(a, b, c, d) == 16


def test_task_04_a1b1c1d1():
    assert check_sum_of_four(a1, b1, c1, d1) == 32


def test_task_04_bb1c1d():
    assert check_sum_of_four(b, b1, c1, d) == 27


def test_task_04_ab1c1d():
    assert check_sum_of_four(a, b1, c1, d) == 9


def test_task_04_a2b2c2d2():
    assert check_sum_of_four(a2, b2, c2, d2) == 8
