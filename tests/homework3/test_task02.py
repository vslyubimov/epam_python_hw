import time

from homework3.task02 import pool_calculation, slow_calculate


def slow_calculation_loop(last_value):
    loop_range = range(0, last_value)
    return sum(slow_calculate(i) for i in loop_range)


def test_result_of_slow_calculation():
    assert pool_calculation(500, 30) == 1024259


def test_time_of_slow_calculation():
    start_time = time.time()
    pool_calculation(500, 30)
    end_time = time.time() - start_time
    assert end_time < 60


def test_equal_results_from_both_func():
    assert pool_calculation(5, 30) == slow_calculation_loop(5)
