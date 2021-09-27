import os.path

import homework2.task01 as task1

file_path = os.path.join(os.path.dirname
                         (os.path.abspath(__file__)), 'data.txt')


def test_get_longest_diverse_words():
    assert task1.get_longest_diverse_words(file_path) == \
           ['Bevölkerungsabschub',
            'Kollektivschuldiger',
            'Schicksalsfiguren',
            'Selbstverständlich',
            'Souveränitätsansprüche',
            'Verwaltungsmaßnahme',
            'Werkstättenlandschaft',
            'symbolischsakramentale',
            'unmißverständliche',
            'unverhältnismäßig']


def test_get_rarest_char():
    rarest_chars = 'X‹Y›’î'
    assert sorted(task1.get_rarest_char(file_path)) == \
           sorted(rarest_chars)


def test_count_punctuation_chars():
    assert task1.count_punctuation_chars(file_path) == 4336


def test_count_non_ascii_chars():
    assert task1.count_non_ascii_chars(file_path) == 15


def test_get_most_common_non_ascii_char():
    assert task1.get_most_common_non_ascii_char(file_path) == \
           b'\xc3\xa4'.decode()
