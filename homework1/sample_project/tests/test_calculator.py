import pytest

from sample_project.calculator.calc import check_power_of_2

def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)
    assert check_power_of_2(8)
    assert check_power_of_2(256)
    assert check_power_of_2(2048)
def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)
    assert not check_power_of_2(0)
    assert not check_power_of_2(-16)
