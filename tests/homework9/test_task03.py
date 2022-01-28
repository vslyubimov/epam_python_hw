import os
from pathlib import Path

import pytest

from homework9.task03 import universal_file_counter


@pytest.fixture()
def start_dir():
    current = Path.cwd()
    temp_folder = Path('temp_folder')
    temp_folder.mkdir()
    for i in range(1, 3):
        filename = current / temp_folder / (str(i) + ".txt")
        with open(filename, "w") as f:
            f.write((((str(i) + " ") * i) + "\n") * i)
    yield Path(temp_folder)
    for i in range(1, 3):
        os.remove(current / temp_folder / (str(i) + ".txt"))
    temp_folder.rmdir()


def test_universal_file_counter(start_dir):
    assert universal_file_counter(start_dir, "txt") == 3
    assert universal_file_counter(start_dir, "txt", str.split) == 5
