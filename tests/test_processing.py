from typing import Any
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_exe(checklist_1: list) -> Any:
    assert filter_by_state(checklist_1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canc(checklist_1: list) -> Any:
    assert filter_by_state(checklist_1, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_not_state(checklist_2: list) -> Any:
    assert filter_by_state(checklist_2) == []


def test_filter_by_state_not_state_1(checklist_3: list) -> Any:
    assert filter_by_state(checklist_3) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41425689, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_from_less(checklist_1: list) -> Any:
    assert sort_by_date(checklist_1, ascending=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_from_less_1(checklist_1: list) -> Any:
    assert sort_by_date(checklist_1, ascending=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
