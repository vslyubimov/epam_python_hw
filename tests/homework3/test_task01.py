from homework3.task01 import cache


def check_x3_times_return():

    @cache(times=3)
    def f():
        return input('!! ')

    assert f(1)
    assert f()
    assert f()

# как это тестить блт
#check_x3_times_return()

