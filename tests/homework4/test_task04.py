from homework4.task04 import fizzbuzz


def test_fizzbuzz_doctest():
    """
        given n, return list
        :param n: int
        :return: list

        >>> fizzbuzz(5)
        ['1', '2', 'fizz', '4', 'buzz']

        >>> fizzbuzz(10)
        ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']
        """


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def test_fizzbuzz_pytest():
    assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
