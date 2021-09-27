"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""


import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "rb") as f:
        text = f.read().decode("unicode_escape")
        text = text.replace("-\n", "").replace("\n", " ")

        numbers = ''.join(list(map(str, range(0, 10))))
        punctuations = string.punctuation + numbers

        for p in punctuations:
            text = text.replace(p, "")

        text = set(text.split())
        longest_words = sorted(list(map(lambda x: [x, set(x)], text)),
                               key=lambda x: len(x[1]), reverse=True)[:10]
        answer = sorted([words[0] for words in longest_words])
        return answer


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "rb") as f:
        text = f.read().decode("unicode_escape")
        text = text.replace("-\n", "").replace("\n", " ").replace(" ", "")

        numbers = ''.join(list(map(str, range(0, 10))))
        punctuations = string.punctuation + numbers

        for p in punctuations:
            text = text.replace(p, "")

        letters = set(text)
        d = {letter: text.count(letter) for letter in letters}
        answer = sorted(d.items(), key=lambda item: item[1])
        end_answer = ''
        for i in range(len(answer)):
            if answer[i][1] == 1:
                end_answer += (answer[i][0])
            else:
                break
        return end_answer


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "rb") as f:
        counter = 0
        text = f.read().decode("unicode_escape")
        text = text.replace("-\n", "").replace("\n", " ").replace(" ", "")
        letters = string.punctuation
        for letter in text:
            if letter in letters:
                counter += 1
        return counter


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "rb") as f:
        counter = 0
        text = f.read().decode("unicode_escape")
        chars = set(text)
        for char in chars:
            try:
                char.encode().decode('ascii')
            except UnicodeDecodeError:
                counter += 1
        return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "rb") as f:
        text = f.read().decode("unicode_escape")
        text = text.replace("-\n", "").replace("\n", " ").replace(" ", "")
        non_ascii_chars = ''
        chars = set(text)
        for char in chars:
            try:
                char.encode().decode('ascii')
            except UnicodeDecodeError:
                pass
                non_ascii_chars += char
    d = {letter: text.count(letter) for letter in non_ascii_chars}
    answer = sorted(d.items(), key=lambda item: item[1])[-1][0]
    return answer
