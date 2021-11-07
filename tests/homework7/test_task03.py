import pytest

from homework7.task03 import tic_tac_toe_checker

table_unfinished = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
win_x = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
win_o = [["-", "-", "o"], ["-", "o", "o"], ["o", "x", "x"]]
table_draw = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "x"]]


@pytest.mark.parametrize(
    ("table", "expected_result"),
    [
        (win_x, "x wins!"),
        (win_o, "o wins!"),
        (table_unfinished, "unfinished!"),
        (table_draw, "draw!"),
    ],
)
def test_tic_tac_toe(table, expected_result):
    actual_result = tic_tac_toe_checker(table)
    assert actual_result == expected_result
