import pytest

from homework4.task03 import my_precious_logger


@pytest.mark.parametrize(
    ("stderr_input", "stdout_input"),
    [("error", "all right")])
def test_logger(capsys, stderr_input, stdout_input):
    my_precious_logger(stderr_input)
    my_precious_logger(stdout_input)
    caught = capsys.readouterr()
    assert caught.err == stderr_input
    assert caught.out == stdout_input
