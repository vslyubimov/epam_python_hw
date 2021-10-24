"""
In previous homework task 4, you wrote a cache function that remembers other
function output value. Modify it to be a parametrized decorator,
so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead
f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""

import functools


def cache(times):
    def wrapped_cache(func):
        cache_dict = {}
        counter = times

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            nonlocal counter
            if counter > 0 and args in cache_dict:
                counter -= 1
                return cache_dict[args]
            else:
                values_to_cache = func(*args, **kwargs)
                cache_dict[args] = values_to_cache
                counter = times - 1
                return values_to_cache
        return wrapped_func
    return wrapped_cache
