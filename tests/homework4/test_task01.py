import os

import pytest

from homework4.task01 import read_magic_number


@pytest.mark.parametrize(("filename", "file_text", "result_bool"),
                         [("test_read_magic_number_file.txt", "2", True)])
def test_magic_number_true(filename, file_text, result_bool):
    try:
        with open(filename, "w") as f:
            f.write(file_text)
        assert result_bool == read_magic_number(f.name)
    except Exception as e:
        raise e
    finally:
        os.unlink(f.name)


@pytest.mark.parametrize(("filename", "file_text", "result_bool"),
                         [("test_read_magic_number_file.txt", "5", False)])
def test_magic_number_false(filename, file_text, result_bool):
    try:
        with open(filename, "w") as f:
            f.write(file_text)
        assert result_bool == read_magic_number(f.name)
    except Exception as e:
        raise e
    finally:
        os.unlink(f.name)
