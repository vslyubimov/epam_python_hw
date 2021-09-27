from homework2.task04 import cache


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)
some_1 = 10, 2
some_2 = 4, 2
val_1_v1 = cache_func(*some_1)
val_2_v1 = cache_func(*some_1)
val_1_v2 = cache_func(*some_2)
val_2_v2 = cache_func(*some_2)


def test_task_04_1():
    assert val_1_v1 is val_2_v1


def test_task_04_2():
    assert val_1_v2 is val_2_v2
