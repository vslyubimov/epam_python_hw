import pytest
import requests

from homework4.task02 import count_dots_on_i


class MockingResponce:
    @property
    def text(self):
        return "i i i i i asdghjkl"


@pytest.fixture()
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockingResponce()
    monkeypatch.setattr(requests, "get", mock_get)


@pytest.mark.usefixtures("mock_response")
def test_mock_count_dots_on_i_positive():
    result = count_dots_on_i("asd")
    assert result == 5


@pytest.mark.xfail(raises=ValueError)
def test_network_exception_passing():
    count_dots_on_i("asdf")
