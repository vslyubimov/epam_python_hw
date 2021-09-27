from homework2.task02 import major_and_minor_elem


def test_task_02_v1():
    test_data = [2, 2, 1, 1, 1, 2, 2]
    assert major_and_minor_elem(test_data) == (2, 1)


def test_task_02_v2():
    test_data = [3, 4, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 8, 8, 8, 1]
    assert major_and_minor_elem(test_data) == (8, 1)
