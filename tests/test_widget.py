from typing import Union

import pytest

from src.widget import get_date, mask_account_card


def test_get_date(date: Union[str]) -> None:
    """Тест проверяет функцию на форматирование строки."""

    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'


def test_mask_account_card(account_card: Union[str]) -> None:
    """Тест проверяет функцию на маскировку номера счета и номера карты."""

    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
