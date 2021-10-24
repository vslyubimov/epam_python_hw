import sys

from homework4.task03 import my_precious_logger


def test_basic_functional():
    assert my_precious_logger('hey') == sys.stderr.write("hey")
    # .readouterr()


def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"
