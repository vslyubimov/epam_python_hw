from homework1.task04 import check_sum_of_four


def test_task_04():
    a = [2, 4, 6, 8]
    b = [0, -4, 6, 8]
    c = [-2, 0, -12, 8]
    d = [0, 0, 0, -24]

    a1 = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    b1 = [0, 6, -5, 5, 7, 2, 3, 6, 2, 3]
    c1 = [0, 2, 3, 4, 5, 6, 7, 1, 6, 1]
    d1 = [0, 3, -3, 4, 6, 7, 8, 9, 1, 3]

    assert (check_sum_of_four(a, b, c, d),
            check_sum_of_four(a1, b1, c1, d1), check_sum_of_four(b, b1, c1, d), check_sum_of_four(a, b1, c1, d))