import pytest
from typing import List, Dict, Any
from src.filtering_by_given_parameters import (
    filter_transactions_by_currency,
    filter_transactions_by_status,
    search_transactions_by_description,
    sort_transactions_by_date,
)


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58Z",
            "amount": "31957.58",
            "currency": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25Z",
            "amount": "67314.70",
            "currency": "USD",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29Z",
            "amount": "8221.37",
            "currency": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 35383033474447895560",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": "2019-11-05T12:04:13Z",
            "amount": "21344.35",
            "currency": "RUB",
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381",
        },
    ]


def test_filter_transactions_by_status(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест на проверку филтрации по статусу."""

    # Проверка по статусу EXECUTED
    executed_transactions = filter_transactions_by_status(sample_transactions, "EXECUTED")
    assert len(executed_transactions) == 2
    assert all(t["state"] == "EXECUTED" for t in executed_transactions)

    # Проверка по статусу CANCELED
    canceled_transactions = filter_transactions_by_status(sample_transactions, "CANCELED")
    assert len(canceled_transactions) == 1
    assert all(t["state"] == "CANCELED" for t in canceled_transactions)

    # Проверка по статусу PENDING
    pending_transactions = filter_transactions_by_status(sample_transactions, "PENDING")
    assert len(pending_transactions) == 1
    assert all(t["state"] == "PENDING" for t in pending_transactions)

    # Проверка на чувствительность к регистру
    mixed_case_executed = filter_transactions_by_status(sample_transactions, "ExEcUtEd")
    assert len(mixed_case_executed) == 2
    assert all(t["state"] == "EXECUTED" for t in mixed_case_executed)


def test_sort_transactions_by_date(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест на проверку сортировки по дате(на убывание и на возрастание)."""

    # Проверка на возрастание
    sorted_asc = sort_transactions_by_date(sample_transactions, ascending=True)
    assert [t["id"] for t in sorted_asc] == [2, 3, 1, 4]

    # Проверка на убывание
    sorted_desc = sort_transactions_by_date(sample_transactions, ascending=False)
    assert [t["id"] for t in sorted_desc] == [4, 1, 3, 2]


def test_filter_transactions_by_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест на проверку фильтрации по заданной валюте."""

    # Проверка на валюту RUB
    rub_transactions = filter_transactions_by_currency(sample_transactions, "RUB")
    assert len(rub_transactions) == 0
    assert all(t["currency"] == "RUB" for t in rub_transactions)

    # Проверка на валюту USD
    usd_transactions = filter_transactions_by_currency(sample_transactions, "USD")
    assert len(usd_transactions) == 0
    assert all(t["currency"] == "USD" for t in usd_transactions)


def test_search_transactions_by_description(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест на проверку фильрации по ключевому слову."""

    org_transfers = search_transactions_by_description(sample_transactions, "Перевод организации")
    assert len(org_transfers) == 2
    assert all("Перевод организации" in t["description"] for t in org_transfers)
    account_transfers = search_transactions_by_description(sample_transactions, "счета на счет")
    assert len(account_transfers) == 1
    assert all("счета на счет" in t["description"].lower() for t in account_transfers)

    partial_match = search_transactions_by_description(sample_transactions, "перевод")
    assert len(partial_match) == 3

    no_match = search_transactions_by_description(sample_transactions, "несуществующее описание")
    assert len(no_match) == 0
