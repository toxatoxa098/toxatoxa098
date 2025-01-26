from typing import Union


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает его маску"""

    if not card_number or card_number.isspace() or card_number.isalpha():
        return "Номер карты отсутствует"
    else:
        digit_card_number = ""
        for element in card_number:
            if element.isdigit():
                digit_card_number += element
                masket = f"{digit_card_number[:4]} {digit_card_number[4:6]}** **** {digit_card_number[-4:]}"

    return masket


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""

    if not account_number or account_number.isspace() or account_number.isalpha():
        return "Номер счета отсутствует"
    else:
        digit_account_number = ""
        for element in account_number:
            if element.isdigit():
                digit_account_number += element
    return f"**{digit_account_number[-4:]}"


print(get_mask_card_number("7000792289606"))
print(get_mask_account("73654108430135874305"))
