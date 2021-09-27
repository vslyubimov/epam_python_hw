from homework1.task01 import check_power_of_2


def test_positive_case_1():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_positive_case_2():
    assert check_power_of_2(8)


def test_positive_case_3():
    assert check_power_of_2(256)


def test_positive_case_4():
    assert check_power_of_2(2048)


def test_negative_case_1():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_negative_case_2():
    assert not check_power_of_2(0)


def test_negative_case_3():
    assert not check_power_of_2(-16)
