from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(numbers: Union[str]) -> None:
    """Функция принимает на вход номер карты и возвращает его маску"""

    assert get_mask_card_number("7000 7922 8960 6361") == numbers
    assert get_mask_card_number("7000-7922-8960-6361") == numbers
    assert get_mask_card_number("7000aT792fd289HH606361") == numbers
    assert get_mask_card_number("7000792289606") == '7000 79** **** 9606'
    assert get_mask_card_number("") == 'Номер карты отсутствует'
    assert get_mask_card_number("hfdghfgdhfghd") == 'Номер карты отсутствует'


def test_get_mask_account(account: Union[str]) -> None:
    """Функция принимает на вход номер счета и возвращает его маску"""

    assert get_mask_account("73654108430135874305") == account
    assert get_mask_account("7365 4108TY4301s3587hhh4305") == account
    assert get_mask_account("7365 4108 4301 3587 4305") == account
    assert get_mask_account("7365-4108-4301-3587-4305") == account
    assert get_mask_account("108430135874305") == account
    assert get_mask_account("") == 'Номер счета отсутствует'
    assert get_mask_account("ythfjfhgkfhgjfgkfefg") == 'Номер счета отсутствует'
