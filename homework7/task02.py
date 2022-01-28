"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def calculation_backspaces(text):
    new_list = []
    for char in text:
        if char != "#":
            new_list.append(char)
        elif len(new_list) > 0:
            new_list.pop()
    return "".join(new_list)


def backspace_comparation(first, second):
    return calculation_backspaces(first) == calculation_backspaces(second)
