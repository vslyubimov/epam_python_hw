import json
from pathlib import Path

import asynctest
import pytest
import homework10
from homework10.task01 import comp_info, get_page, get_page_comps


@pytest.mark.asyncio
async def test_get_company_info(monkeypatch):
    def fake_page(url):
        with open("test/m.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(homework10.task01, "get_page", fake_get_page)
    res = {
        "name": "AO Smith",
        "href": "/stocks/aos-stock",
        "growth": 38.31,
        "code": "AOS",
        "PE": 25.06,
        "price": 0,
        "profit": 0.85,
    }
    d = {"name": "AO Smith", "href": "/stocks/aos-stock", "growth": 38.31}
    actual_res = await comp_info(d, 0)
    assert res == actual_res


@pytest.mark.asyncio
async def test_get_companies_from_page(monkeypatch):
    def fake_page(url):
        with open("test/tab.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(homework10.task01, "get_page", fake_get_page)

    actual_res = await get_page_comps(1)
    assert actual_res[0]["name"] == "3M"
    assert actual_res[1]["name"] == "AO Smith"
    assert actual_res[2]["name"] == "Abbott Laboratories"


def test_json_form_test():
    for file in Path("./test/hw10").glob("*.json"):
        with open(file) as f:
            a = json.load(f)
            name = f.name[14:-5]
        assert len(a) == 10
        assert a[0] == max(a, key=lambda x: x[name])
        assert a[9] == min(a, key=lambda x: x[name])

