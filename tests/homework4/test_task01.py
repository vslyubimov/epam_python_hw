import os
from random import randrange, uniform

from homework4.task01 import read_magic_number


def test_reading_file():
    filename = "test_read_magic_number_file.txt"
    repository = 'homework4'
    abs_path = os.path.abspath(os.path.join(__file__, "../../.."))
    file_path = os.path.join(abs_path, repository, filename)
    file = open(file_path, "w")
    file.write("5")
    file.close()
    assert read_magic_number(file_path)
    os.remove(file_path)


def test_negative_random_int_in_interval_1_3():
    filename = "test_read_magic_number_file.txt"
    repository = 'homework4'
    abs_path = os.path.abspath(os.path.join(__file__, "../../.."))
    file_path = os.path.join(abs_path, repository, filename)
    file = open(file_path, "w")
    file.write(str(randrange(1, 3)))
    file.close()
    assert not read_magic_number(file_path)
    os.remove(file_path)


def test_negative_random_float_in_interval_1_3():
    filename = "test_read_magic_number_file.txt"
    repository = 'homework4'
    abs_path = os.path.abspath(os.path.join(__file__, "../../.."))
    file_path = os.path.join(abs_path, repository, filename)
    file = open(file_path, "w")
    file.write(str(uniform(1, 3)))
    file.close()
    assert not read_magic_number(file_path)
    os.remove(file_path)
