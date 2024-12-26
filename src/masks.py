from typing import Union


def get_mask_card_number(num_car: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает его маску"""

    return f"{num_car[:4]} {num_car[4:6]}** **** {num_car[-4:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""

    return f"**{account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
