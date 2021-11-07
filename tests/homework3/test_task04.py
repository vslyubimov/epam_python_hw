from homework3.task04 import is_armstrong


def test_positive_armstrong_list():
    armstrong_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407,
                         1634, 8208, 9474, 54748, 92727, 93084, 548834,
                         1741725, 4210818, 9800817, 146511208, 472335975,
                         534494836, 912985153, 4679307774]

    for i in armstrong_numbers:
        assert is_armstrong(i)


def test_negative_armstrong():
    just_numbers = [10, 11, 12, 124, 555, 666]
    for i in just_numbers:
        assert not is_armstrong(i)
