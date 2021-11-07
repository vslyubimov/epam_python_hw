from homework11.task01 import SimplifiedEnum


class RandomEnums(metaclass=SimplifiedEnum):
    __keys = ("Anything", "Nothing")


def test_enums():
    assert RandomEnums.Anything == "Anything"


def test_negative():
    assert not RandomEnums.Nothing != "Nothing"
