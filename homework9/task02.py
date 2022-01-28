"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
# >>> with supressor(IndexError):
# ...    [][2]
"""

from contextlib import contextmanager
from typing import Any


@contextmanager
def suppressor(obj_exception: Exception) -> None:
    try:
        yield
    except obj_exception:
        pass


class Suppressor:
    def __init__(self, *exceptions: Any):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        return exctype is not None and issubclass(exctype, self._exceptions)
