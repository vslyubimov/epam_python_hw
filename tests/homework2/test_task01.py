import os.path

import homework2.task01 as task1

file_path = os.path.join(os.path.dirname
                         (os.path.abspath(__file__)), 'data.txt')


def test_get_longest_diverse_words():
    assert task1.get_longest_diverse_words(file_path) == [
        "politisch-strategischen",
        "Verfassungsverletzungen",
        "Souveränitätsansprüche",
        "Mehrheitsvorstellungen",
        "zoologisch-politischen",
        "Wiederbelebungsübungen",
        "Werkstättenlandschaft",
        "résistance-Bewegungen",
        "Entscheidungsschlacht",
        "politisch-technischen",
    ]


def test_get_rarest_char():
    assert task1.get_rarest_char(file_path) == \
           ["›", "‹", "Y", "î", "’", "X", "(", ")"]


def test_count_punctuation_chars():
    assert task1.count_punctuation_chars(file_path) == {
        "'": 3,
        "(": 1,
        ")": 1,
        ",": 2489,
        "-": 1016,
        ".": 1615,
        ":": 79,
        ";": 73,
        "?": 28,
        "«": 43,
        "»": 43,
        "‹": 1,
        "›": 1,
    }


def test_count_non_ascii_chars():
    assert task1.count_non_ascii_chars(file_path) == {
        "Ü": 42,
        "»": 43,
        "«": 43,
        "—": 81,
        "ß": 708,
        "ü": 804,
        "ä": 866,
        "ö": 357,
        "›": 1,
        "‹": 1,
        "Ä": 15,
        "Ö": 3,
        "é": 6,
        "î": 1,
        "’": 1,
    }


def test_get_most_common_non_ascii_char():
    assert task1.get_most_common_non_ascii_char(file_path) == "ä"
