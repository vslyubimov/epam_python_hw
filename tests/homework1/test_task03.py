import os.path

from homework1.task03 import find_maximum_and_minimum


def test_task_03():
    assert find_maximum_and_minimum(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'some_file.txt'))
