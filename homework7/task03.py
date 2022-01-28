"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""


def tic_tac_toe_checker(board):
    a, b, c = board
    diagonal_1 = [a[0], a[1], a[2]]
    diagonal_2 = [a[2], b[1], c[0]]
    diagonals = [diagonal_1, diagonal_2]
    for rows in [board, zip(*board), diagonals]:
        for line in rows:
            if "-" not in line and len(set(line)) == 1:
                return f"{line[0]} wins!"
    if "-" in {char for line in board for char in line}:
        return "unfinished!"
    return "draw!"
