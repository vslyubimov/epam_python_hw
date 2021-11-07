"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') ==
                        ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
                        ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
                        ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(data, start=None, end=None, step=None):
    if not start:
        start = data[0]
    start_index = data.index(start)
    end_index = data.index(end)
    return list(data[start_index:end_index:step])
