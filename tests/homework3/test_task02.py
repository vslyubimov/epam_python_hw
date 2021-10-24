from homework3.task02 import pool_calculation


def test_result_of_slow_calculation():
    assert pool_calculation() == 1024259
