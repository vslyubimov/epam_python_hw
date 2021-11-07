import string

from homework2.task05 import custom_range


def test_custom_range_to_g():
    assert custom_range(string.ascii_lowercase, end='g') == \
           ['a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_from_g_to_p():
    assert custom_range(string.ascii_lowercase, 'g', 'p') == \
           ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_custom_range_from_p_to_g_step2():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == \
           ['p', 'n', 'l', 'j', 'h']
