import pytest

from homework7.task02 import backspace_comparation


@pytest.mark.parametrize(
    ("string1", "string2", "expected_result"),
    [
        (
                "ab#c",
                "ad#c",
                True,
        ),
        ("a#c", "b", False),
        ("c##a", "#c#a", True),
        ("", "", True),
    ],
)
def test_calc_backspace(string1, string2, expected_result):
    actual_result = backspace_comparation(string1, string2)
    assert expected_result == actual_result
