from homework3.task01 import cache


def check_x3_times_return():
    @cache(times=3)
    def f():
        return input('!! ')

    # assert f(1)
    # assert f()
    # assert f()

# check_x3_times_return()
# !!! забыл сделать тест, доделаю познее
