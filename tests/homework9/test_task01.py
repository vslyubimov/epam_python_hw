import os

import pytest

from homework9.task01 import merge_sorted_files


@pytest.fixture()
def create_files(text1, text2):
    args = [text1, text2]
    for i, text in enumerate(args):
        file = f"test{i}_{i}.txt"
        with open(file, "w") as f:
            f.write(text)
    yield tuple(f"test{i}_{i}.txt" for i in range(len(args)))
    for i in range(len(args)):
        os.remove(f"test{i}_{i}.txt")


@pytest.mark.parametrize(
    ("text1", "text2"),
    [
        ("1\n3\n5\n7\n9", "2\n4\n6\n8\n10"),
    ],
)
def test_merge_sorted_files(create_files):
    for i, j, in zip(range(1, 11), merge_sorted_files(create_files)):
        assert i == j
