from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(state: str, expected: List[Dict[str, Any]], filter_state: List[Dict[str, Any]]) -> None:
    assert filter_by_state(filter_state, state) == expected


def test_sort_by_date(sort_date: List[Dict[str, Any]], default_parameter: bool = False) -> None:
    """Функция, принимает список словарей и необязательный
    параметр, задающий порядок сортировки (по умолчанию — убывание) и возвращает
    новый список, отсортированный по дате (date)."""

    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert (sort_by_date(sort_date, default_parameter=True)) == expected


def test_sort_by_date(sort_date: List[Dict[str, Any]], default_parameter: bool = True) -> None:
    """Функция, принимает список словарей и необязательный
    параметр, задающий порядок сортировки (по умолчанию — возрастание) и возвращает
    новый список, отсортированный по дате (date)."""

    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    assert (sort_by_date(sort_date, default_parameter=True)) == expected


def test_sort_by_date(sort_double_date: List[Dict[str, Any]], default_parameter: bool = True) -> None:
    """Проверка корректности сортировки при одинаковых датах."""

    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-09-12T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    assert (sort_by_date(sort_double_date, default_parameter=True)) == expected


def test_filter_by_state(filter_no_state_1: List[Dict[str, Any]]) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке."""

    expected = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

    assert (filter_by_state(filter_no_state_1, "EXECUTED")) == expected


def test_filter_by_state(filter_no_state_2: List[Dict[str, Any]]) -> None:
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке."""

    expected = [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]

    assert (filter_by_state(filter_no_state_2, "CANCELED")) == expected
