import pytest

from homework9.task02 import Suppressor, suppressor


def test_class_not_suppress():
    with pytest.raises(ZeroDivisionError):
        with suppressor(IndexError):
            1 / 0


def test_class_suppressor():
    with Suppressor(IndexError):
        [][2]


def test_gen_suppressor():
    with suppressor(IndexError):
        [][2]


def test_gen_not_supress():
    with pytest.raises(ZeroDivisionError):
        with Suppressor(IndexError):
            1 / 0


def test_subclass_exceptions():
    with Suppressor(Exception):
        raise IndexError()
    with suppressor(Exception):
        raise IndexError()
