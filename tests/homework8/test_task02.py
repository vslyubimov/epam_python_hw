import pytest

from homework8.task02 import TableData


@pytest.fixture()
def presidents():
    filename = "tests/homework8/example.sqlite"
    with TableData(database_name=filename, table_name="presidents") as f:
        yield f


def test_len_presidents(presidents):
    assert len(presidents) == 3


def test_items_presidents(presidents):
    assert presidents["Yeltsin"] == \
           {"age": 999, "country": "Russia", "name": "Yeltsin"}


def test_insides_positive(presidents):
    assert "Yeltsin" in presidents


def test_insides_negative(presidents):
    assert ("Washington" in presidents) is False


def test_iteration(presidents):
    names = [president["name"] for president in presidents]
    assert names == ["Yeltsin", "Trump", "Big Man Tyrone"]
